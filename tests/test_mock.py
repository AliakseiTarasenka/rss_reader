"""
This module contains unit tests for the rss_parser function with mocking.
"""
from unittest import mock, TestCase


def function_rss_parser(func):
    """
    Function that calls the rss_parser function with a specific XML string.
    """
    xml = ('<rss><channel><title>Some RSS Channel</title><link>'
           'https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>')
    func(xml)
    print("calling rss_parser function")


class TestParserMock(TestCase):
    """
    Unit tests for the rss_parser function with mocking.
    """

    @mock.patch("src.rss_reader.rss_parser")
    def test_rss_parser(self, mock_object):
        """
        Test if rss_parser is called when function_rss_parser is called.
        """
        self.assertFalse(mock_object.called)
        function_rss_parser(mock_object)
        self.assertTrue(mock_object.called)
