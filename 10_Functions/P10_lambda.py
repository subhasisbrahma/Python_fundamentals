"""Demonstrates Python's lambda function (anonymous function) syntax as a concise
alternative to standard function definitions for small, single-expression tasks."""

# Lambda Function Definitions

# Syntax: lambda [arguments] : [expression]

# Basic arithmetic operations as lambda functions
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

# Demonstration Function

def demonstrate_lambda():
    """
    Executes the arithmetic operations defined by the lambda functions.
    """
    
    print(f"Addition (10 + 20): {add(10, 20)}")       # 30
    print(f"Subtraction (10 - 20): {sub(10, 20)}")   # -10
    print(f"Multiplication (10 * 20): {mul(10, 20)}")# 200
    print(f"Division (10 / 20): {div(10, 20)}")      # 0.5

# Execute Demonstration

demonstrate_lambda()
