# "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
# Chapter 4: Objects and Graphics
# End-of-Chapter Exercises

# Review Questions

#  1. Using graphics.py allows graphics to be drawn in a Python shell window. FALSE
#     Reference Page 86: "The GraphWin() function creates a new window on the screen. graphics.py is a module which is imported 

#  2. Traditionally, the upper-left corner of a graphics window has coordinates (0,0). TRUE
#     Reference Page 88: "Traditionally, graphics programmers locate the point (0,0) in the upper-left corner of the window,"

#  3. A single point on a graphics screen is called a pixel. TRUE
#     Reference Page 88: "A graphics winow is actually a collection of tiny points called pixels (short for 'picture elements')."

#  4. A function that creates a new instance of a class is called an accessor. FALSE
#     Reference Page 91: "To create a new instance of a class, we use a special operation called a constructor. A call to a constructor is an expression that creates a brand 
#     new object."
#     Reference Page 92: An accessor allows us to access information from the instance variables of the object.

#  5. Instance variables are used to store data inside an object. TRUE
#     Reference Page 92: Values are stored inside an object as instance variables.]

#  6. The statement myShape.move(10,20) moves myShape to the point (10,20). FALSE
#     Reference Page 93: All of the graphical objects have a move method specification move(dx, dy): Moves the object dx units in the x direction and dy units in the y direction.

#  7. Aliasing occurs when two variables refer to the same object. TRUE
#     Reference Page 95: "This situation where two vairabiles refer to the same object is called aliasing."

#  8. The copy method is provided to make a copy of a graphics object. FALSE
#     Reference Page 95: "The graphics library provides a better solution to copies or aliases; all graphical objects support a clone method that makes a copy of the object."

#  9. A graphics window always has the title "Graphics Window." FALSE
#     Reference Page 98: The GraphWin constructor allows an optional parameter to specify the title of the window
#     Reference Page 113. GraphWin(title, width, height)

# 10. The method in the graphics library used to get a mouse click is readMouse. FALSE
#     Reference Page 107: "When getMouse is invoked on a GraphWin, the program pauses and waits for the user to click the mouse somewhere in the graphics window."
#
# Multiple Choice
#
#  1. A method that returns the value of an objects instance variable is called a(n) [D]
#     a) mutator     
#     b) function
#     c) constructor
#     d) accessor *

#  2. A method that changes the state of an object is called a(n) [B]
#     a) stator
#     b) mutator *
#     c) constructor
#     d) changor

#  3. What graphics class would be best for drawing a square? [D]
#     a) Square
#     b) Polygon 
#     c) Line     
#     d) Rectangle *

#  4. What command would set the coordinates of win to go from (0,0) in the lower-left corner to (10,10) in the upper-right? [C]
#     a) win.setcoords(Point(0,0),Point(10,10)
#     b) win.setcoords((0,0),(10,10))
#     c) win.setCoords(0,0, 10,10) *       
#     d) win.setcoords(Point(10,10),Point(0,0))
#
#  5. What expression would create a line from (2,3) to (4,5)? [D]
#     a) Line(2, 3, 4, 5)
#     b) Line((2, 3), (4, 5))
#     c) line(2, 4, 3, 5)
#     d) Line(Point(2,3), Point(4,5)) * Page 90 for example
#
#  6. What command would be used to draw the graphics object shape into the graphics window win? [D]
#     a) win.draw(shape)
#     b) win.show(shape)
#     c) shape.draw()
#     d) shape.draw(win) * Pge 115 for ref

#  7. Which of the following computes the horizontal distance between points p1 and p2? [D]
#     a) abs(p1-p2)
#     b) p2.getX() - p1.getX()
#     c) abs(p1.getY() - p2.getY())
#     d) abs(p1.getX() - p2.getX()) *

#  8. What kind of ojbect can be used to get text input in a graphics window? [B]
#     a) Text
#     b) Entry *
#     c) Input
#     d) Keyboard

#  9. A user interface organized around visual elements and user actions is called a(n) [A]
#     a) GUI *
#     b) Application
#     c) Windower
#     d) API

# 10. What color is color_rgb(0,255,255)? [B] red green blue
#     a) Yello
#     b) Cyan * Page 121
#     c) Magenta
#     d) Orange
#
# Discussion
#
# Q1. Pick an example of an interesting real-world object and describe it as a programming object by listing its data (attributes, what it "knows") and its methods 
#     (behaviors, what it can "do").
# A1. Objects are key to understanding object-oriented technology. You can look around you now and see many examples of real-world objects: your dog, your desk, your television
#     set, your bicycle. These real-world objects share two characteristics: They all have state and behavior. 
#     For example, dogs have state (name, color, breed, hungry) and behavior (barking, fetching, and wagging tail). 
#     Bicycles have state (current gear, current pedal cadence, two wheels, number of gears) and behavior (braking, accelerating, slowing down, changing gears).
#
# Q2. Describe in your own words the object produced by each of the following operations from the graphics module. Be as precise as you can. Be sure to mention such things 
#     as the size, position, and appearance of the various objects. You may include a sketch if that helps.
#
# Q2a) Point(130, 130)

# A2a) Constructs a point at x coordinate 130 and y coordinate 130, with 0,0 being located at upper left hand corner. Page 88
#
# Q2b) c = Circle(Point(30,40), 25)
#          c.setFill("blue")
#          c.setOutline("red")
#
# A2b) A blue circle with a red outline centered at (30,40) with a radius of 25
#
# Q2c) r = Rectangle(Point(20,20), Point(40,40))
#          r.setFill(color_rgb(0,255,150)
#          r.setWidth(3)
#
# A2c) A square 20 units on each side centered. The fill colouris greenish blue and the outline is 3 pixels wide and black.
#
# Q2d) l = Line(Point(100,100), Point(100,200))
#          l.setOutline("red4")
#          l.setArrow("first")
#
# A2d) A vertical dark red line of length 100, with its bottom at point (100,200) and an arrow pointing up at the upper end.
#
# Q2e) Oval(Point(50,50), Point(60,100))
#
# A2e) An unfilled vertical oval
#
# Q2f) shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
#      shape.setFill("orange")
#
# A2f) An orange something! My program did not work well with this!
#
# Q2g) t = Text(Point(100,100), "Hello World!")
#          t.setFace("courier")
#          t.setSize(16)
#          t.setStyle("italic")
#          t.draw(win)
#
# A2g) The words "Hello World!" centered at (100,100), displayed in an italic size 16 courier font/
#
#  Q3.  Describe what happens when the following interactive graphics program runs:
#
       from graphics import *

       def main():                          # Defines the function named main() which contains the program
           win = GraphWin()                 # Creates a GraphWin object with "Graphics Window" default title and default size 200 x 200 pixels
           shape = Circle(Point(50,50), 20) # Constructs a circle object with the center at 50,50 and radius of 20 pixels
           shape.setOutline("red")          # Calls setOutline method of circle object named shape, seting its outline to the color red
           shape.setFill("red")             # Calls setFill method of circle object shape, it fills itself with the color red
           shape.draw(win)                  # Calls draw method of circle object named shape, it draws itself in graphics window object named win
           for i in range(10):              # Creates a counted loop that will iterate 10 times
               p = win.getMouse()           # Calls getMouse() method of graphics window object win, pauses program for user to click in win, returns mouse click as Point object,
                                            # which is assigned to the variable p (an event object)
               c = shape.getCenter()        # Calls getCenter() method of circle object shape, returns a clone of the center point of shape
               dx = p.getX() - c.getX()     # Assignment statement whereby variable dx is assigned the expression in the getX() methods of p and c are used to calculate the
                                            # difference along the x axis of the user's mouse click with respect to the center point of shape
               dy = p.getY() - c.get&()     # Assignment statement whereby variable dy is assigned a similar expression as dx, except this time it is for the Y axis
               shape.move(dx, dy)           # Calls the move() method of shape to move shape by the x distance referred to by dx and the y distance referred to by dy, thus
                                            # Moves the red circle shape moving its center point to the new coordinates encapsulated in the event object p
          win.close()                       # Calls the close() method of the Graphics Window variable win, closing the graphics window after the loop is finished.
                                            # Note that it will not be possible to see the final location of the circle. To do so, comment out win.close() or call on win's
                                            # getMouse() method to make win close after a mouse click.
       main()                               # Calls the function named main() to run the program

# Programming Exercises
#
# Q1a) Alter the previous program to draw squares rather than circles
#
# Programming Exercises
# Constructs a rectangle - Rectangle(point1), point2) having opposite corners at Point1 and Point2
import graphics
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    win.close
main()
#
# Q1b) Have each successive click draw an additional square on the screen (rather than moving the existing one).
#
# Programming Exercises
# Constructs a rectangle - Rectangle(point1), point2) having opposite corners at Point1 and Point2
import graphics
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(40,40), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    win.getMouse()
    win.close()

main()
#
# Q1c Print a message on the window "Click again to quit" after the loop, and wait for a final click before closing the window. Insert immediately before win.close():
#
# Programming Exercises
# Constructs a rectangle - Rectangle(point1), point2) having opposite corners at Point1 and Point2
import graphics
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(40,40), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape = shape.clone()
        shape.move(dx,dy)
        shape.draw(win)
    Text(Point(100,180), "Click again to quit.").draw(win)
    win.getMouse()
    win.close()

main()
#
# Q2) An archery target consists of a central circle of yellow surrounded by concentric rings of red, bue, black and white. Each ring has the same width, which is the same as 
#     the radius of the yellow circle. Write a program that draws such a target.
#     Hint: Objects drawn later will appear on top of objects drawn earlier
#
# Archery target
import graphics
from graphics import *

def main():
    win = GraphWin("Archery Target", 300,300)
    center = Point(150,150)
                   
    whitecircle = Circle(center, 100)
    whitecircle.setFill("white")
    whitecircle.draw(win)

    blackcircle = Circle(center, 80)
    blackcircle.setFill("black")
    blackcircle.draw(win)

    bluecircle = Circle(center, 60)
    bluecircle.setFill("blue")
    bluecircle.draw(win)

    redcircle = Circle(center, 40)
    redcircle.setFill("red")
    redcircle.draw(win)

    yellowcircle = Circle(center, 20)
    yellowcircle.setFill("yellow")
    yellowcircle.draw(win)

    win.getMouse() # pause for click in window
    win.close()

main(
