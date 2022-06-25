# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 6: Defining Functions
# End-of-Chapter Exercises

# Review Questions

# True/False

# 1. Programmer srarely define their own functions = False
# 2. A function can only be called at once place in a program = False
# 3. Information can be passed into a function through parameters = True
# 4. Every Python function returns some value = True (None is returned when no explicit value is provided)
# 5. In Python, some parameters are passed by reference = False. Page 195. Technically Python passes all parameters by value
# 6. In Python a function can return only one value = False. Page 203
# 7. Python functions can never modify a parameter = False. Page 193/198/199. Parameters are always passed by value. However if the actual parameter is a variable whose 
#    object is a mutable object like a list, then changes to the object will be visible to the other program.
# 8. One reason to use functions is to reduce code duplication = True.
# 9. Variables defined in a function are local to that function = True. Page 203. Formal parameters and other variables inside fucntion definitions are local to that 
#    function
# 10. It's a bad idea to define new functions if it makes a program longer = False. Although some programs look longer it makes it much easier for experienced programmers
#     to understand

# Multiple Choice

# 1. The part of a program which uses a function is 
# 
# a) User
# b) Caller *
# c) Callee
# d) Statement

# 2. A python function definition begins with
#
# a) def *
# b) define
# c) function
# d) defun

# 3. A function can sent output back to the program with a(n)
# a) return *
# b) print
# c) assignment
# d) SASE

# 4. Formal and actual parameters are matched up by 
# a) name
# b) position *
# c) ID
# d) interests

# 5. Which os the following is NOT a step in the function calling process
# a) The calling program suspends
# b) The formal parameters are assigned the value of the actual parameters
# c) The body of the function executes
# d) Control returns to the point just before the fucntion was called *

# 6. In Python actual parameters are passed to functions
# a) by value *
# b) by reference
# c) at random
# d) by networking

# 7. Which is the following is not a reason to use functions
# a) to reduce code deuplication
# b) to make a program more modular
# c) to make a program more self documenting
# d) to demonstrate intellectual superiority *

# 8. If a function returns a value, it should generally be called from
# a) an expression *
# b) a different program
# c) main
# d) a cell phone

# 9. A function with a no return statement returns
# a) nothing
# b) its parameters
# c) its variables
# d) None

# Discussion Questions

# Q1. In your own words, describe two motivations for defining functions in your programs

# A1. Functions are useful for reducing duplicate code within a script. Using functions can make a script more modular making it easier to read and manipulate

# Q2. We have been thinking about computer programs as sequences of instructions where the computer methodically executes one instruction and then moves on to the next
#     one. Do programs that contain functions fit this model.

# A2. In a sense a script always travels downwards, it just uses references to functions listed as it moves through the scripts so it may look like it is going backwards 
#     and forwards but in fact, it is just referring to a pre created command. A bit like a journey where you keep going forwards, you just refer to the map every now 
#     and again

# Q3a. Parameters are an important concept in defining functions. What is the purpose of parameters?
 
# A3a. The only way for a function to see a variable from another function is for the variable to be passed as a parameter

# Q3b. What is the difference between a formal parameter and an actual parameter?

# A3b. The parameter appearing in the function definition is called the formal parameter and the expressions appearing in a function call are known as the actual 
#      parameters
#
# Q3c. In what ways are parameters similar to and different from ordinary variables?

# A3c. Parameters are like ordinary function variables in that they are local to the function and serve as "named values." They are different because they are 
#      automatically assigned an initial value when the function is called. Normal local variables have to be assigned a value within the function definition.

# Q4a. Functions can be thought of as miniature (sub) programs inside other programs. Like any other program, we can think of functions as having input and output to 
#      communicate with the main program. How does the program provide "input" to one of it's functions?

# A4a. A program provides input by parameters

# Q4b. Functions can be thought of as miniature (sub) programs inside other programs. Like any other program, we can think of functions as having input and output to 
#      communicate with the main program. How does a function provide output to the program?

# A4b. Usually through a return statement. Functions may also change the values of mutable parameters

# Q5a. Consider this simple function. What does thsi function do?

def cube(x):
 answer = x * x * x
 return answer

# A5a. This function computes the cube of x

# Q5b. Show how a program could use this function to print the value of y(3)

def cube(y)

# Q5c. Here is a fragment of the program that uses this function. The output from this function is 4 27. Explain why the output is not 27 27 even though the cube seems to
#      to change the value of the answer to 27.
#
 answer = 4
 result = cube(3)
 print(answer, result)

# A5c. There are two different variables named answer. The variable inside of cube is changed, but it does not affect the value of the other variable.

# Programming Exercises

# Exercise 1

# Write a program to print the lyrcis of "Old McDonald had a Farm for 5 different animals

#Old McDonald had a Farm

def line1():
    print("Old McDonald had a farm,", "Ee-igh, Ee-igh, Oh!")

def verse(animal, noise):
    print("And on that farm he had a(n)", animal+",", "Ee-igh, Ee-igh, Oh!")
    print("With a", noise, noise, "here and a", noise, noise, "there")
    print("Here a", noise+",", "there a", noise+",", "everywhere a(n)", noise, noise)


def main():
    line1()
    verse("horse", "neigh")
    line1()
    print()
    line1()
    verse("duck", "quack")
    line1()
    print()  
    line1()
    verse("sheep", "baa")
    line1()
    print()
    line1()
    verse("cow", "moo")
    line1()
    print()
    line1()
    verse("dog", "woof")
    line1()
    print()

main()

# Exercise 2

# Write a program to print the lyrics for ten verses of "The ant's go marching in

# The ants go marching in

def verse():
        print("Into the ground...")
        print("To get out...")
        print("Of the rain.")
        print("Boom! " * 3)

def ants():
    num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    rhyme = ['suck his thumb','tie his shoe','brush his hair', 'shut the door','dance like crazy','pick up stones', 'eat the grass','make a cake', 'eat a bug', 'chase the cat']
    for i in range (10):
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(num[i])))
        print("The ants go marching {0} by {0},".format(str(num[i])))
        print("The little one stops to {0},".format(str(rhyme[i])))
        print("And they all go marching down...")
        verse()
        print()
def main():
    ants()
main()

# Exercise 3

# Write definitions for these functions

# sphereArea(radius) Returns the surface area of a sphere having a given radius

# Calculating the radius of a sphere
import math

def sphereArea(radius):
    return 4 * math.pi * radius**2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius * radius * radius

def main():
    r = eval(input("Enter the radius of the sphere: "))
    print("The area of the sphereis", sphereArea(r))
    print()
    print("The volume of a sphere is", sphereVolume(r))

main()

# Exercise 4

# Write definitions for the following two functions

# sumN(n) returns the sum of the first n natural numbers
# sumNCubes(n) returns the sum of the cubes of the first n natural numbers

def sumN(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

def sumNCube(n):
    total = 0
    for i in range(1,n+1):
        total = total + i**3
    return total

def main():
    print("This program computes the sum and sum of cubes of the first")
    print("N natural numbers.\n")

    n = int(input("Please enter a value for n: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCube(n)))

main()

#Here are some basic argument specifiers you should know:

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

# Exercise 5

# Redo Programming Exercise 2 from Chapter 3. use two functions - one to compute the area of a pizza and one to compute cost per square inch.

#This program will calculate the cost per square inch of a pizza given its diameter and price

#Don't forget you may need float as the divsion may not produce integers (Final output will say 0)

#When formatting at the end, use %f for floating point numbers

import math

#Calculate the area of a pizza

def area(d):
    return math.pi * (0.5 * d)**2

#calculate the cost per square inch of the pizza 

def costPerInch(d, price):
    return float(price) / area(d)

def main():
    print("This program will calculate the area and the cost per square inch of a pizza given its diameter and price")
    diameter = float(input("What is the diameter of the pizza? "))
    cost = float(input("What is the cost of the pizza? "))
    print("The area of the pizza is %f" % (area(diameter)))
    print("The cost per square inch of the pizza is $%f " % (costPerInch(diameter,cost)))

main()

#Exercise 6

#Write a program to calculate the area of a triangle given the length of its 3 sides as parameters. (See programming exercise 9 from Chapter 3) Use your function to 
#augment triangle2.py from this chapter so that it also displays the area of the triangle

import math

def triangle(a, b, c):
    # The bottom 2 calculations are what is needed from C3Ex9 to calulate the area of a triangle
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return A

def main():
    a, b ,c  = eval(input("Please enter the length of the 3 sides of the triangle separated by a comma: "))
    A = triangle(a, b, c)
    print("The bottom 4 lines show different ways of formatting")
    print("The area of a triangle is", round(A, 2))
    print("The area of a triangle is %d" %(A))
    print (f"The area of a triangle is {A}.")
    print("The area of a triangle is", round(triangle(a, b, c), 2))

main()

# Exercise 7

# Write a function to compute the nth Fibonacci number. Use your function to solve Programming Exercise 16 from Chapter 3

# This program computes the nth Fibonacci number

# Example 0, 1, 2, 3, 4, 5, 6, 7
#         0, 1, 1, 2, 3, 5, 8, 13

def Fibonacci(number):
    if (number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return (Fibonacci(number - 2) + Fibonacci(number - 1))

def main():
    number = int(input("Enter the Range Number: "))
    for n in range(0, number):
        print(Fibonacci(n))

main()
