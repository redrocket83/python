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
