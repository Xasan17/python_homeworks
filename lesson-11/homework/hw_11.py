# =======================================
# HOW TO CREATE A VIRTUAL ENVIRONMENT (Windows)
# =======================================
# Open Command Prompt (cmd) and run:
# 
# python -m venv venv
# venv\Scripts\activate
# pip install numpy  # or any other package
# =======================================


# === math_operations.py ===
# Module for basic math operations

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers"""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b

def divide(a, b):
    """Returns the result of dividing two numbers"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# === string_utils.py ===
# Module for string operations

def reverse_string(s):
    """Returns the reversed version of the string"""
    return s[::-1]

def count_vowels(s):
    """Returns the number of vowels in the string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# === geometry/circle.py ===
# Inside geometry package

import math

def calculate_area(radius):
    """Returns the area of a circle given its radius"""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Returns the circumference of a circle given its radius"""
    return 2 * math.pi * radius


# === file_operations/file_reader.py ===
# Module to read from a file

def read_file(file_path):
    """Reads a file and returns its content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


# === file_operations/file_writer.py ===
# Module to write to a file

def write_file(file_path, content):
    """Writes content to a file"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# === DEMO: Using all functions above ===

if __name__ == "__main__":
    # Using math operations
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))
    print("Multiplication:", multiply(6, 7))
    print("Division:", divide(8, 2))

    # Using string utils
    text = "Hello World"
    print("Reversed string:", reverse_string(text))
    print("Number of vowels:", count_vowels(text))

    # Using geometry
    radius = 5
    print("Circle area:", calculate_area(radius))
    print("Circle circumference:", calculate_circumference(radius))

    # Using file operations
    file_path = "example.txt"
    content = "Hello, this is a file write example."
    write_file(file_path, content)
    print("File content:", read_file(file_path))
