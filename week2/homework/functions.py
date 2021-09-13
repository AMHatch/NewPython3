# #1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List.

# List1 = [1,2,3,4,5,6,-7,8,9,-1,-2,-3,-5]

# def smallest_num(L):
#     i = 0
#     smallest = L[i]
#     for i in range(len(L)-1):
#         if smallest > L[i]:
#             smallest = L[i]
#     return smallest
# print(smallest_num(List1))


#2 Write a function largest that accepts a List of numbers as an argument.
#It should return the largest number in the List.

# List1 = [1,2,3,4,5,6,-7,8,9,-1,-2,-3,-5]
# def largest_num(L):
#     i = 0
#     largest = L[i]
#     for i in range(len(L)-1):
#         if largest < L[i]:
#             largest = L[i]
#     return largest
# print(largest_num(List1))


#3 Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.
# It should return the shortest String in the List.
# List2 = [[1,2,3,4],[1,2],[3,4,5,6,7],[1]]
# def shortest_string(strings):
#     short = strings[0]
#     for i in strings:
#         if len(i) < len(short):
#             short = i
#     return short
# print(shortest_string(List2))

#4 Write a function longest that accepts a List of Strings as an argument.
#It should return the longest String in the List.

# List2 = [[1,2,3,4],[1,2],[3,4,5,6,7],[1]]
# def longest_string(strings):
#     long = strings[0]
#     for i in strings:
#         if len(i) > len(long):
#             long = i
#     return long
# print(longest_string(List2))