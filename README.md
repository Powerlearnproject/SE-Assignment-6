[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15377019&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

# My Answers

## Introduction to Python
### Python Basics
#### What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.

 - Python is a high-level, interpreted programming language known for its simplicity and readability. Key features include:

     - Readable and Simple Syntax: Easy-to-read code that resembles English language.
     - Versatility: Suitable for various applications including web development, data analysis, artificial intelligence, and more.
     - Large Standard Library: Comprehensive library for different tasks.
     - Interpreted: No compilation needed, making development faster.
- Use Cases:

     - Web Development: Django and Flask frameworks.
     - Data Analysis: Pandas library.
     - Machine Learning: TensorFlow and PyTorch.
     - Automation: Scripting and task automation.
       
### Installing Python
#### Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.

- Installation Steps:
    - Windows:
     - Download Python installer from python.org.
     - Run installer, ensure "Add Python to PATH" is checked.
   - macOS:
     - Install Homebrew if not installed.
     - Use terminal command: brew install python.
  - Linux (Ubuntu):
     - Use package manager: sudo apt-get install python3.
     - Verify Installation:
     - Open terminal or command prompt.
     - Type python --version or python3 --version.
     - Ensure Python version is displayed.
     - Setting Up Virtual Environment:
     - Install virtualenv using pip: pip install virtualenv.
     - Create virtual environment: virtualenv venv.
     - Activate virtual environment:
     - Windows: venv\Scripts\activate
     - macOS/Linux: source venv/bin/activate
       
### Python Syntax and Semantics
#### Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.

 - print("Hello, World!")
 - Function Call: print() function outputs text to console.
   
### Data Types and Variables
#### List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.

 - Basic Data Types: Integer (int), Float (float), String (str), Boolean (bool), List (list), Tuple (tuple), Dictionary (dict).
  - Integer
     - num1 = 10
  - Float
     - num2 = 3.14
  - String
     - name = "Alice"
  - Boolean
     - is_true = True
  - List
     - my_list = [1, 2, 3]
  - Tuple
     - my_tuple = (4, 5, 6)
  - Dictionary
     - my_dict = {"a": 1, "b": 2}

      - print(num1, num2, name, is_true, my_list, my_tuple, my_dict)
   
### Control Structures
#### Explain the use of conditional statements and loops in Python. Provide examples of an if-else statement and a for loop.

  - Conditional Statement (if-else):
     - num = 10

     - if num > 0:
        -  print("Positive")
     - elif num < 0:
        -  print("Negative")
     - else:
         - print("Zero")
     - For Loop:
       - for i in range(5):
          - print(i)

### Functions in Python
#### What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.
 - Functions: Reusable blocks of code that perform specific tasks.

- Function definition
     - def add_numbers(a, b):
         - return a + b

-  Calling the function
     - result = add_numbers(3, 5)
     - print("Sum:", result)  # Output: Sum: 8

### Lists and Dictionaries
#### Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.

 - Lists: Ordered collection of items.
 - Dictionaries: Unordered collection of key-value pairs.
    - List of numbers
     - numbers = [1, 2, 3, 4, 5]

    - Dictionary
     - my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}

  -  Accessing elements
     - print(numbers[0])  # Output: 1
     - print(my_dict["name"])  # Output: Alice

 - Adding elements
     - numbers.append(6)
     - my_dict["email"] = "name@example.com"

     - print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
     - print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Wonderland', 'email': 'name@example.com'}

### Exception Handling
#### What is exception handling in Python? Provide an example of how to use try, except, and finally blocks to handle errors in a Python script.
 - Exception Handling: Managing and responding to errors during execution.

  - try:
         - num = int(input("Enter a number: "))
         - result = 10 / num
         - print("Result:", result)
 - except ZeroDivisionError:
         - print("Error: Cannot divide by zero.")
 - except ValueError:
         - print("Error: Invalid input. Please enter a number.")
 - finally:
         - print("Execution complete.")

### Modules and Packages
#### Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the math module.

  - Modules: Python files containing functions, classes, and variables.
  - Packages: Collection of related modules.
- math_module.py
- Importing math module
 - import math

 - Using functions from math module
     - print("Square root of 16:", math.sqrt(16))  # Output: Square root of 16: 4.0
### File I/O
#### How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.
   - Reading from a file
   - with open("example.txt", "r") as file:
         - content = file.read()
         - print(content)
 - Writing to a file
- my_list = ["apple", "banana", "cherry"]

- with open("fruits.txt", "w") as file:
    - for fruit in my_list:
        - file.write(fruit + "\n")
        - 
# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


