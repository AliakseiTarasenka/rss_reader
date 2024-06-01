"""
This module defines the XMLChannel class for parsing XML channel elements.
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
