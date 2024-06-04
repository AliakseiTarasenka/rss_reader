"""
This module defines a command-line RSS reader.
"""

from argparse import ArgumentParser
from typing import List, Optional, Sequence
import json as jsonlib
import xml.etree.ElementTree as ET
import requests
from src.models import XMLItem, XMLChannel
from src.utils import get_list_of_strings


class UnhandledException(Exception):
    """
    Exception raised for errors that are not handled.
    """


def rss_parser(
        xml: str,
        limit: Optional[int] = None,
        json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ['feed: Some RSS Channel', 'link: https://some.rss.com', 'description: Some RSS Channel']
        >>> print("\\n".join(rss_parser(xml)))
        feed: Some RSS Channel
        link: https://some.rss.com
        description: Some RSS Channel
    """
    root = ET.fromstring(xml)

    channel = root.find('channel')
    if channel is None:
        print("The XML does not contain a 'channel' element.")
        return []

    channel_xml = XMLChannel.get_channel_xml(channel)
    items_xml = XMLItem.get_items_xml(channel, limit)
    result = {**channel_xml, **items_xml}

    if json:
        return [jsonlib.dumps(result, indent=2)]
    return get_list_of_strings([result])


def main(argv: Optional[Sequence] = None):
    """
    The main function with CLI arguments source, --json and --limit
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException from e


if __name__ == "__main__":
    main()
