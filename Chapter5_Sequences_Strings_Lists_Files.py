# "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
# Chapter 5: Sequences: Strings, Lists and Files
# End-of-Chapter Exercises

# REVIEW QUESTIONS
#
# Q1. A Python string literal is always enclosed in double quotes. FALSE
#  
# A1. Reference Page 130 "A string literal is formed by enclosing some characters in quotation marks. Python also allows strings to be delineated by single quotes (apostrophes).
#     There is no difference; just be sure to use a matching set."

# Q2. The last character of a string s is at position len(s)-1 TRUE
#
# A2. Reference Page 131 "Notice that in a string of n characters, the last character is at position n -1, because the index starts at 0." Length will give the length of a 
#     string and the n-1 value of the len will always be the last character
#
# Q3. A string always contains a single line of text. FALSE
# 
# A3. Reference Page 131. A string is a sequence of characters. This sequence can be of any length. In fact, it is also possible to have an empty string, i.e. "".]
#
# Q4. In Python, "4" + "5" is "45". TRUE
#
# A4. Reference Page 132. Handy operators for string concatenation is (+) which builds a string by glueing two strings together
#
# Q5. Python lists are mutable, but strings are not. TRUE
#
# A5. Reference Page 138. "While strings and lists are both sequences, there is an important difference between the two. Lists are mutable. That means that the value of an item in 
#     a list can be modified with an assignment statement. Strings, on the other hand, cannot be changed 'in place'"
#
# Q6. ASCII is a standard from representing characters using numeric codes. TRUE
#
# A6. Reference Page 140. "One important standard is called ASCII (American Standard Code for Information Interchange).ASCII uses the numbers 0 through 127 to represent 
#     characters typically found on an (American) computer keyboard, as well as certain special values known as control codes that are used to coordinate the sending and
#     receiving of information.
#
# Q7. The split method breaks a string into a list of substrings, and join does the opposite. TRUE
#
# A7. Reference Page 144 "Strings have built in methods The split method splits a string into a list of substrings. By default, it will split the string whever a space occurs.
#     Information on string methods can be seen in the table on Page 148.
#
# Q8. A substitution cipher is a good way to keep sensitive information secure. FALSE
#
# A8. Reference Page 150 "Substitution ciphers are a weak form of encryption. Since each letter is always encoded by the same symbol, a codebreaker coud use statistical 
#     information about the frequency of various letters and some simple trial and error testing to discover the original message."
#
# Q9. The add method can be used to add an item to the end of a list. FALSE
#
# A9. Reference Page 147 "The append method can be used to add an item at the end of a list. This is often used to build a list an item at a time."
#
# Q10. The process of associating a file with an object in a program is called "reading" the file. FALSE
#
# A10. Reference Page 159 "We need some way to associate a file on disk with an object in a program. This process is called opening a file. Once a file has been opened, its 
#      contents can be accessed through the associated file object.
#
# Multiple Choice
#
# Q1. Accessing a single character out of a string is called: [D]
#     a) slicing     b) concatenation     c) assignment     d) indexing
#
# Q2. Which of the following is the same as s[0:-1] [C]
#     a) s[-1]     b) s[:]     c) s[:len(s)-1]     d) s[0:1len(s)]
#
# Q3. What function gives the Unicode value of a character? [A]
#     a) ord     b) ascii     c) chr     d) eval
#     Reference Page 140. "Python provides a couple of built-in functions that allow us to switch back and forth between characters and the numberic values used to represent 
#     them in strings. The ord function returns the numeric ("ordinal") code of a single-character string, while chr goes the other direction."
#
# Q4. Which of the following can not be used to convert a string of digits into a number? [D]
#     a) int     b) float     c) str     d) eval
#
# Q5. A successor to ASCII that includes characters from (nearly) all written languages is [C]
#     a) TELLI     b) ASCII+ +     c) Unicode     d) ISO
#     Reference Page 140. "Most modern systems are moving to Unicode, a much larger standard that aims to include the characters of nearly all written languages."
#
# Q6. Which string method converts all the characters of a string to upper case? [D]
#     a) capitalize     b) capwords     c) uppercase     d) upper
#     See Page 148 table
#
# Q7. The string "slots that are filled in by the format method are marked by: [D]
#     a) %     b) $     c) []     d) {}
#     Reference Page 156. "Curly braces ({}) inside the template-string mark 'slots' into which the provided values are inserted. The information inside the curly braces tells 
#     which value goes in the slot and how the value should be formatted.
#
# Q8. Which of the following is not a file-reading method in Python? [C]
#     a) read     b) readline     c) readall     d) readlines
#     Reference Page 161. "Python provides three related operations for reading information from a file [read, readline, readlines]."
#
# Q9. The term for a program that does its input and output with files is [C]
#     a) file-oriented     b) multi-line     c) batch     d) lame
#
# Q10. Before reading or writing to a file, a file object must be created via [A]
#     a) open     b) create     c) File     d) Folder
#
# Discussion

# Q1. Given the initial statements, show the results of evaluating each of the following string expressions
#
#     s1 = "spam"
#     s2 = "ni!"
#
# Q1a "The knights who say, " + s2
# A1a. The knights who say, ni!
#
# Q1b. 3 * s1 + 2 * s2
# A1b. spamspamspamni!ni!
#
# Q1c. s1[1]
# A1c. p
#
# Q1d. s1[1:3]
# A1d. pa
#
# Q1e. s1[2] + s2[:2]
# A1e. ani
#
# Q1f. s1 + s2[-1]
# A1f. spam!
#
# Q1g. s1.upper
# A1g. SPAM
#
# Q1h. s1.upper().ljust(4) * 3
# A1g. SPAM.ljust(4) * 3
#      NI! NI! NI!
# Page 148 for table of string methods
#
# Q2. Given the same initial statements as in the previous problem, show a Python expression that could construct each of the following results by performing string operations
#     on s1 and s2
#
#     s1 = "spam"
#     s2 = "ni!"
# 
# Q2a. "NI"
# A2a. s2[:2].upper())
#
# Q2b "ni!spamni!"
# A2b. s2 + s1 + s2
#
# Q2c "Spam Ni!  Spam Ni!  Spam Ni!
# A2c. (s1.capitalize() +" "+s2.capitalize() +" ")*3
#
# Q2d. spam
# A2d. s1
#
# Q2e. ["sp", "m"]
# A2e. s1.split("a")
#
# Q2f. "spm"
# A2f. s1[0:2] + s1[-1] or "".join(s1.split("a"))
#
# Q3. Show the output of that would be generated by each of the following program fragments
# 
# Q3a. 
for ch in "aardvark":
  prin(ch)
  a
a
r
d
v
a
r
k
# Q3b. 
for w in "Now is the winter of our discontent...".split():
  print(w)
Now
is
the
winter
of
our
discontent...
#
# Q3c
for w in "Mississippi".split("i"):
  print(w, end=" ")
Msssspp
#
# Q3d
msg = ""
for s in "secret".split("e"):
  msg = msg + s
print(msg)
scrt
#
# Q3e
msg = ""
for ch in "secret":
  msg = msg + chr(ord(ch)+1)
  print(msg)
t
tf
tfd
tfds
tfdsf
tfdsfu
#
# Q4. Show the string that would result from each of the following string formatting operations. If the operation is not legal, explain why:
#
#     a) "Looks like (1) and (0) for breakfast".format("eggs", "spam")
#        The operation is not legal. Curly braces are required around 1 and 0.

#     b) "There is {0} {1} {2} {3}".format(1, "spam", 4 "you")
#         'There is 1 spam 4 you.'

#     c) "Hello {0}".format("Susan", "Computewell")
#        'Hello Susan'

#     d) "{0:0.2f} {0:0.2f}".format(2.3, 2.3468)
#        '2.30 2.30'

#     e) "{7.5f} {7.5f}".format(2.3, 2.3468)
#        The operation is not legal. There is no index followed by : supplied in each of the curly braces.

#     f) "Time left {0:02}:{1:05.2f}".format(1, 37.374)
#        'Time left 1:37.37'

#     g) "{1:3}".format("14")
#        '14'
#
# Q5. Explain why public key encryption is more useful for securing commmunications on the Internet than private (shared) key encryption.
#
# A5. Private keys must be known by both parties ahead of time. When contacting sites on the internet, say for e-commerce, there would be no practical way for the parties to exchange
#  the private key.
#
# Programming Exercises
#
# Q1. The example code files for Chapter 5 include a date conversion program, dateconvert2.py. This program could be
#     simplified with string formatting. Modify the program to use the string format method for its output.
#
# dateconvert2.py
# Converts day month and year numbers into two date formats
def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = "{0}/{1}/{2}".format(month,day,year)

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = "{0} {1}, {2}".format(monthStr, day, year)

    print("The date is {0} or {1}".format(date1, date2))

main()
#
# Q2. A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a
#     program that accepts a quiz score as an input and prints out the corresponding grade.
#
# Quiz grader

def main():
    print("Five point quiz grader")
    score = int(input("Enter the score: "))
    grade = "FFDCBA"[score]
    print("The grade is", grade)

main()
#
# Q3. A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#     Write a program that accepts an exam score as input and prints out the corresponding grade.
#
# c05ex03.py
# Exam grader
# A CS professor gives 100 point exams that are grade don the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F

def main():
    print("Exam Grader")
    score = int(input("Enter the score (out of 100): "))
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print(grades)
    print("The grade is", grades[score])

main()
#
# Q4. An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for "random access memory." 
#     Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the
#     phrase are not capitalized.
#
# c05ex04.py
def main():
    phrase = str(input("Enter the phrase you want an acronym for: "))
    acronym = ""
    for word in phrase.split():
        acronym = acronym + word[0]
    acronym = acronym.upper()

    print("The acronym is", acronym)

main()
#
# Q5. Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The value
#     of a name is determined by summing up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up to "z"
#     being 26. For example, the name "Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#     auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.
#
# A5. 
#
#c05ex05.py
# using indexing

def main():

    #name = raw_input("Enter your name in lower case letter")
    # another option to get a lower case namerh
    name = input("Enter your name: ").lower()

    # notice the space in front of 'a' this will give an index of a=1, b=2 and so on
    # also gives a space an index of zero, so it won't count
    letters = " abcdefghijklmnopqrstuvwxyz"

    value = 0
    for c in name:
        print(c, letters.find(c))  # test
        value = letters.find(c) + value
    print("The numeric value of your name is", value)
    
main()
#
#  Or an another good way to do it
#
# c05ex05.py
# Numerology of a single name
def main():
    print("This program computes the 'number value' of a name")
    print()

    name = input("Enter a single name: ")
    total = 0
    for letter in name:
        total = total + ord(letter.lower()) - ord('a') + 1 # print(ord('a')) shows you that a in ord terms is 97

    print("The value is:", total)
   

main()
#
# Question 6.Expand your solution to the previous problem to allow the calculation of a complete name such as "John Marvin Zelle" or "John Jacob Jingleheimer Smith." The 
# total value is just the sum of the numberic values of all the names.
#
# c05ex06.py
# Numerology of a full name


def main():
    print("This program computes the 'number value' of a name")
    print()

    names = input("Enter a name: ")

    # Create a string of all the letters -- avoids nested loop
    letters = "".join(names.split()) # https://www.programiz.com/python-programming/methods/string/join
    total = 0
    for letter in letters:
        total = total + ord(letter.lower()) - ord('a') + 1

    print("The value is:", total)

main()
#
# Q7. A Caesar cipher is a simple substitution sipher based on the idea of shifting each letter of the plaintext message a fixed number (called the key) of positions in the 
#     alphabet. For example, if the key is 2, the word "Sourpuss" would be encoded as "Uqwtrwuu." The original message can be recovered by "reencoding" it using the negative of
#     the key.
#
#     Write a program that can enconde and decode Caesar ciphers. The input to the program will be a string of plaintext and the value of the key. The output will be an encoded 
#     message where each character in the original message is replaced by shifting it key characters in the Unicode character set. For example, if ch is a character in the 
#     string and key is the amount to shift, then the character that replaces ch can be calculated as: chr(ord(ch) + key)
#
def main():
    print("This program encodes and decodes a caesar cipher")
    print()

    key = int(input("Enter the key value: "))
    plaintext = input("Enter some plain text: ")
    cipher = ""
    for letter in plaintext:
        cipher = cipher + chr(ord(letter) + key)
    print(cipher)
main()
#
# Q8. One problem with the previous exercise is that it does not deal with the case when we "drop off the end" of the alphabet. A true Caesar cipher does the shifting in a 
#     circular fashion where the next character after "z" is "a." Modify your solution to the previous problem to make it circular. You may assume that the input consists only 
#     of letters and spaces.
#     Hint: Make a string containing all the characters of your alphabet and use positions in this string as your code. You do not have to shift "z" int "a"; just make sure that
#     you use a circular shift over the entire sequence of characters in your alphabet string.
#
# c05ex08.py
# Caesar cipher (circular version)
def main():
    print("Caesar cipher")
    print()

    key = int(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    cipher = ""
    for letter in plain:
        pos = chars.find(letter)
        newpos = (pos + key)
        print(newpos) # me checking it works
        cipher = cipher + chars[newpos]

    print("Encoded message follows:")
    print(cipher)

main()
#
# Q9. Write a program that counts the number of words in a sentence entered by the user.
#
def main():
    sentence = str(input("Please enter your sentence here: ")) #Example: I shot the sheriff
    sentenceintowords = sentence.split() # example: ['I', 'shot', 'the', 'sheriff']
    print(sentenceintowords) # Put this in to see the output of splitting the sentence
    numberofwords = len(sentenceintowords)
    print("The number of words in the sentence,", sentence, "is", numberofwords)
main()
#
# Q10. Write a program that calculates the average word length in a sentence entered by the user.
#      Same as above, but also count length of each words, add up all the numbers, divide by number of words.
#
# c05ex10.py
# Get the average word count from an input phrase or sentence
def main():
    sentence = (input("Please enter your sentence here: ")) # Example: I shot the sheriff
    sentenceintowords = sentence.split() # Example: ['I', 'shot', 'the', 'sheriff']
    print(sentenceintowords) # Put this in to see the output of splitting the sentence
    numberofwords = len(sentenceintowords) # 4
    print("The number of words in the sentence,", sentence, "is", numberofwords)
    count = 0
    for word in sentence.split():
        count = count + len(word)

    averagewordlength = count / numberofwords
    print("The average word count of words in the sentence is: ", averagewordlength)

main()
#
# Q11. Write an improved version of the chaos.py program from Chapter 1 that allows a user to input two initial values and the number of of iterations, and then prints a nicely
#      formatted table showing how the values change over time. For example, if the starting values were .25 and .26 with 10 iterations, the table might look like this:
#
#     index    0.25         0.26
#     ----------------------------
#       1    0.731250     0.750360
#       2    0.766441     0.730547
#       3    0.698135     0.767707
#       4    0.821896     0.695499
#       5    0.570894     0.825942
#       6    0.955399     0.560671
#       7    0.166187     0.960644
#       8    0.540418     0.147447
#       9    0.968629     0.490255
#      10    0.118509     0.974630
#
# c05ex11.py
# Chaos program to print formatted side-by-side values

def main():
    print("This program illustrates a chaotic function")
    x1 = float(input("Enter the first seed between 0 and 1: "))
    x2 = float(input("Enter the second seed between 0 and 1: "))
    print()
    print("index     ", x1, "       ", x2)
    print("-------------------------------")
    for i in range(1, 11):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:2} {1:15.6f} {2:10.6f}".format(i, x1, x2))

main()
#
# Q12. Write an improved version of the futval.py program from Chapter 2.
#      Your program will prompt the user for the amount of the investment, the annualized interest rate, and the number of years of the investment. The program will then output a
#      nicely formatted table that tracks the value of the investment year by year. Your output might look something like this:
#
#     Year     Value
#     ----------------
#       0     $2000.00
#       1     $2200.00
#       2     $2420.00
#       3     $2662.00
#       4     $2928.20
#       5     $3221.02
#       6     $3542.12
#       7     $3897.43
#
# c05ex12.py
# Future value with formatted table.

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years: "))

    print("Year   Value")
    print("--------------")
    for i in range(years+1):
        print("{0:3}   ${1:7.2f}".format(i, principal))
        principal = principal * (1 + apr)

main()
#
# Q13. Redo any of the previous programming exercises to make them batch-oriented (using text files for input and output
#
# c05ex13.py
# Batch Caesar cipher
# Input file format: first line is key value; remaining lines are text to encode.

def main():
    print("Batch Caesar cipher")
    print()

    inName = input("Enter name of the input file: ")
    infile = open(inName,'r')
    key = int(infile.readline())

    outName = input("Enter name of output file: ")
    outfile = open(outName, 'w')
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    for line in infile:
        for letter in line[:-1]:
            pos = chars.find(letter)
            newpos = (pos + key) % len(chars)
            print(chars[newpos], file=outfile, end="")
        print(file=outfile)

    infile.close()
    outfile.close()
    print("Done")

main()
#
# Q14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." This program analyzes a file to determine the number of lines, words and characters 
#      contained therein. Write your own verison of wc. The program should accept a file name as input and then print three numbers showing the count of lines, words, and 
#      characters in the file.
#
# c05ex14.py
# Program to count lines, words and characters in a file.
# Note: Created a file at C:\Users\rhian\Dropbox\Python Course\Book course\Chapter 5 exercises\Chapter 5 Programming exercises\Question 14\rhiandetails.txt to enter as filename.

def main():
    print("File wordcount")
    print()

    fname = input("Enter filename: ")
    infile = open(fname, 'r')
    chars = infile.read()
    infile.close()
    
    words = chars.split()
    lines = chars.split("\n")

    print("Characters:", len(chars))
    print("Words:", len(words))
    print("Lines:", len(lines))

main()
#
# Q15. Write a program to plot a horizontal bar chart of student exam scores. Your program should get input from a file. The first line of the file contains the count of the 
#      number of students in the file, and each subsequent line contains a student's last name followed by a score in the range 0-100. Your program should draw a horizontal 
#      rectangle for each student where the length of the bar represents the student's score. The bars should all line up on their left-hand edges.
#
# Note: Page 158 for File Processing help
#
#     Hint: Use the number of students to determine the size of the window and its coordinates. 
#     Bonus: label the bars at the left with the students' names.
#
#co05ex15.py
# Student exam scores in a bar graph
#
# import graphics library
from graphics import *

# import dialog box for opening file
from tkinter.filedialog import *
def main():
    infileName = askopenfilename() # Get the file name

main()


