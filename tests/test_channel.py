# import unittest to use its   functionality.
import unittest
import xml.etree.ElementTree as ET
from rss_reader.channel import XMLChannel


class TestXMLChannel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # is executed once cest case starts.
        print('Test Case "TestXMLChannel" has started.')

    @classmethod
    def tearDownClass(cls):
        # is executed once Test Case finishes.
        print('Test Case "TestXMLChannel" has finished.')

    def test_get_channel_xml(self):
        xml_string = """<channel>
                            <title>Test Channel</title>
                            <link>http://example.com</link>
                            <lastBuildDate>Mon, 20 Sep 2021 10:37:00 GMT</lastBuildDate>
                            <pubDate>Mon, 20 Sep 2021 10:37:00 GMT</pubDate>
                            <language>en-us</language>
                            <category>Test</category>
                            <managingEditor>Editor</managingEditor>
                            <description>This is a test channel</description>
                        </channel>"""
        xml_element = ET.fromstring(xml_string)
        expected_result = {
            'feed': 'Test Channel',
            'link': 'http://example.com',
            'lastBuildDate': 'Mon, 20 Sep 2021 10:37:00 GMT',
            'pubDate': 'Mon, 20 Sep 2021 10:37:00 GMT',
            'language': 'en-us',
            'category': 'Test',
            'managingEditor': 'Editor',
            'description': 'This is a test channel'
        }

        result = XMLChannel.get_channel_xml(xml_element)
        self.assertDictEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
