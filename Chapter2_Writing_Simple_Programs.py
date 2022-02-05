# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 2: Writing simple programs
# End-of-Chapter Exercises

# Review Questions

# Q1. The best way to write a program is to immediately type in some code and then debug it until it works. FALSE
#
# 1A. Ref Page 27/28. "Writing large programs is daunting challenge. It would be almost impossible without a systematic approach. The process of creating a program is often
#      broken down into stages according to the information that is produced in each phase."
#
# Q2. An algorithm can be written without using a programming language. TRUE
#
# A2. Ref Page 28. Analyse the problem, Determine specifications and what your program will do, Create a design. The main taks is to design the algorithm which will meet the 
#     specification. Ref Page 30. An algorithm can be written using Pseudocode which is just precise English for describing what a program does.
#
# Q3. Programs no longer require modification after they are written and de-bugged. FALSE
#
# A3. Ref Page 28. One of the processes for creating a program involves testing and debugging the program. Programs are highly likely to be modified again and again after being
#     created which in turn will need further testing and debugging.
#
# Q4. Python identifiers start with an underscore or a letter. TRUE
#
# A4. Ref Page 31. Python has rules about identifiers or names as they're also known by. Each identifier must begin with an underscore or a letter
#
# Q5. Keywords make good variable names. FALSE
#
# A5. Ref Page 31. Some identifiers are part of Python itself and should not be used as they have a completely different meaning or function.
#
# Q6. Expressions are built from literals, variables and operators. TRUE
#
# A6. Ref Page Page 32: "The simplest kind of expression is a literal." p.33 "A simple identifier can also be an expression. We use identifiers as variables to give names 
#     to values. When an identifier appears as an expression, its value is retrieved to provide a result for the expression. p.34 "More complex and interesting expressions 
#     can be constructed by combining simpler expressions with operators."
#
# Q7. In Python x = x + 1 is a legal expression. TRUE
#
# A7. Ref Page 37. A variable can be assigned many times and the current value of a variable can be used to update its value. See Figure 2.1 on Page 38.
#
# Q8. Python does not allow the input of multiple values within a single statement. FALSE
#
# A8. Ref Page 42. Simutaneous assignment can be used to get multiple values from a user in a single input. Example below
#
#     score1, score 2 = eval(input("Please enter 2 scores separated by a comma: "))
#
# Q9. A counted loop is designed to iterate a certain amount of times. TRUE
#
# A9. Ref Page 43/44. A definite loop will execute a definite number of times and is basically known as a counted loop
#
#     for i in range(10): for example
#
# Q10. In a flowchart, diamonds are used to show statement sequences and rectangles are used for decision points. FALSE
#
# A10. Ref Page 46/47. Diamonds are used for decision points and rectangles are use to assign the next item in the sequence 
#
# Multiple Choice Questions
#
#  Q1. Which of the following is not a step in the software development process?
#     (a) specification     
#     (b) testing/Debugging
#     (c) fee setting       
#     (d) maintenance
#     
# A1. [C]
#
#     Ref Page 50 The software development process involves the following steps:
#     1. Problem Analysis
#     2. Program Specification
#     3. Design
#     4. Implementation
#     5. Testing/Debugging
#     6. Maintenance

#  Q2. What is the correct formula for converting Celsius to Fahrenheit?
#     (a) F = 9/5(C) + 32       
#     (b) F = 5/9(C) - 32
#     (c) F = B^2 - 4AC         
#     (d) F = (212 - 32) / (100 - 0)
#
#
# A2. [A]
#     Ref Page29 "She knows that 0 degrees Celsisus (freezing) is equal to 32 degreesFahrenheit. With this information, she computes the ratio of Fahrenheit to Celsius degrees 
#     as (212-32)/(100-0) = 180/100 = 9/5. Using F to represent the Fahrenheit temperature and C for Celsius, the conversion formula will have the form F = (9/5)C + k for some 
#     constant K. Plugging in 0 and 32 for C and F, respectively, Susan immediately sees that k = 32. So the final formula for the relationship is F = (9/5)C + 32."]

#  Q3. The proces of describing exactly what a computer program will do to solve a problem is called
#     (a) design     
#     (b) implementation     
#     (c) programming     
#     (d) specification
#     
# A3. [D]    
#     Ref page 50. "Program Specification: Deciding exactly what the program will do."]

#  Q4. Which of the following is not a legal identifier?
#     (a) spam     
#     (b) spAm     
#     (c) 2spam     
#     (d) spam4U
#
# A4. [C]
#     Ref Page 51 "Python has some rules about how identifiers are formed. Every identifier must begin with a letter or underscore (the "_" character) which may be followed by 
#     any sequence of letters, digits, or underscores."]

#  Q5. Which of the following are not used in expressions?
#
#     (a) variables     
#     (b) statements     
#     (c) operators    
#     (d) literals
#
# A5. [B]      
#     Ref page 32 "The simplest kind of expression is a literal." p.33: "A simple identifier can also be an expression. We use identifiers as variables to give names to values." p.32: 
#     "More complex and interesting expressions can be constructed by combining simpler expressions with operators." p.523: "statement: A Single command in a programming 
#      langauge."]

#  Q6. Fragments of code that produce or calculate new data values are called
#     a) identifiers            
#     b) expressions
#     c) productive clauses     
#     d) assignemnt statements
#
# A6. [B]
#     Ref Page 32 "The fragments of program code that produce or calculuate new data values are called expressions."

#  Q7. Which of the following is not a part of the IPO pattern?
#     a) input     
#     b) program     
#     c) process     
#     d) output
#
# A7. [B]
#    Ref Page 29 "...a standard pattern: Input, Process, Output (IPO)." As discussed in the previous chapter, a program is a specific set of instructions telling a computer 
#    precisely what to do step by step.]

#  Q8. The template for <variable> in range(<expr>) describes
#     a) a general for loop     
#     b) an assignment statement
#     c) a flowchart            
#     d) a counted loop 
#
# A8. [D]
#     Ref Page 44 "This particular loop patter is called a counted loop.."

#  Q9. Which of the following is the most accurate model of assignment in Python? [A}
#     a) sticky-note     
#     b) variable-as-box     
#     c) simultaneous     
#     d) plastic-scale
#
# A9. [A]
#     Ref page 38 "The effect is like moving a sticky note from one object to another."
#
# Q10. In Python, getting user input is done with a special expression called [D]
#     a) for     
#     b) read     
#     c) simulataneous assignment     
#     d) input
#
# A10. [D]
#      Ref Page 39  "The purpose of an input statement is to get some information from the user of a program and store it in a variable. Some programming languages have a special
#      statement to do this. In Python, input is accomplished using an assignment statement combined with a built-in function called input."
#
# Discussion Exercises
#
# Q1. List and describe in your own words, the six steps in the software development process
#
# A1. Problem Analysis = This first stage involvs analysing the problem you are trying to solve. Find as much information as possible
#     Determine the specification = Write down exactly what you want your program to do. You don't need to worry about how you are going to program it at this point, you just 
#     need to decide what it needs to accomplish
#     Create a design = This is where you design the overall structure of the program so we can see how it is going to be worked out
#     Implement the design = Implement the design as a Python program in code
#     Test/Debug the program = Run the program and find any errors. Try debugging the errors to see where anything has gone wrong.
#     Maintain the program = Sometimes programs need to be updated or enhanced which is part of the ongoing maintenance of programs.
#
# Q2. Write out the chaos.py program (Section 1.6) and identifiy parts of the program as follows
#
#     Circle each identifier
#     Underline each expression
#     Put a comment at the end of each line indicating the type of statement on that line. E.g. Output, Assignment, Input, Loop etc
#
# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():                                                # function definition
    print("This program illustrates a chaotic funciton.")  # output statement
    x = eval(input("Enter a number between 0 and 1: "))    # assignment statement wrapped around input statement
    for i in range(10):                                    # loop statement
        x = 3.9 * x * (1 - x)                              # expression
        print(x)                                           # output statement
#
#   Identifiers: main(), print(), x, eval, input, for, i, in, range
#
# Q3. Explain the relationship between the concepts: definite loop, for loop and counted loop
#
# A3. A definite loop is the simplest kind of loop that will execute a definite number of times that is defined at the start of the loop.
#
#     A counted loop is a particular loop pattern. It is a common way to use a definite loop. It will go around the loop body according to a defined count or number of times.
#     Example for i in range(10)
#
#     A for loop is a statement in Python that is used to implement a counted loop and has the form
#     for <var> in <sequence>:
#         <body>
#
# Q4a. Show the output from the following fragments
#
for i in range(5):
    print(i*i)
0
1
4
9
16
#  
# Q4b. Show the output from the following fragments
#
for d in [3,1,4,1,5]:
    print(d, end=" ") # The ‘end’ is an argument included in the ‘print’ function in Python. The default value for it is a newline ‘\n’ character. The ‘end’ specifies the 
#    character or string that the print statement should end with.
3 1 4 1 5 
#
# Q4c. Show the output from the following fragments
#
for i in range(4):
    print("Hello")
Hello
Hello
Hello
Hello
#
# Q4d. Show the output from the following fragments
#
for i in range(3):
    print(i, 2**i)
0 1
1 2
2 4
3 8
4 16
#
# Q5. Why is it a good idea to first write out an algorithm in pseudocode rather than jumping immediately to Python code?
#
# A5. So you can get a good idea of what you want to do before starting so you don't overload yourself trying to code straightaway.
#
# Q6. The Python print function supports other keyboard parameters besides end. One of these other keyboard parameters is sep. What do you think the sep parameter does? 
#     Hint: sep is short for separator. Test your idea either by trying it interactively or by consulting the Python documenation.
#
# A6. The sep parameter separates specifies the separator between multiple values when printing.
#
print("Hello", "how are you?", sep="---")
Hello---how are you?
#
# Q7. What do you think will happen when the following code is executed?
#
# A7. When range(0) is used, it does not calculate anything. # See Page 45 for more information
#
print("start")
for i in range(0):
    print("Hello")
print("end")
start
end
#
# Programming Exercises
#
# Q1. A user friendly program should put in an introduction tells the user what the program does.Modify the convert.py program to print an introduction.
#
# convert.py
def main():
    print("This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius +32
    print("The temperature is", fahrenheit, "degrees fahrenheit")

main()
#
# Q2. On many systems with Python, it is posible to run a program by simply clicking (or double-clicking) on theicon of the program file. If you are able to run the convert.py 
#     program this way, you may discover another usability issue. The program starts running in a new window, but as soon as the program is finished, the window disappears so 
#     that you cannot read the results. Add an input statement at the end of the program so that it pauses to give the user a chance to read the results. Something like this 
#     should work:
#
#     input("Press the <Enter> key to quit.")
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit by: Susan Computewell
#
def main():
    
    print("This program coverts a temperature in Celsius to a temperature in Fahrenheit.")
    
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
    
main()
#
# Q3. Modify the avg2.py program (Section 5.2.3) to find the average of three exam scores
#
## avg3.py
#   A simple program to average three exam scores  
#   Illustrates use of multiple input
#
def main():
    
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the three scores is:", average)

main()
#
# Q4. Modify the convert.py program (Section 2.2) with a loop so that it executes 5 times before quitting. Each time through the loop, the program should get another temperature
#     from the user and print a converted value
#
# convert.py
#
def main():
    for i in range(5): #This line was added to make the program run 5 times
        print("This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit")
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius +32
        print("The temperature is", fahrenheit, "degrees fahrenheit")

main()
#
This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit
What is the Celsius temperature? 10
The temperature is 50.0 degrees fahrenheit
This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit
What is the Celsius temperature? 20
The temperature is 68.0 degrees fahrenheit
This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit
What is the Celsius temperature? 10
The temperature is 50.0 degrees fahrenheit
This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit
What is the Celsius temperature? 5
The temperature is 41.0 degrees fahrenheit
This is a program to convert the temperature in degrees Celsius and convert it to Fahrenheit
What is the Celsius temperature? 4
The temperature is 39.2 degrees fahrenheit
#
# Q5. Modfiy the convert.py program (Section 2.2) so that it computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0 degress 
#     celsius to 100 degrees celsius.
#
# convert.py
#     Table of temperature conversions

# Note: Table alignment is hacked here. Formatted output is covered in
#       Chapter 5.

def main():
    print("Celsius  Fahrenheit")
    print("-------------------")
    print(" 0          32.0")
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print(celsius, "        ", fahrenheit)
    print("100         212.0")

main()

Celsius  Fahrenheit
-------------------
 0          32.0
10          50.0
20          68.0
30          86.0
40          104.0
50          122.0
60          140.0
70          158.0
80          176.0
90          194.0
100         212.0
#
# Q6. Modify the futval.py program (Section 2.7) so that the number of years for the investment is also a user. input. Make sure to change the final message to reflect the correct 
#     number of years.
# 
#   futvl.py
#   Future value with number of years as an input.
#
def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)

main(
#
# Q7. Suppose you have an investment plan where you invest a certain fixed amount every year. Modify futval.py to compute the total accumulation of your investment. The inputs
#     to the program will be the amount to invest each year, the interest rate, and the number of years for the investment.
#
def main():
    print("This program calculates the total future value")
    print("of a multi-year investment with")
    print("non-compounding interest and an additional")
    print("investment of a certain fixed amount each year.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest: "))
    years = eval(input("Enter the number of years for the investment: "))
          
    for i in range(years):
          principal = principal + yearlyinvestment
          principal = principal * (1 + apr)

    print("The value in ", years ,"years is:", principal, sep=" ")

main()
#
#
# Q8. As an alternative to APR, the interest accrued on an account is often described in terms of a nominal rate and the number of compounding periods. For example, if the 
#    interest rate is 3% and the interest is compounded quarterly, the account actually earns .75% interest every 3 months.
#
#     Modify the futval.py program to use this method of entering the interest rate. The program should prompt the user for the yearly rate (rate) and the number of times that 
#     the interest is compounded each year (periods). To compute the value in ten years, the program will loop 10 * periods times and accrue rate/period interest on each 
#     iteration
#
# futval_modified.py    
# Future value with multiple compounding periods

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

main()
#
# Q9. Write a program that converts temperatures from Fahenheit to Celcius
#
# convert.py
#
def main():
    for i in range(5): #This line was added to make the program run 5 times
        print("This is a program to convert the temperature in Fahrenheit and convert it to Celsius")
        fahrenheit = eval(input("Please enter the Fahrenheit temperature: "))
        celsius = (fahrenheit -32) * 5/9 
        print("The temperature is", celsius, "degrees")

main()
#
# Q10. Write a program that converts distances measured in kilometers to miles. One kilometer is approximately 0.62
#
#
#This program will convert distances from kilometers to miles

def main():
    print("This is a program to convert kilometers to miles")
    kilometers = eval(input("How many kilometers do you want to convert? "))
    miles = kilometers * 0.62
    print(kilometers, "kilometers is", miles, "miles")

main()
#
# Q11. Write a program to perform a unit conversion of your own choosing. make sure that the program prints an introduction that explains what to do. 
#
# convert_litres_to_gallons.py
#     A program to convert litres to gallons

def main():
    print("This program converts litres to gallons.")

    gallons = eval(input("How many gallons?: "))
    litres = gallons * .264172052

    print("The fluid volume in litres is", litres, "litres.")

main()
#
# Q12. Write an interactive Python calculator program. The program should allow the user to type a mathematical expression, and then print the value of the expression. Include a
#      loop so that that the user can perform many calculations (say, up to 100). Note: To quit early, the user can make the program crash by typing a bad expression or simply 
#      closing the window that the calculator program is running in. You'll learn better ways of terminating interactive programs in later chapters
#
# calculator.py
# An interactive calculator (up to 100 expressions)

def main():
    print("Welcome to the Interactive Python Calculator")
    for i in range(100):
        result = eval(input(""))
        print(result)

main()

