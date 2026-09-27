# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: C2 - Sum of N Numbers on One Line
# Idea : read N (unused for logic but part of the contest input format),
#        read N space-separated integers into a list, print their sum.
# Time : O(N)        Own tests: 2 (see bottom of file)

n = int(input())
nums = list(map(int, input().split()))
print(sum(nums))

# Own tests:
# Input: 1 / -1000000000        -> Output: -1000000000
# Input: 3 / -4 4 10             -> Output: 10
