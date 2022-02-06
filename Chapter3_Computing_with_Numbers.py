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
# Q8. 




