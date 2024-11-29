"""Exercise #28: Border Drawing

Write a `drawBorder()` function with parameters `width` and `height`.
The function draws the border of a rectangle with the given integer sizes.
The interior of the rectangle requires printing spaces. The sizes given
include the space required for the corners. If the `width` or `height`
parameter is less than 2, the function should print nothing.

There are no Python assert statements to check the correctness of your program.
Instead, you can visually inspect the output yourself.

For example, calling 'drawBorder(16, 4)' would output the following:

+--------------+
|              |
|              |
+--------------+
"""

def drawBorder(width: int, height: int) -> None:
    """Draw a border of `width` and `height`.
    
    If `width` or `height` is less than 2 draw nothing.
    """
