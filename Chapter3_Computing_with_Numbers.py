# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 3: Computing with Numbers
#
# Review questions
#
# Q1. Information that is stored and manipulated by computers is called data
# TRUE
#
# Q2. Since floating point numbers are extremely accurate, they should generally be used instead of ints
# FALSE. Using a float allows us to represent a much larger range of values but the amount of precision is still fixed. A computer stores floating point numbers as a pair of fixed
# length binary integers. One integer represents the string of digits in the value and is called the mantissa. The second integerkeeps track of where the whole part ends and where
# the fractinal part begins. Since the underlying numbers are binary, only fractions that involve powers of 2 can be represented exactly, any other fraction produces an infintely
# repeating mantissa. when an infinitely long mantissa is truncated to a fixed length for storage, the result is a close approximation
#
# Q3. Operations like addition and subtraction are defined in the math library
# FALSE
#
# Q4. The number of possible arrangments of n items is equal to n!
# TRUE. Page 68. In mathematics, factorials are often denoted with an exclamation point (!)
#
# Q5. The sqrt function computes the squirt of a number.
# FALSE. It computes the square root of an input value
#
# Q6. The float data type is identical to the mathematical concept of a real number 
# FALSE
#
# Q7. Computers represent numbers using base 2 (binary) representations
# TRUE
#
# Q8. A hardware float can represent a larger range of values than a hardware int
# TRUE. Using a float allows us to represent a much larger range of values but the amount of precision is still fixed
#
# Q9. Type conversion functions such as float are a safe alternative to eval for getting user input
# TRUE
#
# Q10. In Python, 4+5 is the same as 4.0+5.0
# FALSE. 4+5 = 9 and 4.0+5.0 = 9.0
#
# Multiple choice
#
# Q1. which of the following is not a built in Python data type
# a) int
# b) float
# c) rational *
# d) string
#
# Q2. Which of the following is not a built in operation?
# a) +
# b) %
# c) abs()
# d) sqrt() *
#
# Q3. In order to use functions in the math library, a program must include a 
# a) a comment
# b) a loop
# c) an operator
# d) an import statement *
#
# Q4. The value of 4! is
# a) 9
# b) 24 *
# c) 41
# d) 120
# A factorial is a function that multiplies a number by every number below it. For example 4!= 4*3*2*1=24
#
# Q5. The most appropriate data type for sorting the value of pi is
# a) int
# b) float *
# c) irrational
# d) string 
#
# Q6. The number of distint values that can be represented using 5 bits is 
# a) 5
# b) 10
# c) 32 *
# d) 50
# 2^5 = 32
#
# Q7. In a mixed type expression involving ints and floats, Python will convert 
# a) floats to ints
# b) ints to strings
# c) both floats and ints to strings 
# d) ints to floats *
#
# Q8. Which of the following is not a Python type conversion function?
# a) float
# b) round
# c) int
# d) abs *
#
# Q9. The pattern used to compute factorials is
# a) accumulator *
# b) input, process, output
# c) counted loop
# d) plaid *
#
# Q10. In modern Pythin, an int value that grows larger than the underlying hardware int
# a) causes an overflow
# b) converts to float
# c) breaks the computer
# d) uses more memory *
#
# Discussion Questions
#
# Show the result of evaluating each expression. Be sure that the value is in the proper form to indicate its type (int or float). If the expression is illegal, explain why.
#
# Q1a) 4.0 / 10.0 + 3.5 * 2 = 7.4
# Q1b) 10 % 4 + 6 / 2 = 5
# Q1c) abs(4 - 20) // 3) ** 3 = 8
# Q1d) sqrt(4.5 - 5.0) + 7 * 3 = illegal because sqrt cannot handle negative numbers
# Q1e) 3 * 10 // 3 + 10 % 3 = 10 (10 // 3) = 3 and (10 % 3) = 1 so 3 x 3 + 1
# Q1f) 3 ** 3 = 27
#
#  Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the math library has been imported (via import math).
#
# Q2a) (3 + 4) * 5
# Q2b) (n(n-1) / 2          
# Q2c) 4 * math.pi * r**2                       
# Q2d) math.sqrt(r * math.cos(a)**2 + r * math.sin(b)**2)
# Q2e) (y2 - y1) / (x2 - x1)



# Q1. Write a program to calculate the volume and surface area of a sphere fro its radius, given as input. Here are some formulas that might be useful
# V = 4/3πr^3
# A = 4πr^2
#
#This program will calculate the volume and surface area of a sphere from it's radius
import math
def main():
    print("This is a program to calculate the volume and surface area of a sphere from it's radius")
    radius =(eval(input("What is the radius? ")))
    volume = round((4 / 3) * 3.142 *(radius ** 3),2)
    area = round(4 * 3.142 * (radius * radius),2)
    print("The volume of the sphere is", volume)
    print("The surface area of sphere is", area)
main()
#
# Q2. Write a program that calculates the cost per square inch of a cirular pizza, given its diameter and price. The formula for area is A = πr^2
#
#This program will calculate the cost per square inch of a pizza given its diameter and price
def main():
    print("This program will calculate the cost per square inch of a pizza given its diameter and price")
    diameter = eval(input("What is the diameter of the pizza? "))
    cost = eval(input("What is the cost of the pizza? "))
    radius = diameter / 2
    area = round(3.142 * (radius * radius),2)
    print("The cost per square inch of the pizza is", round((cost/area), 2))
main()
#
# Q3. 






