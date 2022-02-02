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

