# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: A3 - Swap Without a Third Variable
# Idea : read a then b on separate lines, swap using Python's tuple
#        assignment (no temp variable, no arithmetic trick), print a, then b.
# Time : O(1)        Own tests: 2 (see bottom of file)

a = int(input())
b = int(input())
a, b = b, a
print(a)
print(b)

# Own tests:
# Input: -5 / 5   -> Output: 5 / -5
# Input: 7 / 7    -> Output: 7 / 7
