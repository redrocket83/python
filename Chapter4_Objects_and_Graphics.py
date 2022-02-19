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

    win.getMouse() # Pauses the window so you can see the target
    win.close()

main()
#
# Q3) Write a program which draws some sort of face
#
#Chapter 4 Exercise 3
#Write a program that draws some sort of face.
import graphics
from graphics import *

def main():
    #head
    win = GraphWin('Face',300,300)
    f = Oval(Point(75,50),Point(225,250))
    f.setFill('pink')
    f.draw(win)

    #eyes
    el = Circle(Point(120,120),15)
    el.setFill('white')
    el.draw(win)
    ebl = Circle(Point(120,120),5)
    ebl.setFill('black')
    ebl.draw(win)

    er = Circle(Point(180,120),15)
    er.setFill('white')
    er.draw(win)
    ebr = Circle(Point(180,120),5)
    ebr.setFill('black')
    ebr.draw(win)

    #mouth
    n = Oval(Point(110,185),Point(190,225))
    n.setFill('black')
    n.draw(win)

    #nose
    n = Oval(Point(125,110),Point(175,190))
    n.setFill('pink')
    n.draw(win)

    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q4) Write a program which draws a winter scene with a Christmas tree and snowman
#
Chapter 4 Exercise 4
#Write a program that draws a winter scene and some snowmen.
import graphics
from graphics import *

def main():
    #head
    win = GraphWin('winter',800,450)

    #background
    win.setBackground('darkgrey')

    #snow
    sn = Rectangle(Point(0,170), Point(800,450))
    sn.setFill('white')
    sn.draw(win)

    #trees
    tr = Polygon(Point(60,300), Point(120,50), Point(180,300))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(200,200), Point(230,70), Point(260,200))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(500,300), Point(550,40), Point(600,300))
    tr.setFill('green')
    tr.draw(win)

    tr = Polygon(Point(600,350), Point(670,50), Point(740,350))
    tr.setFill('green')
    tr.draw(win)

    #snowman
    s = Circle(Point(400,300),80)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(400,210),50)
    s.setFill('white')
    s.draw(win)

    s = Circle(Point(400,145),30)
    s.setFill('white')
    s.draw(win)

    #coal
    c = Circle(Point(390,140),5)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(410,140),5)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(386,158),4)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(400,163),4)
    c.setFill('black')
    c.draw(win)

    c = Circle(Point(414,158),4)
    c.setFill('black')
    c.draw(win)


    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q5) Write a program that draws 5 dice on the screen depicting a straight (1,2,3,4,5 or 2,3,4,5,6).
#
#Chapter 4 Exercise 5
#Write a program that draws 5 dice on the screen depicting a straight (1, 2, 3, 4, 5)
import graphics
from graphics import *

def main():
    win = GraphWin('dice',500,100)
    win.setCoords(0,0,5,1)

    for i in range(5):
        dice = Rectangle(Point(0.1+i,0.1),Point(0.9+i,0.9))
        dice.setFill('red')
        dice.draw(win)

    center = Point((0.5),(0.5))

    #dice1
    d1 = Circle(center,0.08)
    d1.setFill('white')
    d1.setOutline('white')
    d1.draw(win)

    #dice2
    d2a = d1.clone()
    d2a.draw(win)
    d2a.move(0.8,0.2)

    d2b = d1.clone()
    d2b.draw(win)
    d2b.move(1.2,-0.2)

    #dice3
    d3a = d1.clone()
    d3a.draw(win)
    d3a.move(2.0,0.0)

    d3b = d1.clone()
    d3b.draw(win)
    d3b.move(2.2,0.2)

    d3c = d1.clone()
    d3c.draw(win)
    d3c.move(1.8,-0.2)

    #dice4
    d4a = d1.clone()
    d4a.draw(win)
    d4a.move(2.8,-0.2)

    d4b = d1.clone()
    d4b.draw(win)
    d4b.move(2.8,0.2)

    d4c = d1.clone()
    d4c.draw(win)
    d4c.move(3.2,0.2)

    d4d = d1.clone()
    d4d.draw(win)
    d4d.move(3.2,-0.2)

    #dice5
    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.0,0.0)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,-0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(3.8,0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,0.2)

    d5e = d1.clone()
    d5e.draw(win)
    d5e.move(4.2,-0.2)

    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q6) Modify the graphical future value program so that the input (principal and APR) also are done in a graphical fashion using Entry objects.
#
#futval_graph.py
#Chapter 4 Exercise 6

from graphics import *

def main():
    
    #Introduction
    print("The program plots the growth of a 10-year investment")

    #Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75,-9000, 11.5,15400)

    #Principle input
    Text(Point(1.0, -4000), "Input starting principle").draw(win)
    inputprinciple = Entry(Point(3, -4000), 6)
    inputprinciple.setText("0")
    inputprinciple.draw(win)

    #Interest input
    Text(Point(6, -4000), "Input interest rate").draw(win)
    inputinterest = Entry(Point(8.2, -4000),6)
    inputinterest.setText("0")
    inputinterest.draw(win)

    #Create the Calculate button
    button = Rectangle(Point(2,-6000),Point(8,-8000))
    button.setFill("red")
    button.draw(win)
    buttontxt = Text(Point(5,-7200),"Calculate:")
    buttontxt.draw(win)
    win.getMouse()

    #Receive input
    p = eval(inputprinciple.getText())
    q = eval(inputinterest.getText())

    #labels
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
    Text(Point(4.0, 14000), "Future Values Calculator").draw(win)
         
    #Draw a bar for the initial principle
    bar = Rectangle(Point(0, 0), Point(1, p))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw bars for successive years
    for i in range(1,11):
        #calculate value for next year
        p = p * (1 + q)
        #Draw a bar for this value
        bar = Rectangle(Point(i, 0), Point(i+1, p))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    buttontxt.setText('Quit.')

    win.getMouse() # pause for click in window
    win.close()

main()
#
# Q7) Circle Intersection.
#     Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#     Input: Radius of the circle and the y-intercept of the line.
#     Output: Draw a circle centered at (0,0) with teh given radius in a window with coordinates running from -10,-10 to 10,10.
#     Draw a horizontal line across the window and the given-y intercept.
#     Draw the two points of intersection in red.
#     Print out the x values of the points of intersection.
#     Formula: x = + or -(sqrt((r^2 = y^2))
#
#Circle Intersection
#Program that computes the intersection of a circle

from graphics import *
from math import sqrt

def main():
    #Create the window and set co-ordinates
    win = GraphWin("Circle Intersection Calculator", 300, 330)
    win.setCoords(-10, -12, 10, 10)

    #Screen 1: Description
    descr = Text(Point(0,0), "Program to calculate x value intersections")
    click = Text(Point(0,-11), "Click anywhere to continue")
    descr.setSize(8)
    click.setSize(8)
    descr.draw(win)
    click.draw(win)

    #Wait for mouse click and then clear screen
    win.getMouse()
    descr.undraw()

    #Screen 2: Obtain input from user
    #Add entry box for radius and y intercept
    rad_text = Text(Point(-5,5), "Radius : ")
    int_text = Text(Point(-5,0), "Y Intercept")
    rad_text.setSize(8)
    int_text.setSize(8)
    rad_text.draw(win)
    int_text.draw(win)
    rad_input = Entry(Point(0,5), 3) # 3 being characters for input
    int_input = Entry(Point(0,0), 3)
    rad_input.setSize(8)
    int_input.setSize(8)
    rad_input.draw(win)
    int_input.draw(win)

    #Get the radius and intercept from the user and clear screen
    win.getMouse()
    radius = eval(rad_input.getText())
    intercept = eval(int_input.getText())
    rad_text.undraw()
    int_text.undraw()
    rad_input.undraw()
    int_input.undraw()
    click.undraw()

    #Compute the x values of intersection
    x_int1 = -sqrt(radius ** 2 - intercept ** 2)
    x_int2 = sqrt(radius ** 2 - intercept ** 2)

    #Screen 3: Displaying data
    # Draw circle and line on the x and y axis
    x_axis = Line(Point(-10,0), Point(10,0))
    x_axis.setArrow("last")
    y_axis = Line(Point(0,-10), Point(0,10))
    y_axis.setArrow("last")
    circ = Circle(Point(0,0), radius)
    circ.setOutline("blue")
    line = Line(Point(-10,intercept), Point(10, intercept))
    line.setOutline("blue")
    int1 = Circle(Point(x_int1, intercept), 0.2)
    int1.setFill("red")
    int1.setOutline("red")
    int2 = Circle(Point(x_int2, intercept), 0.2)
    int2.setFill("red")
    int2.setOutline("red")
    x_axis.draw(win)
    y_axis.draw(win)
    circ.draw(win)
    line.draw(win)
    int1.draw(win)
    int2.draw(win)

    #Dispay the data on screen
    int_info = Text(Point(0,-11), f" x points are {x_int1} + {x_int2}")
    int_info.setSize(8)
    int_info.draw(win)

    #Close the window by clicking the mouse
    win.getMouse()
    win.close()

main()
#
# Q8) Line Segment Information.
#     This program allows the suer to draw a line segment that then displays some graphical and textual information about the line segment.
#     Input: Two mouse clicks for the end points of the line segment.
#     Output: Draw the midpoint of the segment in cyan.
#             Draw the line.
#             Print the length and the slope of the line.
#     Formulas: dx = x2 - x1
#               dy = y2 - y1
#               slope = dy / dx
#               length = sqrt(dx^2 + dy^2)
#
#This program allows the user to draw a line segment and then displays some graphical and textual information about the line inpit
#https://github.com/drypycode/zelle-python/blob/master/chap04/exercise_8.py

from graphics import *
from math import * # You can also do import math

def main():
    win = GraphWin("Line drawing tool", 400, 400)
    win.setCoords(-10, -10, 10, 10)

    #Prompt the user for 2 mouse clicks
    message = Text(Point(0, 8), "Click on 2 points to create a line")
    message.setFill("blue")
    message.draw(win)

    #Store the co-ordinates in variables x1 and x2
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    print(x1)
    print(x2)
    print(y1)
    print(y2)

    #Create a line with midpoint as "cyan"
    line = Line(point1,point2)
    line.draw(win)
    mx = (x1+x2)/2
    my = (y1+y2)/2
    print(mx)
    print(my)
    win.plot(mx, my, "green")

    #Print the length and slope of the line
    dx = x2 - x1
    dy = y2 - y1
    slope = dy /dx
    print("The slope of the slope is: ", round(slope,2))
    message2 = Text(Point(0, -6), ("The slope of the line is: ", round(slope,2)))
    message2.draw(win)
    #Print the length of the line
    length = sqrt(dx**2 + dy**2)
    print("The length of the line is", round(length, 2))
    message3 = Text(Point(0, -3), ("The slope of the line is: ", round(slope,2)))
    message3.draw(win)
main()
#
# Q9) Rectangle Information.
#     This program displays information about a rectangle drawn by the user.
#     Input: Two mouse clicks for the opposite corners of a rectangle.
#     Output: Draw the rectangle.
#             Print the perimeter and area of the rectangle.
#     Formulas: area = (length)(width)
#               perimeter = 2(length + width)
#
#This program displays information about a triangle draw by the user

from graphics import *

def main():
    win = GraphWin("Drawing a rectangle", 400,400)
    win.setCoords(0, 0, 20, 20)

    #Store the co-ordinates of the 2 mouse clicks
    point1 = win.getMouse()
    point2 = win.getMouse()

    #Create a rectangle
    rectangle = Rectangle(point1, point2)
    rectangle.draw(win)
    win.getMouse() # pause for click in window

    #Get the length and height of the rectangle
    length = abs(point2.getX() - point1.getX())
    height = abs(point2.getY() - point1.getY())

    #Get the area of the triangle
    area = length * height

    #Get the perimeter of the rectangle
    perimeter = 2 * (length * height)

    #Print the area of the rectangle
    # 2 example of showing the strings in a message output
    #message1 = Text(Point(10,18), ("The area of the rectangle is : ", round(area,2)))
    message1 = Text(Point(10,18), f"The area of the rectangle is: {area:.2f}") # :.2f rounds value to 2 decimal places
    
    message1.draw(win)

    #Print the perimeter of the rectangle
    message2 = Text(Point(10,16), f"The perimeter of the rectangle is: {perimeter:.2f}") # :.2f rounds value to 2 decimal places
    message2.draw(win)

    win.getMouse() # pause for click in window

main()
#
# Q10)Triangle Information.
#     Same as the previous problem, but with three clicks for the vertices of the triangle.
#     Formulas: For perimeter, see length fromt he Line Segment problem.
#     area = sqrt(s(s - a)(s - b)(s - c)) where a, b, and c are the lengths of the sides and s = (a + b + c) / 2.
#
#This program displays information about a triangle draw by the user

from graphics import *

from math import *

def main():
    win = GraphWin("Drawing a Triangle", 400,400)
    win.setCoords(0, 0, 20, 20)

    #Prompt the user to click 3 times
    message =Text(Point(10,19), "Click 3 points to make a triangle")
    message.draw(win)

    #Store the co-ordinates of the 3 mouse clicks
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    x3 = point3.getX()
    y3 = point3.getY()

    #Create a triangle
    triangle = Polygon(point1,point2,point3)
    triangle.draw(win)

    #Calculate the lengths of the sides
    lengtha = sqrt((x2-x1)**2 + (y2-y1)**2)
    lengthb = sqrt((x3-x1)**2 + (y3-y1)**2)
    lengthc = sqrt((x3-x2)**2 + (y3-y2)**2)

    #Calculate the perimeter
    perimeter = lengtha + lengthb + lengthc

    #Calculate s for the area calculation
    # s = (a+b+c)/2
    s = perimeter /2

    #Calculate the area of the triangle
    #area = square root of (s * (s-lengtha)(s-lengthb)(s-lengthc)
    area = sqrt(s*(s-lengtha)*(s-lengthb)*(s-lengthc))

    #State the perimeter and area of the rectangle
    message2 = Text(Point(10,5), f" The area of the triangle is {area:.2f}")
    message2.draw(win)

    message3 = Text(Point(10,3), f" The perimeter of the triangle is {perimeter:.2f}")
    message3.draw(win)
    win.getMouse() # pause for click in window

main()
#
# Q11) Five-click House.
#     You are to write a program that allows the user to draw a simple house using five mouse clicks. The fisrt two clicks will be the opposite
#     corners of the rectangular frame of the house. The third click will indicate the center of the otp ege of a rectangular door. The door should
#     have a total width that is 1/5 the wdith of the house frame. The sides of the door should have extend from the corners of the top down to the
#     bottom of the frame. The fourth click will indicate the center of a square window. The window is half as wide as the door. The last click will
#     indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.
#
#This program draws a simple house using 5 mouse clicks

from graphics import *

from math import *

def main():
    
    win = GraphWin("Drawing a simple house in 5 mouse clicks", 400,400)
    win.setCoords(0, 0, 20, 20)

    #Store the co-ordinates of the 2 mouse clicks to create the rectangle house
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    y1 = point1.getY()
    x2 = point2.getX()
    y2 = point2.getY()

    #Create a rectangle
    rectangle = Rectangle(point1, point2)
    rectangle.draw(win)

    # For the third click, this will show the center of the top of the door
    point3 = win.getMouse()
    x3 = point3.getX()
    y3 = point3.getY()

    #Door width
    rectangle_width = x2 -x1
    door = Rectangle(Point(x3 - (1/5 * rectangle_width), y1), Point(x3 + (1/5 * rectangle_width),y3))
    door.draw(win)

    #For the fourth click, we will print a square window
    point4 = win.getMouse()
    x4 = point4.getX()
    y4 = point4.getY()
    #window is 1/2 width of the door
    window_width = 1/20 * rectangle_width
    window = Rectangle(Point((x4-window_width), (y4-window_width)), Point((x4+window_width), (y4+window_width)))
    window.draw(win)

    #For the fifth click
    point5 = win.getMouse()
    line1 = Line(point2, point5)
    line1.draw(win)
    line2 = Line(point5, Point(x1, y2))
    line2.draw(win)

    win.getMouse() # pause for click in window

main()
    
    

    
    



