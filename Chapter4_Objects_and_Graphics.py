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
#  Q1. Pick an example of an interesting real-world object and describe it as a programming object by listing its data (attributes, what it "knows") and its methods 
#     (behaviors, what it can "do").
#  A1. Objects are key to understanding object-oriented technology. You can look around you now and see many examples of real-world objects: your dog, your desk, your television
#      set, your bicycle. These real-world objects share two characteristics: They all have state and behavior. 
#      For example, dogs have state (name, color, breed, hungry) and behavior (barking, fetching, and wagging tail). 
#      Bicycles have state (current gear, current pedal cadence, two wheels, number of gears) and behavior (braking, accelerating, slowing down, changing gears).
#
#  Q2. Describe in your own words the object produced by each of the following operations from the graphics module. Be as precise as you can. Be sure to mention such things 
#      as the size, position, and appearance of the various objects. You may include a sketch if that helps.
#
#     a) Point(130, 130)
#        Constructs a point at x coordinate 130 and y coordinate 130, with 0,0 being located at upper left hand corner.
#
#     b) c = Circle(Point(30,40), 25)
#        c.setFill("blue")
#        c.setOutline("red")
#
#     c) r = Rectangle(Point(20,20), Point(40,40))
#        r.setFill(color_rgb(0,255,150)
#        r.setWidth(3)
#
#     d) l = Line(Point(100,100), Point(100,200))
#        l.setOutline("red4")
#        l.setArrow("first")

#     e) Oval(Point(50,50), Point(60,100))

#     f) shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
#        shape.setFill("orange")

#     g) t = Text(Point(100,100), "Hello World!")
#        t.setFace("courier")
#        t.setSize(16)
#        t.setStyle("italic")

#  3.  Describe what happens when the following interactive graphics program runs:

