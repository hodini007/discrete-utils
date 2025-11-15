# discrete_utils.py - Core mathematical utilities for Discrete Mathematics Sessional Course
# This file contains reusable functions for Logic, Sets, Number Theory, and Recursion,
# based on the material in Labs 1, 3, 5, 7, and 9.

import itertools
import math
from collections import deque
import sys

# Increase recursion limit for complex recursive problems (e.g., in Lab 9)
sys.setrecursionlimit(2000)


# ==============================================================================
# I. LOGIC AND TRUTH TABLES (Lab 1)
# ==============================================================================

def truth_table_generator(expression_string, variables):
    """
    Generates and prints the truth table for a given propositional logic expression.
    Uses Python's boolean operators ('and', 'or', 'not') for evaluation.
    """
    print(" | ".join(variables) + " | Result")
    print("-" * (len(variables) * 3 + 10))

    # Iterate through all possible combinations of True/False
    for values in itertools.product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))

        try:
            result = eval(expression_string, env)
        except Exception as e:
            # Handle potential syntax or name errors
            print(f"Error evaluating expression: {e}. Check operators ('and', 'or', 'not').")
            return

        row = " | ".join(['T' if v else 'F' for v in values])
        final_result = 'T' if result else 'F'
        print(f"{row} | {final_result}")


def check_equivalence(expr1, expr2, variables):
    """
    Checks if two logical expressions are logically equivalent (P <=> Q is a tautology).
    """
    for values in itertools.product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        try:
            val1 = eval(expr1, env)
            val2 = eval(expr2, env)
        except Exception:
            # Error handling for invalid expressions
            return False

        if val1 != val2:
            return False
    return True


# ==============================================================================
# II. SET OPERATIONS (Lab 3)
# ==============================================================================

def cartesian_product(set_a, set_b):
    """Computes the Cartesian product A x B as a set of tuples."""
    return {(a, b) for a in set_a for b in set_b}


def is_disjoint(set_a, set_b):
    """Checks if two sets are disjoint (their intersection is empty)."""
    return set_a.isdisjoint(set_b)


# ==============================================================================
# III. NUMBER THEORY & MODULAR ARITHMETIC (Lab 7)
# ==============================================================================

def gcd_euclid(a, b):
    """Computes the Greatest Common Divisor using the Euclidean Algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Computes the Least Common Multiple (LCM) using the GCD formula."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_euclid(a, b)


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm: Finds g, x, y such that a*x + b*y = g = gcd(a, b).
    Returns: (g, x, y)
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a, n):
    """
    Computes the modular inverse a^-1 mod n.
    Raises: ValueError if the inverse does not exist (gcd(a, n) != 1).
    """
    g, x, y = extended_gcd(a, n)
    if g != 1:
        raise ValueError(f"Modular inverse for {a} mod {n} does not exist.")
    return x % n


def check_congruence(a, b, n):
    """Verifies a is congruent to b modulo n (a = b (mod n))."""
    return (a - b) % n == 0


# ==============================================================================
# IV. RECURSION AND SEQUENCES (Lab 5 & 9)
# ==============================================================================

def fibonacci_recursive(n):
    """Computes the n-th Fibonacci number recursively."""
    if n < 0:
        raise ValueError("Input must be non-negative.")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """Computes the n-th Fibonacci number iteratively (more efficient)."""
    if n < 0:
        raise ValueError("Input must be non-negative.")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial_recursive(n):
    """Computes the factorial of n recursively."""
    if n < 0:
        raise ValueError("Input must be non-negative.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def recursive_sum(n):
    """Computes the sum of the first n positive integers recursively."""
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)