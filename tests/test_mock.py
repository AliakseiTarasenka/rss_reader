from unittest import mock, TestCase
from src.rss_reader import rss_parser


def function_rss_parser():
    xml = ('<rss><channel><title>Some RSS Channel</title><link>'
           'https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>')
    rss_parser(xml)
    print("calling rss_parser function")


class TestParserMock(TestCase):

    @mock.patch("rss_parser")
    def test_rss_parser(self, mock_object):
        self.assertFalse(mock_object.called)
        function_rss_parser()
        self.assertTrue(mock_object.called)
