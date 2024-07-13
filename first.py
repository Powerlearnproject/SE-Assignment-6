# print is a built-in function in Python used to output text to the console.

# Parentheses() are used to enclose the arguments passed to the function. In this case, the argument is "Hello, World!"

# "Hello, World!" is a string literal. In Python, strings are enclosed in either single quotes (') or double quotes (").

print("Hello, World!")

# Integers (int): Whole numbers, positive or negative, without decimals.
myAge = 23

# Floating-Point Numbers (float): Numbers with a decimal point. 
r = 3.14

# Strings (str): Sequence of characters enclosed in single or double quotes. 
greetings = "Hey"

# Lists (list): Ordered, mutable collection of items, enclosed in square brackets.
animals = ["Dog", "Cat", "Lion"]

# Tuples (tuple): Ordered, immutable collection of items, enclosed in parentheses.
fruits = ("Apple", "Orange", "Apple")

#Dictionaries (dict): Unordered, mutable collection of key-value pairs, enclosed in curly braces.
students_details = {"name": "Ann", "age": 23}

#Sets (set): Unordered collection of unique items, enclosed in curly braces.
prices = (4, 6, 9, 3)

# Booleans (bool): Logical values representing True or False.
isTasty = True

# Conditional statements in Python are used to execute a block of code based on whether a condition is true or false.

# if Statement: Executes a block of code if the condition is true.
# elif Statement: (short for "else if") Checks another condition if the previous if or elif condition was false.
# else Statement: Executes a block of code if none of the preceding conditions were true.

age = 18

if age < 18:
    print("You are not eligible to be a voter.")
elif age == 18:
    print("You are eligible to be a voter.")
else:
    print("You are an adult.")

# Loops in Python are used to execute a block of code repeatedly, either for a specified number of times or until a condition is met.

# for Loop: Iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.
fruits = ["Orange", "Pineapple", "Lemon"]

for fruit in fruits:
    print(fruit)
    
# while Loop: Repeats a block of code as long as a condition is true.
num = 0

while num < 5:
    print("Count is:", num)
    num += 1


# Functions are reusable blocks of code that perform a specific task. They allow you to structure your code more efficiently, making it easier to manage, debug, and understand. Functions help in avoiding code repetition and enhance modularity and readability.

# Useful of functions
# Code Reusability: Functions allow you to write code once and reuse it multiple times.
# Modularity: Functions help break down complex problems into smaller, manageable tasks.
# Readability: Functions make the code more readable and easier to understand.
# Maintainability: Functions simplify the process of updating and maintaining code.

# Defining the function
def add_numbers(m, n):
    """
    This function takes two arguments and returns their sum.
    """
    return m + n

# Calling the function
ans = add_numbers(5, 3)
print("The sum is:", ans)


# Lists
#Ordered: Elements in a list have a defined order.
#Indexed: Each element is accessible via its index.
#Mutable: Elements can be changed, added, or removed.
#Duplicates Allowed: Lists can contain duplicate elements.
#Syntax: Defined using square brackets [].

my_nums = [1, 2, 3, 4, 5]

# Dictionaries
# Unordered: Elements do not have a defined order.
# Key-Value Pairs: Each element is stored as a key-value pair.
# Mutable: Keys and values can be changed, added, or removed.
# Unique Keys: Keys must be unique; values can be duplicated.
# Syntax: Defined using curly braces {}.

my_dictionary = {"name": "Alice", "age": 25, "city": "New York"}

# script
# Creating a list of numbers
number = [1, 2, 3, 4, 5]

# Cre_numting a dictionary with key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}

# Basic operations on lists
# Adding an element to the list
number.append(6)
print("List after adding an element:", num)

# Removing an element from the list
number.remove(3)
print("List after removing an element:", number)

# Accessing an element by index
print("Element at index 2:", number[2])

# Basic operations on dictionaries
# Adding a key-value pair
person["email"] = "alice@example.com"
print("Dictionary after adding a key-value pair:", person)

# Removing a key-value pair
del person["city"]
print("Dictionary after removing a key-value pair:", person)

# Accessing a value by key
print("Value for key 'name':", person["name"])

# Looping through lists
print("Looping through the list:")
for numb in number:
    print(numb)

# Looping through dictionaries
print("Looping through the dictionary:")
for key, value in person.items():
    print(key, ":", value)
    

# Exception handling in Python is a mechanism that allows you to manage and respond to runtime errors or exceptional conditions in your code. This ensures that your program can handle unexpected situations gracefully without crashing.

# try Block: Contains the code that might raise an exception.
# except Block: Contains the code that executes if an exception occurs in the try block.
# finally Block: Contains the code that executes regardless of whether an exception occurs or not. This block is optional.

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        result = None
    except TypeError:
        print("Error: Invalid input type!")
        result = None
    else:
        print("Division successful!")
    finally:
        print("Execution of the try-except block is complete.")
    
    return result

# Example usage
num1 = 10
num2 = 0

print(f"Dividing {num1} by {num2}:")
division_result = divide_numbers(num1, num2)
print("Result:", division_result)

num1 = 10
num2 = 2

print(f"\nDividing {num1} by {num2}:")
division_result = divide_numbers(num1, num2)
print("Result:", division_result)

num1 = "10"
num2 = 2

print(f"\nDividing {num1} by {num2}:")
division_result = divide_numbers(num1, num2)
print("Result:", division_result)

# Modules
# A module is a single file (or files) that are imported under one import and used. A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. It also allows you to reuse the code across multiple programs.

# Packages
# A package is a way of organizing related modules into a directory hierarchy. Packages allow for a hierarchical structuring of the module namespace using dot notation. A package is a collection of modules in directories that give a package hierarchy.

import math

# Using the sqrt function from the math module
res = math.sqrt(225)
print("The square root of 16 is:", res)

# File I/O in Python
# File I/O (Input/Output) in Python involves reading data from and writing data to files. This can be done using built-in functions and methods.

# Reading from a File
# To read from a file in Python, you can use the open() function in combination with methods like read(), readline(), or readlines().
# Reading the content of a file and printing it to the console

