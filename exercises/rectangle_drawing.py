"""Exercise #27: Rectangle Drawing

Write a `drawRectangle()` function with parameters `width` and `height`.
The function doesn't return any values but rather prints a rectangle with
the given number of hashtags in the horizontal and vertical directions.
If either the `width` or `height` parameter is `0` or a negative number,
the function should print nothing.

There are no Python assert statements to check the correctness of your
program. Instead, you can visually inspect the output yourself. For example,
calling `drawRectangle(10, 4)` should produce the following output:

##########
##########
##########
##########
"""

def drawRectangle(width: int, height: int) -> None:
    """Draw a rectangle of `width` and `height` using '#'.
    
    If `width` or `height` is less than or equal to 0 draw nothing.
    """
