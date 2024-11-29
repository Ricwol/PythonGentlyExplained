"""Exercise #38: Random Shuffle

Write a `shuffle()` function with a `values` parameter set to a list
of values. The function doesn't return anything, but rather it sets
each value in the list to a random index. 

The resulting shuffled list must contain the same values as before
but in random order.

This exercise asks you to implement a function identical to Python's
`random.shuffle()` function. As such, avoid using this function in
your solution as it'd defeat the purpose of the exercise.
"""

from __future__ import annotations

from random import randint
from typing import Any


def shuffle(values: list[Any]) -> None:
    """Shuffle `values` to create a random order."""
