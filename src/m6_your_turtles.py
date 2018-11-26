"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Marcus Hughes-Oliver.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
jack = rg.SimpleTurtle('circle')
jack.speed = 20
size = 30
for k in range(15):
    jack.draw_circle(size)
    jack.pen_up()
    jack.forward(5)
    jack.right(90)
    jack.forward(5)
    jack.right(90)
    size = size - 2
    jack.pen_down()

tom = rg.SimpleTurtle('triangle')
tom.speed = 15
size1 = 200
for k in range(11):
    tom.draw_regular_polygon(3, size1)
    tom.pen_up()
    tom.right(30)
    tom.forward(10)
    size = size - 5
    tom.pen_down()
window.close_on_mouse_click()

