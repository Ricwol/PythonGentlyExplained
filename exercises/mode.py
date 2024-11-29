"""Exercise #16: Mode

Write a `mode()` function that has a `numbers` parameter. 
This function returns the mode, or most frequently appearing number, of
the list of integer and floating-point numbers passed to the function.

Passing an empty list to `mode()` should cause it to return `None`.
"""

from __future__ import annotations

from typing import Optional


def mode(numbers: list[float]) -> Optional[float]:
    """Return the mode of `numbers`.
    
    Return `None` if `numbers` is empty.
    """
