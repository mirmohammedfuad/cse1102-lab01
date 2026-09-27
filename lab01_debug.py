# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: Section 12 - Debugging / Error Analysis
# Idea : fixed versions of the three buggy programs, with explanation.

# ---------------------------------------------------------------
# Debug 1 - Adding ten
# Bug: input() always returns a str, so num + 10 tries to concatenate
#      a string with an int -> TypeError. Fix: convert num to int first.
num = int(input("Enter a number: "))
result = num + 10
print(result)

# ---------------------------------------------------------------
# Debug 2 - The silent bug
# Bug: a and b are strings, so a + b concatenates them ("3"+"4" -> "34")
#      instead of adding numbers. No error is raised, so the bug is silent.
#      Fix: convert both to int before adding.
a = int(input())
b = int(input())
print(a + b)

# ---------------------------------------------------------------
# Debug 3 - Circle area
# Bug: radius is read as a string, and ** does not work between a str
#      and an int -> TypeError. Fix: convert radius to float first.
radius = float(input())
print(3.14 * radius ** 2)
