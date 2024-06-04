"""
This module contains unit tests for the XMLItem class.
"""
import unittest
import xml.etree.ElementTree as ET
from src.models import XMLItem


class TestXMLItem(unittest.TestCase):
    """
    Unit tests for the XMLItem class.
    """

    def setUp(self):
        # is executed before every test in Test Case.
        print(f'Check {self._testMethodName} has started.')

    def tearDown(self):
        # is executed after every test in Test Case.
        # tearDown() and tearDownClass() methods
        # will only be called if the setUp() and setUpClass() succeed
        print(f'Check {self._testMethodName} has finished.')

    def test_get_items_xml(self):
        """
        Test if get_items_xml method correctly parses an XML items into a set of dictionaries.
        """
        xml_string = """<channel>
                            <item>
                                <title>Test Item 1</title>
                                <author>Author 1</author>
                                <pubDate>Tue, 21 Sep 2021 14:37:00 GMT</pubDate>
                                <link>http://example.com/1</link>
                                <category>Category 1</category>
                                <description>This is a test item 1</description>
                            </item>
                            <item>
                                <title>Test Item 2</title>
                                <author>Author 2</author>
                                <pubDate>Tue, 21 Sep 2021 15:37:00 GMT</pubDate>
                                <link>http://example.com/2</link>
                                <category>Category 2</category>
                                <description>This is a test item 2</description>
                            </item>
                        </channel>"""
        xml_element = ET.fromstring(xml_string)
        expected_result = {"items": [
            {
                'title': 'Test Item 1',
                'author': 'Author 1',
                'pubDate': 'Tue, 21 Sep 2021 14:37:00 GMT',
                'link': 'http://example.com/1',
                'category': 'Category 1',
                'description': 'This is a test item 1'
            },
            {
                'title': 'Test Item 2',
                'author': 'Author 2',
                'pubDate': 'Tue, 21 Sep 2021 15:37:00 GMT',
                'link': 'http://example.com/2',
                'category': 'Category 2',
                'description': 'This is a test item 2'
            }
        ]}

        result = XMLItem.get_items_xml(xml_element, 2)
        self.assertDictEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
