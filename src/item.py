"""
This module defines the XMLItem class for parsing XML item elements.
"""
import xml.etree.ElementTree as ET


class XMLItem:
    """
    A class used to represent an XML Item and its elements.
    """
    item_elements = ['title', 'author', 'pubDate', 'link', 'category', 'description']

    @classmethod
    def get_items_xml(cls, channel: ET, limit: int) -> dict:
        """
        Parses XML items into a dictionary.
        """
        items = channel.findall('item')

        if limit is None or limit > len(items):
            limit = len(items)

        items_list = [
            {el: item.find(el).text for el in cls.item_elements if item.find(el) is not None}
            for item in items[:limit]
        ]
        if 0 >= len(items_list):
            return {}
        return {"items": items_list}
