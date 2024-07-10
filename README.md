[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15396610&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

1. Python Basics:
   - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.
 Python is a high-level, general-purpose programming language known for its:
Readability: Its syntax is clear and concise, resembling natural language, making it easier to learn and understand.
Versatility: Python can be used for various tasks, including web development, data analysis, machine learning, scripting, and automation.
Large Standard Library: Python comes with a vast collection of built-in modules and libraries for common functionalities.
Large Community and Resources: Python has a large and active community, providing extensive documentation, tutorials, and support.

Use Cases:
Web Development: Frameworks like Django and Flask make Python popular for building web applications.
Data Science and Machine Learning: Libraries like NumPy, pandas, and scikit-learn empower data analysis and machine learning tasks.
Scripting and Automation: Python excels in automating repetitive tasks and system administration.
Scientific Computing: Libraries like SciPy and Matplotlib are valuable tools for scientific computing and data visualization.


2. Installing Python:
   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.
MACOs:
Download the latest installer from https://www.python.org/downloads/.
Run the installer and follow the on-screen instructions.
Check installation by opening a command prompt and typing python --version.
Consider using virtual environments (venv) to isolate project dependencies:
Open a command prompt and navigate to your project directory.
Run python -m venv my_venv (replace my_venv with your desired name).
Activate the virtual environment: my_venv\Scripts\activate.bat (adjust path based on your OS).

3. Python Syntax and Semantics:
   - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.
print("Hello, World!")

Explanation:
print(): A built-in function that displays output on the console.
"Hello, World!": A string literal enclosed in double quotes, representing the text to be printed.

4. Data Types and Variables:
   - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.
Basic Data Types:

int: Integer numbers (e.g., 42, -100).
float: Floating-point numbers (e.g., 3.14, -2.5).
str: String of characters (e.g., "This is a string").
bool: Boolean values (True or False).

my_number = 10
pi = 3.14159
greeting = "Hello"
is_running = True

print(f"my_number (int): {my_number}")
print(f"pi (float): {pi}")
print(f"greeting (str): {greeting}")
print(f"is_running (bool): {is_running}")


5. Control Structures:
   - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.
if-else: Executes code based on a condition.

age = 25
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


for: Iterates a block of code a specific number of times or over a sequence of items.

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}.")


6. Functions in Python:
   - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.

Functions are reusable blocks of code that perform specific tasks.

def add_numbers(x, y):
  """This function adds two numbers and returns the sum."""
  return x + y

# Call the function
result = add_numbers(5, 3)
print(f"The sum is: {result}")



7. Lists and Dictionaries:
   - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.
  
Lists:  Ordered, mutable collections of items.
Dictionaries: Unordered collections of key-value pairs.


numbers = [1, 2, 3, 4, 5]
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}


8. Exception Handling:
   - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.
   Exception handling allows us to gracefully manage errors that might occur during program execution.

try:
   result = 10 / 0
except ZeroDivisionError:
  print("Error: Division by zero")
finally:
  
  print("This block always executes.")


9. Modules and Packages:
   - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.
Modules:  Reusable Python code files containing functions, variables, and classes.Packages:  Hierarchical collections of modules organized into directories.

import math  
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")



11. File I/O:
    - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.
   
Reading from a File:

with open("data.txt", "r") as file:
  contents = file.read()
  print(contents)

with open("data.txt", "r") as file:
  for line in file:
    print(line.strip()) 
Writing to a File:
with open("output.txt", "w") as file:
  file.write("This is some text written to the file.")

with open("output.txt", "a") as file:
  file.write("\nMore text appended.")

# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


