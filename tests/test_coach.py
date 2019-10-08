from unittest import TestCase, mock

from commands.coach import coach
from core.throttling import ThrottleDecorator


class CoachTest(TestCase):

    def tearDown(self):
        ThrottleDecorator._last_run = 0

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
        mocked_bsp.return_value = mock.MagicMock(
            find_all=mock.MagicMock(
                return_value=[
                    mock.MagicMock(
                        get_text=mock.MagicMock(return_value='quote 1')),
                    mock.MagicMock(
                        get_text=mock.MagicMock(return_value='quote 2'))
                ]
            )
        )
        coach(mock.MagicMock(), mock.MagicMock(), mock.MagicMock())

    @mock.patch('commands.coach.requests.get')
    @mock.patch('commands.coach.BeautifulSoup')
    @mock.patch('commands.coach.re')
    def test_total_pages_less_than_20(
            self, mocked_re, mocked_bsp, mocked_get):
        self.assertIsInstance(mocked_re, mock.MagicMock)
        self.assertIsInstance(mocked_bsp, mock.MagicMock)
        self.assertIsInstance(mocked_get, mock.MagicMock)

        mocked_re.search = mock.MagicMock(
            return_value=mock.MagicMock(
                group=mock.MagicMock(
                    return_value=13
                )
            )
        )
        mocked_bsp.return_value = mock.MagicMock(
            find_all=mock.MagicMock(
                return_value=[
                    mock.MagicMock(
                        get_text=mock.MagicMock(return_value='quote 1')),
                    mock.MagicMock(
                        get_text=mock.MagicMock(return_value='quote 2'))
                ]
            )
        )
        coach(mock.MagicMock(), mock.MagicMock(), mock.MagicMock())
