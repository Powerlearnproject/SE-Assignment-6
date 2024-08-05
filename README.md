[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15496736&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

1. Python Basics:
   - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.
ANSWER
Python is an open-source, high-level, general-purpose programming language known for its intuitive syntax, rich standard library and stong community support. It excels in data analysis, machine learning, and web development. Python's simplicity and versatility makes it a top choice for developers worldwide.


2. Installing Python:
   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.
ANSWER
1. Install Python:
Visit the official Python website.
Download the latest Python installer for Windows.
Run the installer and follow the prompts.
Make sure to check the box that says “Add Python X.Y to PATH” during installation (where X.Y represents the Python version).
2. Verify the Installation:
Open a Command Prompt or Windows PowerShell.
Type the following command and press Enter:
python --version
If you see a version of Python (e.g., Python 3.9.2), it means Python is installed successfully.
3. Create a Virtual Environment:
Open Command Prompt or PowerShell.
Navigate to the directory where you want to create your project.
Run the following command to create a virtual environment (replace <name_of_project> with your desired project name):
python -m venv <name_of_project>
Activate the virtual environment:
For Command Prompt:
<name_of_project>\Scripts\activate
4. Deactivate the Virtual Environment:
When you’re done working in the virtual environment, run:
deactivate
https://medium.com/thesecmaster/step-by-step-procedure-to-install-python-on-windows-612f16b5ace6     

4. Python Syntax and Semantics:
   - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.
ANSWER
print("Hello, World!")
print(): This is a built-in Python function used to display text or values. It outputs the specified content to the console.
"Hello, World!": This is a string literal enclosed in double quotes. Strings represent text and can contain letters, numbers, or special characters.
print("Hello, World!"): The entire line is a statement. It calls the print() function with the string argument "Hello, World!".
When you run this program, it will display “Hello, World!” in the console.


5. Data Types and Variables:
   - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.
ANSWER
Integers (int):
Represent whole numbers (positive, negative, or zero).
Example: age = 25
Floating-Point Numbers (float):
Represent decimal numbers with fractional parts.
Example: pi = 3.14
Complex Numbers (complex):
Represent numbers with both real and imaginary parts.
Example: z = 2 + 3j
Strings (str):
Represent text or character sequences.
Example: name = "Alice"
Booleans (bool):
Represent True or False values.
Example: is_student = True
# Creating variables of different data types
age = 25
pi = 3.14
name = "Alice"
is_student = True

# Printing the values
print("Name:", name)
print("Age:", age)
print("Pi:", pi)
print("Is Student?", is_student)
https://python.land/python-data-types


6. Control Structures:
   - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.
ANSWER
Conditional statements allow you to make decisions in your code based on certain parameters and also facilitate in controlling the flow of code execution.
if...else Statement:
The if...else statement allows you to execute different code blocks based on whether a condition is true or false.
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
for Loop:
A for loop iterates over a sequence (e.g., a list, tuple, string, or range) and executes a set of statements for each item.
for variable in iterable:
    # Code to execute for each item


7. Functions in Python:
   - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.
ANSWER
Functions are essential building blocsk that allow us to organize and reuse code efficiently. They provide a way to encapsulate a set of instructions, perform specific tasks, and return results.
def add_numbers(a,b):
    return a+b
result = add_numbers(5, 3)
print(f"The sum is: {result}")
 https://www.freecodecamp.org/news/python-function-guide-with-examples/
    

8. Lists and Dictionaries:
   - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.
 ANSWER
Lists:
Lists are ordered collections of elements.
Elements in a list can be of different data types (e.g., integers, strings, objects).
Lists are mutable (you can modify their contents after creation).
Access elements using indices (starting from 0).
Example:
# Creating a list
my_list = [10, 20, 30, 'hello']

# Accessing elements
print(my_list[0])  # Output: 10
print(my_list[3])  # Output: 'hello'
Dictionaries:
Dictionaries store data as key-value pairs.
Keys must be unique and immutable (e.g., strings, integers).
Values can be of any data type.
Dictionaries are unordered (no specific order of elements).
Example:
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}

# Accessing values using keys
print(my_dict['name'])  # Output: 'Alice'
print(my_dict['age'])   # Output: 25
Demonstration:
# Create a list of numbers
my_list = [1, 2, 3, 4, 5]

# Create a dictionary with key-value pairs
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}

# Accessing elements
print("List element at index 2:", my_list[2])  # Output: 3
print("Value for 'banana' in dictionary:", my_dict['banana'])  # Output: 2

# Modifying elements
my_list[3] = 10
my_dict['cherry'] = 7

# Adding new elements
my_list.append(6)
my_dict['grape'] = 4

# Removing elements
del my_list[1]
my_dict.pop('apple')

# Display updated lists and dictionaries
print("Updated list:", my_list)  # Output: [1, 3, 10, 5, 6]
print("Updated dictionary:", my_dict)  # Output: {'banana': 2, 'cherry': 7, 'grape': 4}
https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/


9. Exception Handling:
   - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.
ANSWER
Exception handling in python allows one to gracefully handle errors that might occur during program execution.
The try block contains code that might raise an exception.
The except block catches specific exceptions and handles them.
The finally block executes regardless of whether an exception occurred or not.
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"Result: {result:.2f}")
    finally:
        print("Execution completed.")

# Example usage
divide(10, 2)  # Output: Result: 5.00 \n Execution completed.
divide(10, 0)  # Output: Error: Division by zero! \n Execution completed.
In this example:
The try block attempts division.
If a ZeroDivisionError occurs, the except block handles it.
The else block executes if no exception occurs.
The finally block always runs, even after an exception.
https://www.programiz.com/python-programming/exception-handling
https://www.geeksforgeeks.org/python-exception-handling/


10. Modules and Packages:
   - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.
ANSWER
A module in Python is a single file containing python code that allows for logical organization and reuse in other programs. It can include functions, classe and variables.
A package is a collection of related modules organized in a directory hierarchy. It helps manage larger projects by grouping related funtionality together.
Importing a Module:
To use a module in your script, you import it using the import statement.
Example:

import math  # Import the math module
The math module provides various mathematical functions and constants.
Example:
import math

# Calculate the square root
num = 25
sqrt_result = math.sqrt(num)
print(f"Square root of {num} is {sqrt_result:.2f}")

# Calculate the value of pi
print(f"Value of pi: {math.pi:.4f}")
Output:
Square root of 25 is 5.00
Value of pi: 3.1416
In this example, we import the math module and use its functions to find the square root and the value of pi.


11. File I/O:
    - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.
ANSWER.
To read from a file, follow these steps:
Open the file using the open() function with the appropriate mode (e.g., 'r' for read).
Read the content using methods like read(), readline(), or readlines().
Close the file using close() to free up system resources.
# Open a text file for reading
file_path = "example.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)

To write to a file, follow these steps:
Open the file using the open() function with the appropriate mode (e.g., 'w' for write).
Write data using methods like write() or writelines().
Close the file.
# Create a list of strings
my_strings = ["Hello, world!", "Python is awesome.", "Goodbye!"]

# Open a text file for writing
output_file = "output.txt"
with open(output_file, "w") as file:
    for string in my_strings:
        file.write(string + "\n")  # Add a newline after each string

print(f"Strings written to {output_file}")


    
# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


