"""
This module defines utility functions.
"""

from typing import List


def get_list_of_strings(json_data) -> List[str]:
    """
    Converts a list of dictionaries into a list of strings.
    """
    str_list = []
    for item in json_data:
        for key, value in item.items():
            str_list.append(f"{key}: {value}")
    return str_list
