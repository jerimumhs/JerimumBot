from unittest import TestCase


# noinspection PyUnresolvedReferences
class BS4Test(TestCase):
    def test_import_bs4(self):
        import bs4  # noqa F401

    def test_import_telegram(self):
        import telegram  # noqa F401

    def test_import_requests(self):
        import requests  # noqa F401

    def test_import_pyowm(self):
        import pyowm  # noqa F401
