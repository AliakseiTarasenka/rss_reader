"""
This module defines models for parsing XML channel and item elements.
"""
import xml.etree.ElementTree as ET


class XMLChannel:
    """
    A class used to represent an XML Channel and its elements.
    """
    channel_elements = ['title', 'link', 'lastBuildDate', 'pubDate',
                        'language', 'category', 'managingEditor', 'description']

    @classmethod
    def get_channel_xml(cls, channel: ET) -> dict:
        """
        Parses an XML channel into a dictionary.
        """
        channel_dict = {}
        for el in cls.channel_elements:
            element = channel.find(el)
            if element is not None:
                if element.tag == 'title':
                    channel_dict["feed"] = element.text
                else:
                    channel_dict[el] = element.text
        return channel_dict


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
