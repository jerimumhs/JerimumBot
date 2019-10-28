from unittest import TestCase

import pytest
import pendulum

from db import Status
from tests.fixtures import mongo  # noqa F401


@pytest.mark.usefixtures('mongo')
class StatusTest(TestCase):
    def test_ordering(self):
        s1 = Status(user=123, _value=Status.ABERTA, _datetime=pendulum.yesterday()).save()
        Status(user=123, _value=Status.FECHADA, _datetime=pendulum.now()).save()
        self.assertAlmostEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.first(), s1)

    def test_now_ordering(self):
        Status(user=123, _value=Status.ABERTA, _datetime=pendulum.yesterday()).save()
        s2 = Status(user=123, _value=Status.FECHADA, _datetime=pendulum.now()).save()
        self.assertAlmostEqual(Status.objects.count(), 2)
        self.assertEqual(Status.now(), s2)

    def test_aberta(self):
        Status.aberta(123)
        self.assertAlmostEqual(Status.objects.count(), 1)
        self.assertEqual(Status.now()._value, Status.ABERTA)

    def test_fechada(self):
        Status.fechada(123)
        self.assertAlmostEqual(Status.objects.count(), 1)
        self.assertEqual(Status.now()._value, Status.FECHADA)

    def test_get_value(self):
        s = Status.aberta(123)
        self.assertAlmostEqual(Status.objects.count(), 1)
        self.assertEqual(s.value, Status.CHOICES.get(Status.ABERTA).get('name'))

    def test_set_value(self):
        s = Status.aberta(123)
        self.assertAlmostEqual(Status.objects.count(), 1)
        self.assertEqual(Status.now().value, Status.CHOICES.get(Status.ABERTA).get('name'))

        s.value = 'f'
        self.assertEqual(s._value, 'f')

        s.value = 'a'
        self.assertEqual(s._value, 'a')

        self.assertRaises(ValueError, setattr, s, 'value', 'TESTE')

    def test_sticker(self):
        s = Status.aberta(123)
        self.assertAlmostEqual(Status.objects.count(), 1)
        self.assertEqual(s.sticker, Status.CHOICES.get(Status.ABERTA).get('sticker'))
