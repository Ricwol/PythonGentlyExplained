"""Exercise #29: Pyramid Drawing

Write a `drawPyramid()` function with a `height` parameter. The top of
the pyramid has one centered hashtag character, and the subsequent rows
have two more hashtags than the previous row. The number of rows
matches the `height` integer. 

There are no Python assert statements to check the correctness of your
program. Instead, you can visually inspect the output yourself. For example,
calling `drawPyramid(8)` would output the following:

       #
      ###
     #####
    #######
   #########
  ###########
 #############
###############
"""

def drawPyramid(height: int) -> None:
    """Draw a pyramid of `height` with '#'."""
