# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 1: Computers and Programs
# End-of-Chapter Exercises

# Review Questions

# 1. Computer Science is the study of computer - False

# A - Computer Science is the study of what can be computed using the techniques of design, analysis and experimentation. Computer science is the foundation of the broader field 
# of computing which includes areas such as networking, databases and information systems as an example

# 2. The CPU is the brain of the computer - True

# 3. Secondary memory is also called RAM - False

# A - Secondary memory is where permanent information is stored on devices such as HDD, SDD or external storage like USB drives.

# 4. All information that a computer is currently working on is stored in main memory - True

# 5. The syntax of a language is its meaning and semantics is its form - False

# A - Every structure in a programming language  has a precise form (Syntax) and a precise meaning (Semantics)

# 6. A function definition is a sequence of statements that defines a new command - True

# 7. A programming environment refers to a place where programmers work - False

# A - An IDE (Integrated Development Environment) is specifically designed to help programmers write programs.

# 8. A variable is used to give a name to a value so it can be referred to in other places - True

# 9. A loop is used to skip over a section of a program - False

# A loop performs a seqence of statements multiple times 

# Multiple Choice

# 1. B
# 2. D
# 3. D
# 4. A
# 5. B
# 6. B
# 7. C
# 8. B
# 9. A
# 10. D

# Discussion questions

# Q1a) Hardware vs Software
# Hardware is the physical components of the computer, such as the central processing unit (CPU) , hard disk , monitor , keyboard and mouse. 
# Software is the programs that run on a computer. A computer system requires both hardware and software to function.

# Q1b) Algorithm vs Program
# An algorithm is a sequence of steps for solving a particular problem
# A program is the result of transforming an algorithim into a working solution

# Q1c) Programming Language vs Natural Language
# Programming language are exact and unambiguous way. Each structure in a programming language has a precise form (syntax) and a precise meaning (semantics)
# Natural language is fraught with ambiguiuty and imprecision and miscommunication is common place

# Q1d) High level language vs Machine languge
# A high level language must be compiled or interpreted fot the computer to understand it. Programs are usually written in high level languages such as Python.
# Computer hardware understands only a low level langauge called machine language.

# Q1e) Intepreter vs Compiler
# A high level language must either be compiled or interpreted in order for the computer to understand it. A compiler is a complex computer program which takes in another 
# program written in a high level language and translates it into an equivalent program in the machine language of the computer. Once a program is compiled, it may be run over
# and over again without the need for the compiler or source code
# An interpreter is a program which simulates a computer that understands a high level language. Rather than translating the source program into a machine equivalent, it 
# analyses and executes the source code instruction by instruction. The interpreter and the source code are needed every time the program runs.

# Q1f) Syntax vs Semantics
# Each structure in a programming language has a precise form (syntax) and a precise meaning (semantics)

# Q2. List and explain in your own words the role of each of the fice basic functional units of a computer depicted in Figure 1.1 

# Input devices  - Keyboard, mouse to provide some soft of input to the computer
# CPU - Central Processing Unit is the brain of the computer. This is where all the basic operations of the computer are carried out
# Main Memory - Stores programs and data which can be accessed by the CPU
# Secondary memory - Main memory is volatile and is lost when the computer is powered off
# Output devices - When information needs to be displayed, the CPU sends it to one or more output devices

# Q3. Write a detailed algorithm for making a peanut butter and jelly sandwich
# 
# 1. Go to cupboard and get peanut butter and jelly.
# 2. Go to bread bin and get loaf of bread
# 3. Take 2 slices of bread out of the packed and lay them face down
# 4. Go to the drawer and get 2 knives
# 5. Open the jar and use one knife to get peanut butter out the jar and spread on both slices of bread
# 6. Open the jar and use the second knife to get jelly out the jar and spread on top of the peanut butter on the bread
# 7. Take on slice and place it on top of the other sice so the peanut butter and jelly are together
# 8. Use the knife to cut the sandwich in half
# 9. Put lid back on peanut jar and jelly jar
# 10. Put peanut butter jar back in cupboard
# 11. Put jelly jar back in the cupboard
# 12. Wash up knives
# 13. Eat sandwich

# Q4. Many numbers stored in a computer are not exact values but approximations which will be seen in later chapters. Usually small differences are not a problem but given
# what you have learned about chaotic behaviour, can you think of any examples where this might be a problem.

# A4. This may be a critical problem in financial firms, architectural calculations or medical measurements

# Q5) Trace through the chaos program from Section 1.6 by hand using 0.15 as the input value and show the sequence of output which results

# chaos.py
# This program illustrates a chaotic function
def main():
         print("This program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range(10):
             x = 3.9 * x * (1 - x)
             print(x)

# x = .15
#                                                      
# for 0 in range(10):                                                  
#     x = 3.9 * .15 * (1 - .15)                        
#     print(0.49725)                                   
#                                                       
# for 1 in range(10):                                  
#     x = 3.9 * 0.49725 * (1 - 0.49725)                 
#     print(0.97497050625)                             
#                                                       
# for 2 in range(10):                                  
#     x = 3.9 * 0.97497050625 * (1 - 0.97497050625)    
#     print(0.09517177095122)
#     
# for 3 in range(10):                    
#     x = 3.9 * 0.09517177095122 * (1 - 0.09517177095122)
#     print(0.3358450093644)
# 
# for 4 in range(10):                    
#     x = 3.9 * 0.3358450093644 * (1 - 0.3358450093644)
#     print(0.86990724229278)
# 
# for 5 in range(10):                    
#     x = 3.9 * 0.86990724229278 * (1 - 0.86990724229278)
#     print(0.44135766518747)
# 
# for 6 in range(10):                    
#     x = 3.9 * 0.44135766518747 * (1 - 0.44135766518747)
#     print(0.96158819861419)
# 
# for 7 in range(10):                    
#     x = 3.9 * 0.96158819861419 * (1 - 0.96158819861419)
#     print(0.14405170611043)
# 
# for 8 in range(10):                    
#     x = 3.9 * .0.14405170611043 * (1 - .0.14405170611043)
#     print(0.48087316710069)
# 
# for 9 in range(10):                    
#     x = 3.9 * 0.48087316710069 * (1 - 0.48087316710069)
#     print(0.97357324062664)
#
#The below shows the difference when a calculator is used vs the program's intepretation
#
# Trace output sequence       Output sequence when program is run:
# 0.49725                     0.49724999999999997 
# 0.97497050625               0.97497050625
# 0.09517177095122            0.09517177095121285
# 0.3358450093644             0.3358450093643686
# 0.86990724229278            0.8699072422927216
# 0.44135766518747            0.4413576651876355
# 0.96158819861419            0.9615881986142427
# 0.14405170611043            0.14405170611022783
# 0.48087316710069            0.48087316710014555
# 0.97357324062664            0.9735732406265619

# Programming Exercises

# PROGRAMMING EXERCISES

# 1a) print("Hello, world!") Hello, world!
# 1b) print("Hello", "world!") Hello world!
# 1c) print(3) 3
# 1d) print(3.0) 3 0
# 1e) priint(2 + 3) 5
# 1f) print 2.0 +3.0) 5.0
# 1g) print("2" + "3") 23
# 1h) print("2 + 3 =" 2 +3)  2 + 3 = 5
# 1i) print(2 * 3) 6
# 1j) print(2 **3) 8
# 1k) print( 7 / 3) 2.3333333333333335
# 1l) print(7 //3) 2 #floor division, rounds down to nearest integer

#Q2. Enter and run the chaos program from section 1.6. Try it out with various values of input between 0 and 1 to see that it functions as described in the chapter

# Value = 0.2
# Output
# 0.6240000000000001
# 0.9150335999999998
# 0.30321373239705673
# 0.8239731430433209
# 0.5656614700878645
# 0.9581854282490118
# 0.1562578420270518
# 0.5141811824451928
# 0.9742156868513789
# 0.0979659811418921

# Value = 0.3
# Output
# .819
# 0.5781321000000001
# 0.951191962303401
# 0.18106067129594494
# 0.5782830479626462
# 0.9510998811665442
# 0.18138469912496583
# 0.5790887311884146
# 0.950605393136126
# 0.1831236407388855

# Q3.Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistics function. Your modified line of code should look like the following

#def main():
#    x =eval(input("Enter a number between 0 and 1: "))
#    for i in range(10):
#        x = 2.0 * x * (1-x)
#        print(x)
#
#main()

# Value = 0.2
# Output
# 0.32000000000000006
# 0.43520000000000003
# 0.49160192
# 0.4998589445046272
# 0.49999996020669446
# 0.49999999999999684
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994

# Value = 0.3
# Output
# .42
# 0.4872
# 0.49967231999999995
# 0.4999997852516352
# 0.4999999999999078
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994

# Whatever value is used, the value always seem to end up around 0.5 and much less random than 3.9

#Q4. Modify the chaos program so it prints out 20 values instead of 10

#def main():
#    x =eval(input("Enter a number between 0 and 1: "))
#    for i in range(20):
#        x = 2.0 * x * (1-x)
#        print(x)
#
#main()

#Q5. Modify the chaos program so that the number of values to print is determined by the user. You will have to add another line at the top of the program to get another value
#from the user

#def main():
#    x = eval(input("Enter a number between 0 and 1: "))
#    n = eval(input("Enter a number of values to print: ")
#    for i in range(n):
#        x = 2.0 * x * (1-x)
#        print(x)
#
#main()

#Q6a. The calculations performed in the chaos program can be written in a number of ways that are algebraically equivalent. Write a program for each of the following ways of
# doing the computation. Have your programs print out 100 interations
# 3.9 * x * x (1 - x)

def main():
    print("Question 6a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a value between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)
main()

#Q6b 
# 3.9 * (x - x * x)

#def main():
     print("Question 6b chaotic function")
     n = eval(input("How many numbers should I print? "))
     x = eval(input("Enter a value between 0 and 1: "))
     for i in range(n):
         x = 3.9 * (x - x * x)
         print(x)
main()

#Q6c
# 3.9 * x - 3.9 * x * x)

#def main():
     print("Question 6c chaotic function")
     n = eval(input("How many numbers should I print? "))
     x = eval(input("Enter a value between 0 and 1: "))
     for i in range(n):
         x = 3.9 * x - 3.9 * x * x
         print(x)
main()

# Can also combine all 3 programs as per below program

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    x2 = x
    x3 = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        x2 = 3.9 * (x2 - x2*x2)
        x3 = 3.9*x3 - 3.9*x3*x3
        print(x,x2,x3)

main()

# The three scripts show that algebraically equivalent expressions do not return the same outputs when the input values are a floating-point data type. 
# This is because of rounding errors found in floats

# Q7. [Advanced] Moify the chaos program so it accepts two inputs and then prints a table with 2 columns similar to the one shown in section 1.8. (Note: you probably won't be
#able to get the columns to line up as nicely as those in the example. 

# This is from the solutions 

# File: chaos.py
# Chaos program to print side-by-side values
# Note: This output is UGLY, but uses only things seen in Chapter 1
#       For a more elegant version see c05ex12.py

def main():
    print("This program illustrates a chaotic function")
    x1 = eval(input("Enter the first seed between 0 and 1: "))
    x2 = eval(input("Enter the second seed between 0 and 1: "))
    print()
    print("input     ", x1, " | ", x2)
    print("-------------------------------------------")
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("      ", x1, " | ", x2)

main()
