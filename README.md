[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15359347&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

Python Basics:
Python is a high-level, interpreted programming language known for its simplicity and readability. Some key features include easy learning curve, versatility, a large standard library, and strong community support. It's used extensively in web development, data analysis, machine learning, and automation.

Installing Python:

Windows:
Download Python installer from python.org.
Run the installer, check "Add Python to PATH" option.
Verify installation: Open Command Prompt, type python --version.
Set up virtual environment:
Copy code
python -m venv myenv
myenv\Scripts\activate
macOS/Linux:
Python often comes pre-installed.
Use package manager (e.g., Homebrew, apt-get) to install if not available.
Verify installation: Terminal, python3 --version.
Set up virtual environment:
bash
Copy code
python3 -m venv myenv
source myenv/bin/activate
Python Syntax and Semantics:

python
Copy code
# Hello World program
print("Hello, World!")
print() function: Outputs text to the console.
"Hello, World!": String enclosed in double quotes.
Data Types and Variables:

Basic data types: int, float, complex, str, bool, list, tuple, set, dict.
python
Copy code
# Variable examples
num = 10              # int
pi = 3.14             # float
name = "Kevin"        # str
is_valid = True       # bool
my_list = [1, 2, 3]   # list
Control Structures:

Conditional statements:
python
Copy code
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
Loops:
python
Copy code
# For loop example
for i in range(1, 5):
    print(i)
Functions in Python:

Functions are reusable blocks of code. Example:
python
Copy code
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)  # Output: Sum: 8
Lists and Dictionaries:

Lists: Ordered collection of items.
python
Copy code
numbers = [1, 2, 3, 4, 5]
Dictionaries: Key-value pairs.
python
Copy code
person = {"name": "Kevin", "age": 25, "city": "Nairobi"}
Exception Handling:

Used to handle errors gracefully.
python
Copy code
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
Modules and Packages:

Modules: Python files containing functions and variables.
Packages: Directory of modules.
python
Copy code
import math
print("Square root of 16:", math.sqrt(16))
File I/O:

Reading from a file:
python
Copy code
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
Writing to a file:
python
Copy code
data = ["Apple", "Banana", "Orange"]
with open("fruits.txt", "w") as file:
    for fruit in data:
        file.write(fruit + "\n")

# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


