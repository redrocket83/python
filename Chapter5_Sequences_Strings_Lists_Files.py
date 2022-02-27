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
