# Python on steroids

## Story

In your new position, you have to do code reviews for junior colleagues.
Their code is rather clumsy and verbose, and does not really use
the rich standard library of Python. Your job is to refactor the functions
into a more elegant and readable form.

Luckily, there are tests included along with the codebase, so you can check
if you altered the behavior of the refactored functions.

## What are you going to learn?

- Understand and use advanced language features.
- Think in terms of density AND readability at the same time.
- Refactor code without breaking functionality.

## Tasks

1. Parse a line describing user data in the format: `FirstName LastName usernameexample.com`.
Return a tuple: `(first_name, last_name, user, host)`.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

2. Compare two lists of file names, and find the files that are removed or added.
Return a dictionary with two keys:
- 'removed': A sorted list of removed files.
- 'added': A sorted list of added files.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

3. Write out a log line in a specific format.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **two lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

4. Find the biggest rectangle in a sequence.
Rectangles are represented as tuples of `(width, height)`.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **one line** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

5. Find a pattern in a file. Print out all lines that match the pattern
(case-insensitive) with line numbers.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **four lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

6. Read all words from a file that are longer than a given length.
Convert to lowercase, and remove punctuation.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

7. Find top `n` words in a file. Return a list of tuples (word, count), ordered by
descending count.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **two lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

## General requirements

- There are no nasty tricks in the code to reduce actual line numbers, such as using semicolons (`print(x); print(y); print(z)`), or using dynamic code evaluation tools (`eval` or `exec`).
