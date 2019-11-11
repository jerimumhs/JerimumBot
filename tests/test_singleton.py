from unittest import TestCase, mock

from core import BotTelegramCore
from bot import JerimumBot


class SingletonTest(TestCase):
    def setUp(self):
        BotTelegramCore._instance = None

    @mock.patch('core.telegram.Updater')
    def test_same_jerimum(self, mocked_updater):
        i1 = JerimumBot.instance()
        i2 = JerimumBot.instance()
        self.assertIs(i1, i2)

    @mock.patch('core.telegram.Updater')
    def test_core_initialize_error(self, mocked_updater):
        self.assertRaises(TypeError, BotTelegramCore.instance)

    @mock.patch('core.telegram.Updater')
    def test_jerimum_initialize(self, mocked_updater):
        i1 = JerimumBot.instance()
        i2 = BotTelegramCore.instance()
        self.assertIs(i1, i2)
        self.assertIs(JerimumBot._instance, BotTelegramCore._instance)
