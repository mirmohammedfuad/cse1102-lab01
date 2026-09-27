# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: B1 - Average of Three
# Idea : read three integer marks from one line, compute the average and
#        print it with exactly 2 digits after the decimal point using an f-string.
# Time : O(1)        Own tests: 2 (see bottom of file)

m1, m2, m3 = map(int, input().split())
average = (m1 + m2 + m3) / 3
print(f"{average:.2f}")

# Own tests:
# Input: 0 0 0     -> Output: 0.00
# Input: 100 100 99 -> Output: 99.67
