[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WfNmjXUk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15397748&assignment_repo_type=AssignmentRepo)
# SE-Assignment-6
 Assignment: Introduction to Python
Instructions:
Answer the following questions based on your understanding of Python programming. Provide detailed explanations and examples where appropriate.

 Questions:

1. Python Basics:
   - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.
   - Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility.

     Some key features that contribute to its popularity among developers:
 -Easy to learn and read: Python's syntax is clear and intuitive, using indentation to define code blocks.
 -Interpreted language: Python code is executed line by line, making debugging easier.
 -Dynamically typed: Variables don't need explicit type declarations.
 -Large standard library: Python comes with a comprehensive set of built-in modules and functions.
 -Automatic memory management: Python uses garbage collection, reducing memory management overhead.
 -Strong community support: A large, active community contributes to Python's development and provides resources.
 
Cases where Python is particularly effective:

Web Development:

Frameworks like Django and Flask make it easy to build web applications.
Example: Building a content management system for a blog.


Data Science and Machine Learning:

Libraries like NumPy, Pandas, and Scikit-learn facilitate data analysis and model creation.
Example: Developing a predictive model for stock prices.


Artificial Intelligence:

Frameworks like TensorFlow and PyTorch are popular for deep learning projects.
Example: Creating a natural language processing system for chatbots.


2. Installing Python:
   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.
  
   - Download the installer:

Go to the official Python website: https://www.python.org/
Click on "Downloads"
Under "Download for Windows", click on the button that says "Python 3.x.x" (where x.x is the latest version number)


Run the installer:

Locate the downloaded file (usually in your Downloads folder)
Double-click the file to run it (e.g., "python-3.x.x-amd64.exe")


Customize the installation (optional):

Check the box that says "Add Python 3.x to PATH" - this makes it easier to run Python from the command line
Click "Customize installation" if you want to change the install location or select/deselect optional features


Install Python:

Click "Install Now" (or "Next" if you customized the installation)
Wait for the installation to complete


Verify the installation:

Open Command Prompt (you can search for "cmd" in the Start menu)
Type "python --version" and press Enter
If Python is installed correctly, you should see the version number

To set up virtual environment, use command prompt or gitbash to execute;

python --version
pip --version

Try running Python:

Type python and press Enter
You should see the Python interactive shell (>>>)
Type print("Hello, World!") and press Enter
If "Hello, World!" is printed, Python is working correctly
Type exit() to leave the Python shell



Setting up a virtual environment:

Open Command Prompt or Terminal.
Navigate to your project directory:
cd path/to/your/project

Create a virtual environment:
python -m venv myenv
Replace "myenv" with your preferred name for the environment.
Activate the virtual environment:

On Windows:
myenv\Scripts\activate

Install packages in the virtual environment:
Copypip install package_name

When you're done, deactivate the virtual environment:
deactivate


3. Python Syntax and Semantics:
   - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.
  
-Create a Python file:

Open Git Bash
Navigate to the directory where you want to create your file
Create a new file with a .py extension:
touch hello_world.py

Edit the file:

Open the file in a text editor. You can use Nano, which is often available in Git Bash:
Copynano hello_world.py

Type the following Python code:
python print("Hello, World!")

Save the file and exit the editor

In Nano, press Ctrl+X, then Y, then Enter

Run the Python program:

In Git Bash, make sure you're in the directory containing hello_world.py
Run the program using Python:
python hello_world.py

- should see "Hello, World!" printed in the console


4. Data Types and Variables:
   - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.
  
   - Numeric Types:
a) int (Integer):

Whole numbers, positive or negative
Example: 5, -3, 1000

b) float (Floating-point):

Numbers with decimal points
Example: 3.14, -0.5, 2.0

Sequence Types:
c) str (String):

Ordered sequence of characters
Immutable (can't be changed after creation)
Example: "Hello, World!", 'Python'

d) list:

Ordered collection of items
Mutable (can be modified)
Example: [1, 2, 3], ['a', 'b', 'c']

e) tuple:

Ordered collection of items
Immutable
Example: (1, 2, 3), ('a', 'b', 'c')

f)Boolean :

Represents True or False
Example: True, False

5. Control Structures:
   - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.
  
   - if statement:

Used to execute a block of code only if a condition is True.

x = 10
if x > 5:
    print("x is greater than 5")

    if-else statement:

Executes one block if the condition is True, and another if it's False.

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
    while loop:

Repeats a block of code as long as a condition is True.

count = 0
while count < 5:
    print(count)
    count += 1

    Loop control statements:

break: Exits the loop prematurely.
continue: Skips the rest of the current iteration and moves to the next.
else: Executed if the loop completes normally (without a break).

for i in range(5):
    if i == 3:
        break
    print(i)

6. Functions in Python:
   - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.
  
    def function_name(parameters):
    """Docstring explaining what the function does"""
    # Function body
    # Code to perform the task
    return result  # Optional

   Key aspects of functions:

Modularity:

Functions break code into smaller, manageable pieces.
This makes code easier to understand, debug, and maintain.


Reusability:

Once defined, functions can be called multiple times from different parts of your program.
This reduces code duplication.


Abstraction:

Functions hide complex implementation details behind a simple interface.
Users of the function don't need to know how it works internally.


Organization:

Functions help organize code logically, grouping related operations.


Scope:

Variables defined inside a function are typically local to that function.
This helps prevent naming conflicts and unintended side effects.


Testability:

Functions with well-defined inputs and outputs are easier to test.


Parameterization:

Functions can accept parameters, making them flexible and adaptable.

Functions are a cornerstone of structured programming and are essential for writing clean, efficient, and maintainable code in Python. They allow you to break complex problems into smaller, more manageable parts, and they promote code reuse and modularity.

def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    
    :param a: The first number
    :param b: The second number
    :return: The sum of a and b
    """
    return a + b

# Examples of calling the function
result1 = add_numbers(5, 3)
print("Result 1:", result1)  # Output: Result 1: 8

result2 = add_numbers(10.5, 4.5)
print("Result 2:", result2)  # Output: Result 2: 15.0

# You can also use variables as arguments
x = 20
y = 30
result3 = add_numbers(x, y)
print("Result 3:", result3)  # Output: Result 3: 50

# Or use the function directly in a print statement
print("Result 4:", add_numbers(100, 200))  # Output: Result 4: 300



8. Lists and Dictionaries:
   - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.
  
- Differences between Lists and Dictionaries in Python:

Structure:

Lists: Ordered collection of items, indexed by position (starting from 0). Items can be of any data type.
Dictionaries: Unordered collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.
Access:

Lists: Accessed by their index.
Dictionaries: Accessed by their keys.
Usage:

Lists: Used when the order of items is important or when you need to access items by their position.
Dictionaries: Used when you need a logical association between a key and a value, and quick lookups based on keys.
Methods:

Lists: Have methods like append(), extend(), insert(), remove(), pop(), index(), count(), sort(), and reverse().
Dictionaries: Have methods like keys(), values(), items(), get(), update(), pop(), and popitem().

# Create a list of numbers
numbers_list = [1, 2, 3, 4, 5]

# Create a dictionary with key-value pairs
person_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Basic operations on the list
# Add an item to the list
numbers_list.append(6)
print("List after appending 6:", numbers_list)

# Remove an item from the list
numbers_list.remove(3)
print("List after removing 3:", numbers_list)

# Access an item by index
third_item = numbers_list[2]
print("Third item in the list:", third_item)

# Basic operations on the dictionary
# Add a new key-value pair
person_dict["occupation"] = "Engineer"
print("Dictionary after adding occupation:", person_dict)

# Remove a key-value pair
del person_dict["age"]
print("Dictionary after removing age:", person_dict)

# Access a value by key
person_name = person_dict["name"]
print("Person's name:", person_name)


9. Exception Handling:
   - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.
     Exception handling in Python is a mechanism to handle errors or exceptional conditions that occur during the execution of a program. Instead of letting the program crash when an 
     error occurs, you can use exception handling to catch the error, handle it gracefully, and continue executing the program or terminate it in a controlled manner.

     def divide_100_by_user_input():
    try:
        # Prompt the user for input
        user_input = input("Enter a number to divide 100 by: ")
        
        # Convert the input to a float
        number = float(user_input)
        
        # Perform the division
        result = 100 / number
        
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
        result = None
        
    except ValueError:
        # Handle invalid input error (e.g., if the input is not a number)
        print("Error: Invalid input. Please enter a numeric value.")
        result = None
        
    finally:
        # This block always executes, regardless of whether an exception was raised
        print("Execution complete.")
    
    return result

# Run the function and print the result
result = divide_100_by_user_input()
if result is not None:
    print(f"Result: {result}")


     
     

10. Modules and Packages:
   - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.

modules and packages are fundamental concepts for organizing and managing code. They allow developers to structure their programs in a more readable, maintainable, and reusable way.

Import the module in another script or interactive session.

# main.py
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.pi)              # Output: 3.14159


11. File I/O:
    - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.
   
    Writing code that reads Python file.

    # Using the with statement (preferred way)
    with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Without the with statement (needs manual close)
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

 Script for reading the content of the file and printing it on the console.
 def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with your file path
    read_and_print_file(file_path)


Script of printing on the console
Writing a List of Strings to a File

def write_list_to_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except IOError as e:
        print(f"An I/O error occurred: {e}")



# Submission Guidelines:
- Your answers should be well-structured, concise, and to the point.
- Provide code snippets or complete scripts where applicable.
- Cite any references or sources you use in your answers.
- Submit your completed assignment by [due date].


