from unittest import TestCase, mock

from core import BotTelegramCore
from bot import JerimumBot


class SingletonTest(TestCase):
    @mock.patch('core.telegram.Updater')
    def test_same_jerimum(self, mocked_updater):
        i1 = JerimumBot()
        i2 = JerimumBot()
        self.assertEqual(i1, i2)

    @mock.patch('core.telegram.Updater')
    def test_core_initialize_error(self, mocked_updater):
        self.assertRaises(TypeError, BotTelegramCore)

    @mock.patch('core.telegram.Updater')
    def test_jerimum_initialize(self, mocked_updater):
        i1 = JerimumBot()
        i2 = BotTelegramCore()
        self.assertEqual(i1, i2)
