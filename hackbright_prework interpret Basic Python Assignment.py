'''
                          Reading and Exercises 
    Exercise 1  - Write a well-structured English sentence with invalid tokens
in it. Then write another sentence with all valid tokens but with
invalid structure.
'''
Invalid tokens, valid structure: Mickey asked 46345 to mn345554w
Vaild tokens, invalid structure: said lilly now to go


# Exercise 4  - Start the Python interpreter and use it as a calculator. Python’s syntax for math operations is almost the same as standard mathematical notation. For example, the symbols +, - and / denote addition, subtraction and division, as you would expect. The symbol for multiplication is *.
# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).


>>> 10/1.61 #converts kilometers to miles
6.211180124223602
>>> (43 * 60) + 30 # converts time to seconds
2610
>>> 2610 / 6.211180124223602 #computes average time in seconds per mile
420.21000000000004
>>> 420.21000000000004/60 #computes average time in minutes per mile
7.003500000000001
>>> 60/7.003500000000001 #average speed in miles per hour
8.567144998929106
>>>
'''
Exercise 1  
Type the following statements in the Python interpreter to see what they do:
5
x = 5
x + 1
'''

print 5
x = 5
print(x)
x = x + 1
print (x)

"""
Exercise 2  
Assume that we execute the following assignment statements:
""" 

width = 17
height = 12.0
delimiter = '.'

"""
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
"""
>>> type(width)
<class 'int'>
>>> type(height)
<class 'float'>
>>> type(delimiter)
<class 'str'>
>>> width/2
8.5
>>> width/2.0
8.5
>>> height/3
4.0
>>> 1 + 2 * 5
11
>>> delimiter * 5
'.....'
>>> 
#Exercise 3  
# Practice using the Python interpreter as a calculator:
# 3.1 The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!

volume = (4.0/3) * 3.14 * (5**3)
print volume # 523.333333333

''' 3.2 Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?
'''

print (24.95*0.6)*60 + 3 + (0.75*59)   #945.45

''' 3.3 If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
'''

time = 7.2 * 3 + 8.25 * 2 # 38.1 mins 
 6:30am + 38.1 minutes = ~7:30am 
 
 
 
 # 3. Think Like A Computer Scientist: Strings

''' Exercises
Exercise 1
Write a function that takes a string as an argument and displays the letters backward, one per line.
'''
fruit = "Apple"
backword = len(fruit) - 1
while backword>=0:
    letters = fruit[backword]
    print letters
    backword = backword -1
    
    '''
    for prefix and suffix from String
    '''
    prefixes = "JKLMNOPQ"
    suffix ="ack"
    for letter in prefixes:
        if letter in ('O', 'Q'):  # if the letter is O or Q
            print (letter + 'u' + suffix)
        else:
            print (letter + suffix)
           
           
# Exercise 3  - Given that fruit is a string, what does fruit[:] mean?
 It returns a copy of the string, from the 0th index to the last 

''' Exercise 4  - Modify find so that it has a third parameter, the index in word where it should start
looking.'''

def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find("welcome", "e", 3) 


# Exercise 5  - Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(string, letter):
    count = 0
    for c in string:
        if letter == c:
            count +=1 
    return count 

print count("hello", "l")

# Exercise 6  - Rewrite this function so that instead of traversing the string, it uses the three-parameter version of find from the previous section.

def count2(string, letter, index=0):
    count=0 
    while index < len(string):
        if string[index] == letter:
            count += 1 
            index += 1
        else: 
            index += 1
    return count 

''' Exercise 7  - There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of as in 'banana'.
'''

print "banana".count("a")

# Exercise 8   - Read the documentation of the string methods at http://docs.python.org/2/library/stdtypes.html#string-methods. You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# Exercise 9  Starting with this diagram, execute the program on paper, changing the values of i and j during each iteration. Find and fix the second error in this function.

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1

    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

print is_reverse("pots", "stop")

# Exercise 10 - Use this idiom to write a one-line version of is_palindrome from Exercise 6.

def is_palindrome(word):
    return word == word[::-1]
    
'''Exercise 11  The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).'''

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False   #wrong 
            
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'   # wrong - returns true, checks if 'c' is lowercase but does not check the letters in the input s

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag     #wrong- returns the last character 

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag    # Correct 

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True    # wrong

# Exercise 12   -
'''ROT13 is a weak form of encryption that involves “rotating” each letter in a word by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.
Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount. For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.'''


    
'''1) Handle User Input
Asks a user to fill in some information about themselves (using raw_input() to gather the information and assign it to variables). Use string formatting (from PyFormat), raw_input() and variable assignment that you learned from this section’s readings.

We’d like your file to ask and store the user’s answers to the following questions:

“What’s your first name?”
“What’s your last name?”
“What’s your favorite color?”
“How many pets do you have?”
And then have it print a greeting that includes those values once they are collected.

'''

#Ask for user's first name
firstName = raw_input("What is your first name? ")
lastName = raw_input("What is your last name? ")
color = raw_input("What is your favorite color? ")
pets = raw_input("How many pets you have? ")

print "Great! So your name is %s %s, " \
"and your favorite color is\n %s and you have %s pets. Nice to meet you!" % (firstName,lastName,color,pets)
      
    
    
    ''' 2) Formatting text
Copy the following line of python into your repl.it session.


paragraph = """An invitation to dinner was soon afterwards dispatched;
and already had Mrs. Bennet planned the courses that were to do credit
to her housekeeping, when an answer arrived which deferred it all. Mr.
Bingley was obliged to be in town the following day, and, consequently,
unable to accept the honour of their invitation, etc. Mrs. Bennet was
quite disconcerted."""


    average_rating=4.56789123
    print('{:.10}{:.3}'.format(paragraph , "..." ))
    print('{:.3}'.format(average_rating))

     
     3) Discussion Question
Using Python comment syntax (prepend the line with a #) at the bottom of your repl.it session answer the following question:

Why is the following Python invalid?

first_name = "Sally"
first_name[0] = "C"
'''
It's invalid because string is immutable in Python. Therefore, string object can't be changed.
      
 #embddes link   

<iframe height="400px" width="100%" src="https://repl.it/@ayeshasultana/hackbrightprework1py?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



            

