#python introduction

 python is high-level programming language for general-purpose programming.
And it is open source, interpreted, object-oriented programming language.
Python was created by Dutch progrmmer, Guido Van Rossun.


Why i choose Python 
It is a programming language which is close to human languageand because of that, it is easy to learn and use. 
Python is used by variuse industries and companies.



Python Shell
Python is an interpreted scripting language, so it does not need to be compiled.
It means it executes the code line by line.
it si use to execute a single python command and get the result

I learnt that, python shell waits for the python code from the user. Whent you enter the code ,
it interprets the code and shows the result in the next line.


Installing Visual Studio Code
Download vs code (visual stutio code) install it,  if you install it.
Then open the visual Studio code by double cliking the Visual Studio code icon.
When you open it you will get the interface . Try to interact with the labeled icons

Then create a folder what ever name you want to call it on your system or desktop. then open the visual studio code and follow it step by step.

Basic Python

1. Python Syntax
A python syntax is the rules that defines how a python program is written and interpreted.

A python script can be written in python interactive shell or in the code editor,A python file has an extension .py.

2. Python Indentation
Python Indentation refers to the blank spaces at the beginning of a line of code.
An indentation is the white space in a text. indentation in many languages is used to increase code readability: however python use indentation to create blocks of code. 

3. Commente
Comment is text in our code that python completly ignores.
Comments play a crusial role in enhancing code readability and allowing developers to level notes within their code. In python, any text preceded by a hash (#) symbol is a considered as a comment.and will not be executed.

Examle: single line comment 

    # This is the first comment
    # This is the second comment
    # Python is eating the world

Example: Multiline Comment

Triple quote can be used for multiline comment if it is not assigned to a variable

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""


Data types:

Data types defines the kind of value a variable holds.
And they several types of data type in python. 
let's get started with the most common ones 

1. Number 
. Integer:Integer(negative, zero and positive) numbers Example: -3, -2, -1, 0, 1, 2, 3...
. Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5..... 
. Complex Example 1 + j, 2 + 4j

2. String
A string is a collection of one or more character under a single or double quote. if a string is more than one sentence then use a triple quote.

Example:

'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'

3. Booleans
A boolean data type is either True or False value. T and F should be always uppercase.

Example:

    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False

4. List 
A list is use to store multiple items in a single variable.

Example:

[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float.

5. Dictionary
Dictionary is use to store data in key:value pairs.

Example:

{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland',
'age':250,
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}


Tuple
Tuple is a collection of items that is ordered and unchangeable.

Example:

('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets.

Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

Example:

{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set.


Checking Data types
We use the (type()) to check data type of certain data/variable.