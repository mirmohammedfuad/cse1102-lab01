# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: P1 - Compound Interest (Post-lab)
# Idea : read P, R, T from one line; final amount = P * (1 + R/100) ** T;
#        print with 2 decimal places.
# Time : O(1)        Own tests: 2 (see bottom of file)

P, R, T = input().split()
P = float(P)
R = float(R)
T = int(T)

amount = P * (1 + R / 100) ** T
print(f"{amount:.2f}")

# Own tests:
# Input: 1000000 0 50 -> Output: 1000000.00
# Input: 1 100 1       -> Output: 2.00
