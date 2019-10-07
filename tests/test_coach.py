from unittest import TestCase, mock

from commands.coach import coach


class CoachTest(TestCase):
    @mock.patch('commands.coach.last_call', None)
    @mock.patch('commands.coach.random.randint')
    @mock.patch('commands.coach.requests.get')
    @mock.patch('commands.coach.BeautifulSoup')
    @mock.patch('commands.coach.re')
    def test_randint_returning_max_value(
            self, mocked_re, mocked_bsp, mocked_get, mocked_randint, mocked_last_call=None):
        self.assertIsNone(mocked_last_call)
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

    @mock.patch('commands.coach.last_call', None)
    @mock.patch('commands.coach.requests.get')
    @mock.patch('commands.coach.BeautifulSoup')
    @mock.patch('commands.coach.re')
    def test_total_pages_less_than_20(
            self, mocked_re, mocked_bsp, mocked_get, mocked_last_call=None):
        self.assertIsNone(mocked_last_call)
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
        mocked_bsp.find_all = mock.MagicMock(
            return_value=[
                mock.MagicMock(
                    get_text=mock.MagicMock(return_value='quote 1')),
                mock.MagicMock(
                    get_text=mock.MagicMock(return_value='quote 2'))
            ]
        )
        coach(mock.MagicMock(), mock.MagicMock(), mock.MagicMock())
