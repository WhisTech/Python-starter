"""
PYTHON FUNDAMENTALS — PRACTICAL NOTES
====================================
Purpose: beginner-friendly revision notes for Python fundamentals and LeetCode.
How to use: read one section at a time, uncomment/run examples when practising.
These are notes, so most examples are inside comments or docstrings.

OFFICIAL REFERENCES
- https://docs.python.org/3/tutorial/
- https://docs.python.org/3/library/stdtypes.html
"""

# ============================================================
# 1. VARIABLES, DATA TYPES, INPUT, OUTPUT AND TYPE CONVERSION
# ============================================================

# A variable is a name referring to a value.
name = "Aditya"
age = 19
height = 168.0
is_student = True
nothing = None

# Common built-in types:
# int: whole numbers       -> 10, -4
# float: decimal numbers   -> 3.14, -0.5
# str: text                -> "Python"
# bool: True or False
# list: ordered, mutable   -> [1, 2, 3]
# tuple: ordered, immutable -> (1, 2, 3)
# set: unique items        -> {1, 2, 3}
# dict: key-value mapping  -> {"name": "Aditya"}

# Check a type:
# print(type(age))

# Convert between types:
# int("12")       -> 12
# float("3.5")    -> 3.5
# str(123)         -> "123"
# list("cat")     -> ['c', 'a', 't']
# tuple([1, 2])    -> (1, 2)
# set([1, 1, 2])   -> {1, 2}

# input() always returns a string. Convert it if you need a number:
# age = int(input("Enter age: "))

# print() displays values. f-strings insert expressions into text:
# print(f"My name is {name} and I am {age} years old.")

# Operators:
# Arithmetic: + - * / // % **
# /  true division: 5 / 2 -> 2.5
# // floor division: 5 // 2 -> 2
# % remainder: 5 % 2 -> 1
# ** exponent: 2 ** 3 -> 8
# Comparison: == != > < >= <=
# Logical: and, or, not
# Membership: in, not in
# Identity: is, is not (checks object identity, not value equality)

# == compares values; is checks whether two references are the same object.
# Use `is None` to check for None: if value is None: ...

# Truthiness: empty strings/collections, 0, 0.0, False and None are falsey.
# Most other values are truthy. bool(value) checks truthiness.


# =====================
# 2. STRINGS (str)
# =====================

# A string is an immutable sequence of Unicode characters.
text = "  Python Programming  "

# Create strings with single quotes, double quotes, or triple quotes.
# Empty string: empty = ""
# Strings support indexing and slicing:
# word = "Python"
# word[0]       -> 'P'       first character
# word[-1]      -> 'n'       last character
# word[0:3]     -> 'Pyt'     start included, end excluded
# word[:3]      -> 'Pyt'
# word[3:]      -> 'hon'
# word[::-1]    -> 'nohtyP'  reversed copy
# Strings cannot be changed in place: word[0] = 'J' raises TypeError.

# CASE CONVERSION
# s.upper()       -> all uppercase
# s.lower()       -> all lowercase
# s.casefold()    -> stronger lowercase-style conversion for caseless matching
# s.capitalize()  -> first character capitalized; remaining characters lowercased
# s.title()       -> title-case words (not perfect for every name/apostrophe)
# s.swapcase()    -> uppercase becomes lowercase and vice versa

# WHITESPACE / PADDING
# s.strip()       -> remove leading/trailing whitespace
# s.lstrip()      -> remove leading whitespace
# s.rstrip()      -> remove trailing whitespace
# s.removeprefix("pre") -> remove that exact prefix if present (Python 3.9+)
# s.removesuffix(".txt") -> remove that exact suffix if present (Python 3.9+)
# s.center(10, "-") -> center in width 10
# s.ljust(10, "-")  -> left-align in width 10
# s.rjust(10, "-")  -> right-align in width 10
# s.zfill(5)         -> pad numeric-looking text on the left with zeroes

# SEARCHING / COUNTING
# s.find("py")       -> first matching position, or -1 if not found
# s.rfind("a")      -> last matching position, or -1 if not found
# s.index("py")      -> first matching position; raises ValueError if absent
# s.rindex("a")     -> last matching position; raises ValueError if absent
# s.count("a")       -> number of non-overlapping occurrences
# s.startswith("Py") -> True if prefix matches
# s.endswith(".py")  -> True if suffix matches
# Use find() when 'not found' should be a normal result (-1).
# Use index() when absence should be treated as an error.

# REPLACE / SPLIT / JOIN
# s.replace("old", "new", count) -> new string with replacements; original unchanged
# "a,b,c".split(",")       -> ['a', 'b', 'c']
# "one  two".split()        -> ['one', 'two'] (runs of whitespace handled)
# s.rsplit(",", 1)           -> split from the right, at most once
# "a\nb\nc".splitlines()     -> ['a', 'b', 'c']
# "-".join(["a", "b"])     -> 'a-b'
# IMPORTANT: join() is called on the separator string, not the list.
# "hello".partition("l")    -> ('he', 'l', 'lo') at first separator
# "hello".rpartition("l")   -> ('hel', 'l', 'o') at last separator

# CHARACTER TESTS (return True/False)
# s.isalpha()     -> all characters are letters and string is non-empty
# s.isalnum()     -> all characters are letters or digits and non-empty
# s.isdecimal()   -> all characters are decimal digits and non-empty
# s.isdigit()     -> digit characters, broader than isdecimal()
# s.isnumeric()   -> numeric characters, broader still
# s.islower()     -> cased characters are lowercase and at least one is cased
# s.isupper()     -> cased characters are uppercase and at least one is cased
# s.istitle()     -> title-case test
# s.isspace()     -> all characters are whitespace and string is non-empty
# s.isidentifier() -> valid Python identifier syntax
# s.isprintable() -> all characters are printable (empty string is printable)

# FORMATTING
# f"Name: {name}"        -> f-string (usually the clearest choice)
# "Name: {}".format(name) -> format() method
# "{:.2f}".format(3.14159) -> '3.14'
# repr(s) shows a representation useful for debugging, often with quotes.

# String methods return new strings because strings are immutable.
# Most string methods do not change the original string.


# =====================
# 3. LISTS (list)
# =====================

# A list is ordered, mutable, and allows duplicates and mixed data types.
nums = [10, 20, 30, 20]
# Empty list: [] or list()
# Indexing/slicing work like strings: nums[0], nums[-1], nums[1:3]
# Change one item: nums[0] = 99

# ADD ITEMS
# nums.append(40)          -> adds one object at the end
# nums.extend([50, 60])     -> adds each item from an iterable
# nums.insert(1, 15)       -> inserts 15 at index 1
# Difference: append([4, 5]) adds a nested list; extend([4, 5]) adds two items.

# REMOVE ITEMS
# nums.remove(20)  -> removes first matching value; ValueError if absent
# nums.pop()       -> removes and returns last item
# nums.pop(1)      -> removes and returns item at index 1; IndexError if invalid
# del nums[0]      -> delete by index
# del nums[1:3]    -> delete a slice
# nums.clear()     -> remove all items
# If you need to handle a possibly missing value, check `if value in nums:`
# before remove(), or use try/except ValueError.

# FIND / COUNT / ORDER / COPY
# nums.index(20)        -> index of first match; ValueError if absent
# nums.count(20)        -> number of occurrences
# nums.sort()           -> sorts the same list in place; returns None
# nums.sort(reverse=True) -> descending order in place
# nums.reverse()        -> reverses same list in place; returns None
# sorted(nums)          -> returns a new sorted list; original unchanged
# sorted(nums, reverse=True) -> new list in descending order
# nums.copy()           -> shallow copy
# nums[:]               -> another shallow-copy idiom
# list(existing_iterable) -> creates a list from an iterable

# VERY IMPORTANT: in-place methods such as append(), sort(), reverse(), extend()
# usually return None. Do not write: nums = nums.sort(). Use nums.sort(); print(nums).

# LIST OPERATIONS
# len(nums), min(nums), max(nums), sum(nums)
# 20 in nums, 99 not in nums
# nums + [40] -> new concatenated list
# nums * 2    -> new list repeating the contents

# COPYING: `b = a` does NOT copy a list; both names refer to the same list.
# `b = a.copy()` creates a shallow copy. Nested mutable objects remain shared.

# LIST COMPREHENSION
# squares = [x * x for x in range(5)]
# evens = [x for x in range(10) if x % 2 == 0]


# =====================
# 4. TUPLES (tuple)
# =====================

# A tuple is ordered and immutable. It allows duplicates.
# t = (10, 20, 30)
# Empty tuple: () or tuple()
# One-item tuple MUST have a comma: one = (5,)
# (5) is just the integer 5, not a tuple.
# Access: t[0], t[-1], t[1:]
# Unpacking: x, y = (10, 20)
# Swap values: x, y = y, x

# Tuple methods (only two public data methods):
# t.count(20) -> number of occurrences
# t.index(20) -> first index; ValueError if absent
# Common operations: len(t), min(t), max(t), sum(t) (for numeric values), x in t
# You cannot append/remove/assign tuple items. Convert to list to edit, then tuple().
# A tuple is hashable only if all of its contents are hashable.


# =====================
# 5. SETS (set)
# =====================

# A set is mutable, contains unique hashable elements, and has no indexing/slicing.
# s = {1, 2, 3}
# Empty set: set() ; {} creates an empty dictionary, not a set.
# Duplicates are removed automatically: set([1, 1, 2]) -> {1, 2}
# Elements must be hashable; lists and dictionaries cannot be set elements.

# ADD / REMOVE
# s.add(4)             -> add one element
# s.update([4, 5], (6, 7)) -> add all elements from one or more iterables
# s.remove(2)          -> remove item; KeyError if absent
# s.discard(2)          -> remove item if present; no error if absent
# s.pop()               -> removes and returns an arbitrary element; KeyError if empty
# s.clear()             -> remove all elements
# s.copy()              -> shallow copy
# Use discard() when absence is normal and should not raise an error.
# Use remove() when a missing element indicates a problem.

# MATHEMATICAL OPERATIONS (these return a new set)
# a | b                 or a.union(b) -> union: elements in either set
# a & b                 or a.intersection(b) -> common elements
# a - b                 or a.difference(b) -> in a but not b
# a ^ b                 or a.symmetric_difference(b) -> in either, but not both
# a.issubset(b)         -> every item of a is in b
# a.issuperset(b)       -> every item of b is in a
# a.isdisjoint(b)       -> no common items

# IN-PLACE SET OPERATIONS (modify original set; return None)
# a.update(b)
# a.intersection_update(b)
# a.difference_update(b)
# a.symmetric_difference_update(b)

# Other useful operations: len(s), x in s, x not in s, for x in s
# Set order is not guaranteed. Do not rely on printed order.
# Method versions like a.intersection(iterable) accept general iterables;
# operators like a & b expect set-like operands.


# =========================
# 6. FROZEN SET (frozenset)
# =========================

# A frozenset is an immutable set: unique hashable elements, no add/remove methods.
# fs = frozenset([1, 2, 2, 3]) -> frozenset({1, 2, 3})
# Empty frozenset: frozenset()
# Supports: union(), intersection(), difference(), symmetric_difference(),
# issubset(), issuperset(), isdisjoint(), copy(), len(), membership tests.
# Operations return a new set-like result; the original frozenset cannot change.
# Because it is immutable/hashable, a frozenset can be a dictionary key or
# an element of another set (provided its elements are hashable).
# A normal mutable set cannot be a dictionary key or an element of another set.


# =====================
# 7. DICTIONARIES (dict)
# =====================

# A dictionary maps unique keys to values. It is mutable and preserves insertion order.
# Keys must be hashable; values can be any type.
# student = {"name": "Aditya", "age": 19}
# Empty dictionary: {} or dict()
# Read value: student["name"] -> KeyError if key is missing
# Safe lookup: student.get("name") -> None if missing by default
# student.get("marks", 0) -> 0 if 'marks' is missing
# Use [] when the key is expected and missing data should be an error.
# Use get() when a key may be absent and you want a default instead of KeyError.

# ADD / UPDATE
# student["city"] = "Navi Mumbai" -> add key or replace its value
# student.update({"age": 20, "course": "CSE DS"}) -> merge/update entries
# student.setdefault("grade", "A") -> return existing value or insert default
# Beware: setdefault() inserts the default if the key is absent.

# READ KEYS / VALUES / PAIRS
# student.keys()   -> dynamic view of keys
# student.values() -> dynamic view of values
# student.items()  -> dynamic view of (key, value) pairs
# list(student)    -> list of keys
# for key in student: ... -> iterates over keys
# for key, value in student.items(): ... -> iterates over key-value pairs

# REMOVE
# student.pop("age") -> remove and return value; KeyError if missing without default
# student.pop("age", None) -> return None if missing, without raising KeyError
# student.popitem() -> remove and return the last inserted (key, value) pair
# del student["name"] -> delete key; KeyError if missing
# student.clear() -> remove all items
# student.copy() -> shallow copy

# OTHER DICTIONARY FEATURES
# len(student), "name" in student -> membership tests keys, not values
# "Aditya" in student.values() -> test values
# dict.fromkeys(["a", "b"], 0) -> create dictionary with keys and shared value
# dict([("a", 1), ("b", 2)]) -> create from key-value pairs
# Dictionary comprehension: squares = {x: x*x for x in range(5)}
# Merge dictionaries (Python 3.9+): merged = first | second
# `first | second` returns a new dict; `first |= second` updates first in place.

# Missing-key choice:
# d[key]              -> raises KeyError if absent
# d.get(key)          -> returns None if absent
# d.get(key, default) -> returns default if absent
# key in d            -> check existence before accessing


# =========================
# 8. CONTROL STATEMENTS
# =========================

# if / elif / else:
# score = 75
# if score >= 90:
#     print("A")
# elif score >= 75:
#     print("B")
# else:
#     print("Keep practising")

# Nested conditions are allowed, but prefer clear conditions where possible.
# Comparison chaining: if 0 <= score <= 100: ...
# Conditional expression: result = "pass" if score >= 40 else "fail"

# match/case (Python 3.10+):
# command = "start"
# match command:
#     case "start": print("Starting")
#     case "stop": print("Stopping")
#     case _: print("Unknown command")

# break    -> exit the nearest loop immediately
# continue -> skip to the next iteration of the nearest loop
# pass     -> do nothing; placeholder where a statement is required


# =====================
# 9. LOOPS
# =====================

# for loop: iterates over items in an iterable
# for fruit in ["apple", "mango"]:
#     print(fruit)

# range(stop)              -> 0 through stop-1
# range(start, stop)       -> start through stop-1
# range(start, stop, step) -> increment by step
# for i in range(5): print(i)       # 0, 1, 2, 3, 4
# for i in range(10, 0, -1): ...    # counts down from 10 to 1

# while loop repeats while its condition is true:
# count = 0
# while count < 3:
#     print(count)
#     count += 1
# Ensure the condition eventually becomes false to avoid an infinite loop.

# enumerate(iterable, start=0) -> gives (index, item) pairs
# for index, value in enumerate(["a", "b"], start=1): ...

# zip(a, b) -> pair items from iterables, stopping at the shortest by default
# for name, mark in zip(["A", "B"], [80, 90]): ...

# Loop else: else runs if the loop finishes normally, but not if it exits via break.
# for n in [2, 4, 6]:
#     if n % 2 != 0:
#         break
# else:
#     print("No odd values found")

# Nested loops: a loop inside another loop.
# Use `break` carefully: it exits only the nearest enclosing loop.

# Comprehensions (compact ways to build collections):
# [x*x for x in range(5)]                 -> list
# {x*x for x in range(5)}                 -> set
# {x: x*x for x in range(5)}               -> dict
# tuple(x*x for x in range(5))             -> tuple from generator expression


# =====================
# 10. FUNCTIONS
# =====================

# A function is a reusable block of code defined with def.
# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Aditya"))

# print() displays a value; return sends a value back to the caller.
# A function without an explicit return returns None.

# Parameters are names in the function definition; arguments are values passed in.
# def add(a, b): return a + b
# add(2, 3)       -> positional arguments
# add(a=2, b=3)   -> keyword arguments

# Default parameters:
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}"
# Put required parameters before parameters with defaults.

# *args collects extra positional arguments into a tuple:
# def total(*numbers):
#     return sum(numbers)

# **kwargs collects extra keyword arguments into a dictionary:
# def show_details(**details):
#     return details

# Unpacking arguments:
# nums = [2, 3]
# add(*nums)             -> same as add(2, 3)
# info = {"a": 2, "b": 3}
# add(**info)             -> same as add(a=2, b=3)

# Scope: local variables are created inside a function. A function can read
# global names, but use global only when genuinely necessary.

# Lambda: small anonymous expression function
# square = lambda x: x * x
# Prefer def for functions that need multiple steps or clear documentation.

# Docstring: first string inside a function/class/module, used as documentation.
# def square(x):
#     """Return x squared."""
#     return x * x

# IMPORTANT DEFAULT-VALUE TRAP:
# Avoid mutable defaults such as def add_item(item, items=[]): ...
# The same list is reused across calls. Safer pattern:
# def add_item(item, items=None):
#     if items is None:
#         items = []
#     items.append(item)
#     return items


# =========================
# 11. BUILT-IN FUNCTIONS TO KNOW
# =========================

# len(x)       -> number of items
# type(x)      -> type of object
# isinstance(x, int) -> type check (also considers subclasses)
# print(x)     -> display
# input()      -> read text input
# int(), float(), str(), bool(), list(), tuple(), set(), frozenset(), dict()
# range()      -> sequence-like range of integers
# enumerate()  -> index-item pairs
# zip()        -> pair values from iterables
# sorted(x)    -> new sorted list
# reversed(x)  -> reverse iterator (not automatically a list)
# sum(x)       -> sum numeric items
# min(x), max(x) -> smallest/largest item
# abs(n)       -> absolute value
# round(n, 2)  -> rounding (binary floating-point can affect edge cases)
# any(x)       -> True if at least one item is truthy
# all(x)       -> True if every item is truthy; True for an empty iterable
# map(func, iterable) -> lazy iterator applying func
# filter(func, iterable) -> lazy iterator retaining items where func is truthy
# help(str)    -> interactive help in Python
# dir(obj)     -> names/attributes available on an object (includes internals)


# =========================
# 12. COMMON BEGINNER MISTAKES
# =========================

# 1. {} is an empty dict; set() is an empty set.
# 2. Tuple with one item needs a comma: (5,).
# 3. Strings and tuples are immutable; list and set are mutable.
# 4. List/dict/set cannot be set elements or dictionary keys because they are unhashable.
# 5. Dictionary membership checks keys: `key in d`, not values.
# 6. `d[key]` raises KeyError when absent; `d.get(key, default)` can avoid it.
# 7. set.remove(x) raises KeyError when absent; set.discard(x) does not.
# 8. list.remove(x) raises ValueError when absent; list.pop(i) uses an index.
# 9. find() returns -1 if absent; index() raises ValueError.
# 10. append(x) adds one object; extend(iterable) adds each item.
# 11. sort(), reverse(), append(), extend(), update() usually mutate and return None.
# 12. sorted(x) returns a new list; x.sort() changes a list in place.
# 13. `b = a` is assignment, not a copy for mutable collections.
# 14. `is` is not a replacement for `==`; use `is None` for None checks.
# 15. `input()` returns str; convert numeric input explicitly.
# 16. range() excludes the stop value.
# 17. `break` exits the nearest loop; `continue` skips one iteration.
# 18. A function with no return statement returns None.
# 19. Never rely on set iteration order.
# 20. Avoid modifying a list while iterating over that same list; iterate over a copy
#     or build a new list instead.


# =========================
# 13. QUICK COMPARISON TABLE
# =========================

# Type       Ordered?  Mutable?  Duplicates?   Access pattern
# str        Yes       No        Yes           Index / slice
# list       Yes       Yes       Yes           Index / slice
# tuple      Yes       No        Yes           Index / slice
# set        No*       Yes       No            Membership / iteration
# frozenset  No*       No        No            Membership / iteration
# dict       Insertion order Yes No duplicate keys Key -> value
# *Sets do not provide positional indexing or guarantee a useful iteration order.


# =========================
# 14. PRACTICE CHECKLIST
# =========================

# [ ] Explain mutable vs immutable with examples.
# [ ] Explain find() vs index().
# [ ] Explain append() vs extend().
# [ ] Explain remove() vs pop() vs del for lists.
# [ ] Explain remove() vs discard() for sets.
# [ ] Explain dictionary [] vs get().
# [ ] Explain keys(), values(), items().
# [ ] Use if/elif/else and nested conditions.
# [ ] Use for, while, range(), enumerate(), zip().
# [ ] Use break, continue, pass, and loop else.
# [ ] Write functions using return, defaults, *args and **kwargs.
# [ ] Recognize methods that mutate in place and return None.

if __name__ == "__main__":
    print("Python Fundamentals Notes")
    print("Open this file and read the sections. Examples are commented for practice.")
