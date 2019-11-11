from unittest import TestCase

import pytest
import pendulum

from db import CommandCall
from tests.fixtures import mongo  # noqa F401


@pytest.mark.usefixtures('mongo')
class CommandCallTest(TestCase):
    def test_ordering(self):
        c1 = CommandCall(user='123',
                         _value=CommandCall.COACH,
                         _datetime=pendulum.yesterday()).save()
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.now()).save()
        self.assertAlmostEqual(CommandCall.objects.count(), 2)
        self.assertEqual(CommandCall.objects.first(), c1)

    def test_coach_ordering(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.yesterday()).save()
        c2 = CommandCall(user='123',
                         _value=CommandCall.COACH,
                         _datetime=pendulum.now()).save()
        self.assertAlmostEqual(CommandCall.objects.count(), 2)
        self.assertEqual(CommandCall.last_coach(), c2)

    def test_clima_ordering(self):
        CommandCall(user='123',
                         _value=CommandCall.CLIMA,
                         _datetime=pendulum.yesterday()).save()
        c2 = CommandCall(user='123',
                         _value=CommandCall.CLIMA,
                         _datetime=pendulum.now()).save()
        self.assertAlmostEqual(CommandCall.objects.count(), 2)
        self.assertEqual(CommandCall.last_clima(), c2)

    def test_coach(self):
        CommandCall.coach('123')
        self.assertAlmostEqual(CommandCall.objects.count(), 1)
        self.assertEqual(CommandCall.objects.first()._value, CommandCall.COACH)

    def test_clima(self):
        CommandCall.clima('123')
        self.assertAlmostEqual(CommandCall.objects.count(), 1)
        self.assertEqual(CommandCall.objects.first()._value, CommandCall.CLIMA)

    def test_get_value(self):
        c = CommandCall.coach('123')
        self.assertAlmostEqual(CommandCall.objects.count(), 1)
        self.assertEqual(c.value,
                         CommandCall.CHOICES
                         .get(CommandCall.COACH))

    def test_set_value(self):
        c = CommandCall.coach('123')
        self.assertAlmostEqual(CommandCall.objects.count(), 1)
        self.assertEqual(c.value,
                         CommandCall.CHOICES
                         .get(CommandCall.COACH))

        c.value = '1'
        self.assertEqual(c._value, '1')

        c.value = '2'
        self.assertEqual(c._value, '2')

        self.assertRaises(ValueError, setattr, c, 'value', 'TESTE')

    def test_is_cooldown_over_true(self):
        c = CommandCall(user='123',
                        _value=CommandCall.COACH,
                        _datetime=pendulum.yesterday()).save()
        self.assertTrue(c.is_cooldown_over())

    def test_is_cooldown_over_true_2(self):
        c = CommandCall(user='123',
                        _value=CommandCall.COACH,
                        _datetime=pendulum.now().subtract(seconds=CommandCall.COOLDOWN)).save()
        self.assertTrue(c.is_cooldown_over())

    def test_is_cooldown_over_false(self):
        c = CommandCall(user='123',
                        _value=CommandCall.COACH,
                        _datetime=pendulum.now()).save()
        self.assertFalse(c.is_cooldown_over())

    def test_allow_call_coach_true_empty(self):
        self.assertTrue(CommandCall.allow_call(command=CommandCall.COACH))

    def test_allow_call_coach_true(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.yesterday()).save()
        self.assertTrue(CommandCall.allow_call(command=CommandCall.COACH))

    def test_allow_call_coach_false(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.now()).save()
        self.assertFalse(CommandCall.allow_call(command=CommandCall.COACH))

    def test_allow_call_clima_true_empty(self):
        self.assertTrue(CommandCall.allow_call(command=CommandCall.CLIMA))

    def test_allow_call_clima_true(self):
        CommandCall(user='123',
                    _value=CommandCall.CLIMA,
                    _datetime=pendulum.yesterday()).save()
        self.assertTrue(CommandCall.allow_call(command=CommandCall.CLIMA))

    def test_allow_call_clima_false(self):
        CommandCall(user='123',
                    _value=CommandCall.CLIMA,
                    _datetime=pendulum.now()).save()
        self.assertFalse(CommandCall.allow_call(command=CommandCall.CLIMA))

    def test_allow_call_clima_coach_true(self):
        CommandCall(user='123',
                    _value=CommandCall.CLIMA,
                    _datetime=pendulum.now()).save()
        self.assertTrue(CommandCall.allow_call(command=CommandCall.COACH))

    def test_allow_call_coach_clima_true(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.now()).save()
        self.assertTrue(CommandCall.allow_call(command=CommandCall.CLIMA))

    def test_allow_call_shared_true(self):
        self.assertTrue(CommandCall.allow_call(shared=True))

    def test_allow_call_shared_true_1(self):
        CommandCall(user='123',
                    _value=CommandCall.CLIMA,
                    _datetime=pendulum.yesterday()).save()
        self.assertTrue(CommandCall.allow_call(shared=True))

    def test_allow_call_shared_true_2(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.yesterday()).save()
        self.assertTrue(CommandCall.allow_call(shared=True))

    def test_allow_call_shared_false_1(self):
        CommandCall(user='123',
                    _value=CommandCall.CLIMA,
                    _datetime=pendulum.now()).save()
        self.assertFalse(CommandCall.allow_call(shared=True))

    def test_allow_call_shared_false_2(self):
        CommandCall(user='123',
                    _value=CommandCall.COACH,
                    _datetime=pendulum.now()).save()
        self.assertFalse(CommandCall.allow_call(shared=True))
