# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: C1 - Bill Splitter
# Idea : read bill B, number of friends N and tip percent P on separate
#        lines; add the tip to the bill, divide equally by N, print with 2 decimals.
# Time : O(1)        Own tests: 2 (see bottom of file)

B = float(input())
N = int(input())
P = float(input())

total = B * (1 + P / 100)
each = total / N
print(f"Each pays: {each:.2f}")

# Own tests:
# Input: 1 / 1 / 0     -> Output: Each pays: 1.00
# Input: 1000000 / 100 / 100 -> Output: Each pays: 20000.00
