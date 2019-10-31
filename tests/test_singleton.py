from unittest import TestCase

from core import BotTelegramCore
from bot import JerimumBot


class SingletonTest(TestCase):
    def test_same_jerimum(self):
        i1 = JerimumBot()
        i2 = JerimumBot()
        self.assertEqual(i1, i2)

    def test_core_initialize_error(self):
        self.assertRaises(TypeError, BotTelegramCore)

    def test_jerimum_initialize(self):
        i1 = JerimumBot()
        i2 = BotTelegramCore()
        self.assertEqual(i1, i2)
