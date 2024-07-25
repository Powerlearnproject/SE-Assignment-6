[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15464404&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

## Questions:

1. **Python Basics**:
   - **What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.**
     - Python is a high-level, interpreted programming language known for its simplicity and readability. Key features include its easy-to-understand syntax, dynamic typing, and extensive standard library. Python is popular for web development, data analysis, artificial intelligence, scientific computing, and automation. Examples of use cases include web applications with Django or Flask, data analysis with Pandas, and machine learning with TensorFlow or Scikit-learn.

2. **Installing Python**:
   - **Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.**
     - **Windows**:
       1. Download the installer from the [Python website](https://www.python.org/downloads/).
       2. Run the installer and check "Add Python to PATH."
       3. Follow the installation steps.
       4. Verify installation with `python --version` in Command Prompt.
       5. Create a virtual environment with `python -m venv myenv` and activate it using `myenv\Scripts\activate`.
     - **macOS**:
       1. Install Homebrew if not already installed.
       2. Run `brew install python`.
       3. Verify installation with `python3 --version`.
       4. Create a virtual environment with `python3 -m venv myenv` and activate it using `source myenv/bin/activate`.
     - **Linux**:
       1. Use your package manager (e.g., `sudo apt-get install python3` for Debian-based systems).
       2. Verify installation with `python3 --version`.
       3. Create a virtual environment with `python3 -m venv myenv` and activate it using `source myenv/bin/activate`.

3. **Python Syntax and Semantics**:
   - **Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.**
     ```python
     print("Hello, World!")
     ```
     - **Explanation**: `print()` is a built-in function that outputs text to the console. The text "Hello, World!" is enclosed in double quotes and passed as an argument to the `print()` function.

4. **Data Types and Variables**:
   - **List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.**
     - Basic data types include:
       - `int`: Integer numbers (e.g., `5`).
       - `float`: Floating-point numbers (e.g., `3.14`).
       - `str`: Strings of text (e.g., `"hello"`).
       - `bool`: Boolean values (`True` or `False`).
     - **Script**:
       ```python
       age = 30            # int
       height = 5.9        # float
       name = "Alice"      # str
       is_student = True   # bool

       print(age, height, name, is_student)
       ```

5. **Control Structures**:
   - **Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.**
     - **`if-else` Example**:
       ```python
       x = 10
       if x > 5:
           print("x is greater than 5")
       else:
           print("x is 5 or less")
       ```
     - **`for` Loop Example**:
       ```python
       for i in range(5):
           print(i)
       ```

6. **Functions in Python**:
   - **What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.**
     - Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and avoiding repetition.
     - **Function Example**:
       ```python
       def add(a, b):
           return a + b

       result = add(5, 3)
       print(result)  # Output: 8
       ```

7. **Lists and Dictionaries**:
   - **Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.**
     - **Lists** are ordered collections of items, while **dictionaries** are unordered collections of key-value pairs.
     - **Script**:
       ```python
       # List
       numbers = [1, 2, 3, 4, 5]
       numbers.append(6)
       print(numbers)

       # Dictionary
       person = {"name": "Alice", "age": 30}
       person["city"] = "New York"
       print(person)
       ```

8. **Exception Handling**:
   - **What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.**
     - Exception handling is used to manage errors and exceptions that occur during the execution of a program.
     - **Example**:
       ```python
       try:
           x = 1 / 0
       except ZeroDivisionError:
           print("Cannot divide by zero!")
       finally:
           print("Execution completed.")
       ```

9. **Modules and Packages**:
   - **Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.**
     - Modules are files containing Python code that can be imported into other Python scripts. Packages are collections of modules organized in directories.
     - **Example**:
       ```python
       import math

       print(math.sqrt(16))  # Output: 4.0
       ```

10. **File I/O**:
    - **How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.**
      - **Reading from a file**:
        ```python
        with open('input.txt', 'r') as file:
            content = file.read()
            print(content)
        ```
      - **Writing to a file**:
        ```python
        lines = ["Hello, world!", "This is a second line."]
        with open('output.txt', 'w') as file:
            file.write('\n'.join(lines))
        ```


# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


