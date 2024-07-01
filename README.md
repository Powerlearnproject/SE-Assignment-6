[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15356993&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

1. Python Basics:
   - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.
   __Python is a versatile, high-level programming language known for simplicity, readability, and extensive libraries. It excels in web development, data science, machine learning, automation, and scientific computing. Its clear syntax, support for multiple paradigms, and broad community make it a top choice for developers.__

2. Installing Python:
   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.
   To install Python:
   1. Download the installer from python.org.
   2. Run the installer, selecting "Add Python to PATH" option.
   3. Open a terminal (cmd/PowerShell on Windows, Terminal on macOS/Linux).
   4. Verify installation with `python --version`.
   5. Install virtualenv with `pip install virtualenv`.
   6. Create a virtual environment: `virtualenv myenv`.
   7. Activate it: `source myenv/bin/activate` (macOS/Linux) or `myenv\Scripts\activate` (Windows).

3. Python Syntax and Semantics:
   - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.
   
```python
print("Hello, World!")
```
- **Print Statement (`print("Hello, World!")`)**: The `print()` function in Python is used to output text or variables to the console. Here, `"Hello, World!"` is enclosed in double quotes to denote a string literal, which is what `print()` outputs.

4. Data Types and Variables:
   - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.
   __Python's basic data types include `int` (integers), `float` (floating-point numbers), `str` (strings), `bool` (booleans), `list` (mutable ordered collections), `tuple` (immutable ordered collections), and `dict` (key-value mappings). Variables are declared with simple assignment (`=`) and can be inspected using `type()` to determine their data type.__

5. Control Structures:
   - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.
__1. **Conditional Statements (`if-else`)**: Used to execute code based on conditions.

   Example:
   ```python
   x = 10
   if x > 0:
       print("x is positive")
   else:
       print("x is non-positive")
   ```

2. **Loops**:
   - **`for` Loop**: Iterates over a sequence (e.g., list, tuple) or other iterable objects.

     Example:
     ```python
     numbers = [1, 2, 3, 4, 5]
     sum = 0
     for num in numbers:
         sum += num
     print("Sum:", sum)
     ```
     __

6. Functions in Python:
   - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.
   __Functions in Python are reusable blocks of code that perform specific tasks. They enhance code readability, modularity, and reusability by encapsulating logic. Example function:

```python
# Function to compute sum of two numbers
def sum_numbers(a, b):
    return a + b

# Example of calling the function
result = sum_numbers(3, 5)
print("Sum:", result)
```
.__

7. Lists and Dictionaries:
   - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.

   In Python, lists are ordered collections of items accessed by index, mutable and defined with square brackets `[ ]`. Dictionaries are unordered collections of key-value pairs, accessed by keys, mutable and defined with curly braces `{ }`. Example script:

```python
# Creating a list and a dictionary
numbers = [1, 2, 3, 4, 5]
person = {'name': 'Alice', 'age': 30}

# Basic operations
print(numbers[0])  # Accessing list item
print(person['name'])  # Accessing dictionary value
numbers.append(6)  # Modifying list
person['city'] = 'New York'  # Modifying dictionary

# Output: 1, Alice
```

8. Exception Handling:
   - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.

   Exception handling in Python helps manage errors gracefully. It uses `try` to attempt risky operations and `except` to handle errors if they occur. For instance, dividing by zero triggers a `ZeroDivisionError`. The `finally` block, if used, ensures cleanup tasks run regardless of errors. This approach enhances program reliability by preventing crashes and allowing controlled responses to unexpected situations.

9. Modules and Packages:
   - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.

In Python, **modules** are files containing Python definitions and statements. They allow you to organize code into reusable units. **Packages** are directories containing multiple modules and an `__init__.py` file, indicating it's a package.

To import and use a module (e.g., `math`):

1. **Importing a Module**: Use `import module_name` to make its functions and variables accessible.
   
2. **Using Functions from the Module**: Call functions like `module_name.function()`.

Example with the `math` module:

```python
# Example using the math module
import math

# Using functions from the math module
print(math.sqrt(25))  # Computes square root
print(math.pi)  # Accesses the value of pi
```


10. File I/O:
    - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.

    In Python, file operations involve using `open()` to read or write files. Reading uses `file.read()` to fetch content, while writing uses `file.write()` or `file.writelines()` to save data. Context managers (`with open(...) as file:`) ensure proper file handling by automatically closing files. These operations simplify managing file content for various applications in Python programming.

# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


