"""Exercise #13: Sum & Product

Write two functions named `calculateSum()` and `calculateProduct()`.

They both have a parameter named `numbers`, which will be a list of
integer or floating-point values. 

The `calculateSum()` function adds these numbers and returns the sum.
If the list passed to `calculateSum()` is empty, the function returns
`0`.

The `calculateProduct()` function multiplies these numbers and returns
the product. If the list passed to `calculateProduct()` is empty, the
function returns `1`.

Since this function replicates Python's `sum()` function, your solution
shouldn't call.
"""

from __future__ import annotations


def calculateSum(numbers: list[float]) -> float:
    """Calculate and return the sum of `numbers`.
    
    Return 0 if `numbers` is empty.
    """
    return 0


def calculateProduct(numbers: list[float]) -> float:
    """Calculate and return the product of the given numbers.
    
    Return 1 if `numbers` is empty.
    """
    return 1
