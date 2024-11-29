"""Exercise #12: Smallest & Biggest

Write a `getSmallest()` function that has a `numbers` parameter.
The `numbers` parameter will be a list of integer and floating-point
number values. The function returns the smallest value in the list.
If the list is empty, the function should return `None`.

Since this function replicates Python's `min()` function, your solution
shouldn't use it.
"""

from __future__ import annotations

from typing import Optional


def getSmallest(numbers: list[float]) -> Optional[float]:
    """Find and return the smallest number, otherwise return None."""
