# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: B2 - Circle Calculator
# Idea : read radius r, compute area = pi*r*r and circumference = 2*pi*r
#        using the fixed pi = 3.14159265, print each with 3 decimal places.
# Time : O(1)        Own tests: 2 (see bottom of file)

PI = 3.14159265
r = float(input())
area = PI * r * r
circumference = 2 * PI * r
print(f"Area = {area:.3f}")
print(f"Circumference = {circumference:.3f}")

# Own tests:
# Input: 0    -> Output: Area = 0.000 / Circumference = 0.000
# Input: 1000 -> Output: Area = 3141592.650 / Circumference = 6283.185
