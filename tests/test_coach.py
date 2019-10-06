from unittest import TestCase, mock

from commands.coach import coach


class CoachTest(TestCase):
    @mock.patch('commands.coach.random.randint')
    @mock.patch('commands.coach.requests.get')
    @mock.patch('commands.coach.BeautifulSoup')
    @mock.patch('commands.coach.re')
    def test_randint_returning_max_value(
            self, mocked_re, mocked_bsp, mocked_get, mocked_randint):
        self.assertIsInstance(mocked_re, mock.MagicMock)
        self.assertIsInstance(mocked_bsp, mock.MagicMock)
        self.assertIsInstance(mocked_get, mock.MagicMock)
        self.assertIsInstance(mocked_randint, mock.MagicMock)

        mocked_randint.side_effect = lambda x, y: y
        mocked_bsp.find_all = mock.MagicMock(
            return_value=[
                mock.MagicMock(
                    get_text=mock.MagicMock(return_value='quote 1')),
                mock.MagicMock(
                    get_text=mock.MagicMock(return_value='quote 2'))
            ]
        )
        coach(mock.MagicMock(), mock.MagicMock(), mock.MagicMock())
