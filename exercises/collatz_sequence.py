"""Exercise #39: Collatz Sequence

Write a function named `collatz()` with a `startingNumber` parameter.
The function returns a list of integers of the Collatz sequence that
`startingNumber` produces. The first integer in this list must be
`startingNumber` and the last integer must be `1`.

Your function should check if `startingNumber` is an integer less than `1`,
and in that case, return an empty list.
"""

from __future__ import annotations


def collatz(startingNumber: int) -> list[int]:
    """Return Collatz sequence starting with `startingNumber`.
    
    If `startingNumber` is less than 1 return empty list.
    """
    return []
