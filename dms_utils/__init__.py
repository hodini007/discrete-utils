# __init__.py - Exposes core functions directly from the discrete_utils module.
# This allows users to import functions like: 'from dms_utils import gcd_euclid, factorial_recursive'

from .discrete_utils import (
    # Logic
    truth_table_generator,
    check_equivalence,

    # Sets
    cartesian_product,
    is_disjoint,

    # Number Theory
    gcd_euclid,
    lcm,
    extended_gcd,
    mod_inverse,
    check_congruence,

    # Recursion/Sequences
    fibonacci_recursive,
    fibonacci_iterative,
    factorial_recursive,
    recursive_sum
)