# CSE 2102: Discrete Mathematics Sessional (RUET)

This repository contains the programming assignments and a reusable utility package developed for the CSE 2102 Discrete Mathematics Sessional course. The core objective is to implement fundamental concepts from discrete mathematics—including logic, set theory, number theory, recursion, and graph theory—using Python.

## 📦 Core Utility Package (`dms_utils`)

To maintain code consistency and efficiency across all lab assignments, a reusable Python package named `dms_utils` has been created. It centralizes robust implementations of common discrete math concepts.

### Structure

The package is located in the `dms_utils/` directory:

* `dms_utils/discrete_utils.py`: Contains all primary function definitions (GCD, Modular Inverse, Truth Tables, Factorial, etc.).

* `dms_utils/__init__.py`: Exposes all functions directly at the package level for clean imports.

### Usage

To use any function from the package in your daily lab files (e.g., `lab07.py`), ensure your environment is set up correctly and import the function directly:

```python
# To import the GCD and Modular Inverse functions
from dms_utils import gcd_euclid, mod_inverse

# Example: Check Modular Inverse
try:
    inverse = mod_inverse(7, 26)
    print(f"Inverse of 7 mod 26 is: {inverse}")
except ValueError as e:
    print(e)
```
## 📝 Lab Assignments

This section lists the individual lab assignment files, structured according to the course manual. Each file contains the complete solution code for the experiments of that specific lab session.

| Lab No. | File Name | Topics Covered | Manual Reference (Week) |
| :---: | :---: | :---: | :---: |
| **Lab 1** | `lab01.py` | Propositional Logic, Truth Tables, Logical Equivalence | 1 |
| **Lab 2** | `lab02.py` | Predicates, Quantifiers, Rules of Inference | 2 |
| **Lab 3** | `lab03.py` | Set Operations, Computer Representation of Sets | 3 |
| **Lab 4** | `lab04.py` | Functions, Mappings (One-to-One, Onto), Composition | 4 |
| **Lab 5** | `lab05.py` | Sequences, Recurrence Relations, Summations | 5 |
| **Lab 6** | `lab06.py` | Counting Principles, Permutations, and Combinations | 9 (or equivalent Combinatorics week) |
| **Lab 7** | `lab07.py` | Divisibility, Modular Arithmetic, GCD/LCM | 7 |
| **Lab 8** | `lab08.py` | Solving Linear Congruences, Modular Equations | 8 |
| **Lab 9** | `lab09.py` | Mathematical Induction and Recursion | 9 |
| **Lab 10** | `lab10.py` | Graph Models, Adjacency Matrix/List Representation | 10 |
| **Lab 11** | `lab11.py` | Graph Traversal: BFS and DFS | 11 |
| **Lab 12** | `lab12.py` | Planar Graphs and Graph Coloring | 12 |
| **Lab 13** | `lab13.py` | Revision and Comprehensive Graph Analysis | 13 |

## 🚀 Getting Started (Local Setup)

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/hodini007/discrete-utils
    cd cse2102
    ```

2.  **Ensure Python is installed.** (Python 3.x is recommended.)

3.  **Run a Test Script:** To verify your package is working correctly, run the provided test file from the root directory:

    ```bash
    python test_dms.py
    ```

4.  **Work on Assignments:** Navigate to the root folder and execute any lab file:

    ```bash
    python lab01.py
    ```

<!-- end list -->

```eof
```
