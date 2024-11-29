"""Exercise #14: Average

Write an `average()` function that has a `numbers` parameter.
This function returns the statistical average of the list of integer
and floating-point numbers passed to the function.

Passing an empty list to `average()` should cause it to return `None`.

While Python's built-in `sum()` function can help you solve this
exercise, try writing the solution without using it.
"""

from __future__ import annotations

from typing import Optional


def average(numbers: list[float]) -> Optional[float]:
    """Calculate and return the average of `numbers`.
    
    Return `None` if `numbers` is empty.
    """
