# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: A2 - Sum of Two Numbers
# Idea : read two integers from one line using split()+map(), print a + b.
#        No prompts printed - judge only wants the answer.
# Time : O(1)        Own tests: 2 (see bottom of file)

a, b = map(int, input().split())
print(a + b)

# Own tests:
# Input: 0 0            -> Output: 0
# Input: -1000000000000000000 1000000000000000000 -> Output: 0
