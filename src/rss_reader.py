# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import json as jsonlib
import xml.etree.ElementTree as ET
import requests
from channel import XMLChannel
from item import XMLItem


class UnhandledException(Exception):
    pass


def get_list_of_strings(json_data) -> List[str]:
    str_list = []
    for item in json_data:
        for key, value in item.items():
            str_list.append(f"{key}: {value}")
    return str_list


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
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xml)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    root = ET.fromstring(xml)

    channel = root.find('channel')
    if channel is None:
        return []
    XMLChannel.get_channel_xml(channel)
    XMLItem.get_items_xml(channel, limit)

    result = {**XMLChannel.get_channel_xml(channel), **XMLItem.get_items_xml(channel, limit)}

    if json:
        return [jsonlib.dumps(result, indent=2)]
    else:
        return get_list_of_strings([result])


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
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
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
