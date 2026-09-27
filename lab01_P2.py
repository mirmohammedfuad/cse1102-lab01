# Name : Mir Mohammed Fuad             Roll: UG02-71-26-013
# Course : CSE-1102 Foundation of Computer Programming Lab
# Lab : 01        Task: P2 - Name Tag (Post-lab)
# Idea : read first and last name from one line, print as "Last, First".
# Time : O(1)        Own tests: 2 (see bottom of file)

first, last = input().split()
print(f"{last}, {first}")

# Own tests:
# Input: John Smith -> Output: Smith, John
# Input: Md Alamgir -> Output: Alamgir, Md
