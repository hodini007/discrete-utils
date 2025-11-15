# test_dms.py - This file lives *outside* the dms_utils package folder
# (i.e., in the same directory as the dms_utils folder).

# 1. Import functions directly from the package
from dms_utils import gcd_euclid, factorial_recursive, fibonacci_iterative

# 2. Run a few tests to confirm they work

print("--- Discrete Math Utilities Test ---")

# Test 1: Number Theory (GCD)
a, b = 48, 18
print(f"1. GCD({a}, {b}) = {gcd_euclid(a, b)}")

# Test 2: Recursion (Factorial)
n = 5
print(f"2. {n}! = {factorial_recursive(n)}")

# Test 3: Sequences (Fibonacci)
m = 10
fib_10 = fibonacci_iterative(m)
print(f"3. 10th Fibonacci number (iterative) = {fib_10}")

print("----------------------------------")
print("If all tests run without error, the package is set up correctly!")
