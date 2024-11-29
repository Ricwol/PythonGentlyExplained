"""Exercise #15: Median

Write a `median()` function that has a `numbers` parameter.
This function returns the statistical median of the `numbers` list.
The median of an odd-length list is the number in the middlemost number
when the list is in sorted order. If the list has an even length, the
median is the average of the two middlemost numbers when the list is in
sorted order. 

Passing an empty list to `median()` should cause it to return `None`.

Feel free to use Python's built-in `sorted()` method to sort the
`numbers` list.
"""

from __future__ import annotations

from typing import Optional


def median(numbers: list[float]) -> Optional[float]:
    """Calculate and return the median.
    
    Return `None` if `numbers` is empty.
    """
