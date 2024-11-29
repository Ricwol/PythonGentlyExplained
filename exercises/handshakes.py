"""Exercise #26: Handshakes

Write a function named `printHandshakes()` with a list parameter named
`people` which will be a list of strings of people's names. The function
prints out `'X shakes hands with Y'`, where X and Y are every possible
pair of handshakes between the people in the list. No duplicates are permitted:
    if "Alice shakes hands with Bob" appears in the output, then
    "Bob shakes hands with Alice" should not appear.

For example, 'printHandshakes(['Alice', 'Bob', 'Carol', 'David'])' should print:

Alice shakes hands with Bob
Alice shakes hands with Carol
Alice shakes hands with David
Bob shakes hands with Carol
Bob shakes hands with David
Carol shakes hands with David

The `printHandshakes()` function must also return an integer of the
number of handshakes.
"""

from __future__ import annotations

def printHandshakes(people: list[str]) -> int:
    """Return the total number of handshakes."""
    return 0
