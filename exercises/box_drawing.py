"""Exercise #30: 3D Box Drawing

Write a `drawBox()` function with a `size` parameter. The `size`
parameter contains an integer for the width, length, and height of the box.
The horizontal lines are drawn with `-` dash characters, the vertical
lines with `|` pipe characters, and the diagonal lines with `/` forward
slash characters. The corners of the box are drawn with `+` plus signs.

There are no Python assert statements to check the correctness of your program.
Instead, you can visually inspect the output yourself.
For example, calling `drawBox(1)` through `drawBox(5)` would output the
following boxes, respectively:

                                                        +----------+
                                                       /          /|
                                      +--------+      /          / |
                                     /        /|     /          /  |
                       +------+     /        / |    /          /   |
                      /      /|    /        /  |   /          /    |
           +----+    /      / |   /        /   |  +----------+     +
          /    /|   /      /  |  +--------+    +  |          |    /
  +--+   /    / |  +------+   +  |        |   /   |          |   / 
 /  /|  +----+  +  |      |  /   |        |  /    |          |  /  
+--+ +  |    | /   |      | /    |        | /     |          | /   
|  |/   |    |/    |      |/     |        |/      |          |/    
+--+    +----+     +------+      +--------+       +----------+

Size 1  Size 2      Size 3         Size 4            Size 5

If the argument for size is less than 1, the function prints nothing.
"""

def drawBox(size: int) -> None:
    """Draw a 3D box of `size`.
    
    If `size` is less than 1 draw nothing.
    """
