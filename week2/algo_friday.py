# # call stack has last in first out 
# #can only add a function and remove a function once completed

# # callstack =[ global, function1, function2]

# def takeShower():
#     #some more code to execute
#     return "Showering!"


# def eatBreakFast():
#     #some more code to execute
#     meal = cookFood
#     return 'Eating {meal}'


# def cookFood():
#     #some more code to execute
#     items = ["Oatmeal", "Eggs", "Protein Shake"]
#     #some more code to execute
#     return items


# def wakeUp():
#     #some more code to execute
#     takeShower()
#     #some more code to execute
#     eatBreakfast()
#     print("Ok ready to go to work!")


# if(true):
#     #some more code to execute
#     pass


# while True:
#     #some more code to execute
#     pass
    


# wakeUp()

# class stack():
# # Write a function called power which accepts a base and an exponent.
# # The function should return the power of the base to the exponent.
# # 2^3 = 2*2*2


# def power(base,exponent):
#     #base case
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent -1)

#     power(2,4)
#4*3*2*1
# def factorial(a):
#     if a == 0 :
#         return 1
#     return a * factorial(a - 1)

# print(factorial(4))

# 3. Write a function called recursiveRange which accepts a number and adds up all
# the numbers from 0 to the number passed to the function
def recursive_range(n):
    if n == 0 :
        return 0
    return n + recursive_range(n - 1)
print(recursive_range(5))


# 0
# 1 + recursive_range(0)  1 + 0
# 2 + recursive_range(1)  2 + 1 = 3
# 3 + recursive_range(2)  3 + 3 = 6
# 4 + recursive_range(3)  6 + 4 = 10
# 5 + recursive_range(4)  10 + 5 = 15
#recursive_range(5)
