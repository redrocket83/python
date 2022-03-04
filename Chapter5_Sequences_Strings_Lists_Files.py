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
# Q3
