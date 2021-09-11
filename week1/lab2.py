# planet1 = "Earth"
# planet2 = "Jupiter"
# planet3 = "Neptune"
# planet4 = "Mars"
# planet5 = "Saturn"
# planet6 = "Mercury"
# planet7 = "Uranus"
# planet8 = "Venus"


# #1

planets=['earth','jupiter','neptune','mars','saturn','mercury','uranus','venus']

# #2 

# print(len(planets))

# #3

#index = 0

# while index < len(planets):
#     print(planets[index].lower())
#     index += 1

# #4

# planets.append('pluto')

#5

HoustonCities = ["Katy", "Memorial City", "Sugar Land","The Heights", "River Oaks", "Pasadena"]
ClearLakeCities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

Houston = HoustonCities + ClearLakeCities


# print(len(Houston))
# index = 0
# while index < len(Houston):
#     print(Houston[index])
#     index += 1




# #6

# planets.pop()
# or
# del planets[-1]
# #7

# htx1 = Houston[:4]
# htx2 = Houston[2:6]
# htx3 = Houston[-2:]

# #8 

# Houston.insert(4,"Denver")

# #9

# Houston.pop()

# #10

# Houston.index('Seabrook')

# #11

# Houston.sort()

#12 SKIP?

USCities = Houston.copy()


#13

# Houston.clear()

#14
# nums = [4, 5, 7, 8]

# nums5 = nums * 5

#15 
# string = "Digital Crafts"
# list_string = list(string)
#smarter not harder
# backwards = "".join(reversed(list_string))

#without build in methods
# backwards_string = ''
# index = (len(list_string) -1)
# while index >= 0 :
#     backwards_string += list_string[index]
#     index -= 1
# print(backwards_string)                       


# #16 
# for number in range(6):
#     print(number)
# #17
# for number in range(6,17,2)
#     print(number)
#18
# for planet in planets: 
#     print(planet)
# #19
# for city in USCities:
#     print(city)

# #20 
# for i in range(6,17,2):
#     print(i * 5)
    
#21
# for i in range(1,11):
#     # c = 1 * i
#     # print(f'1 x {i} = {c}')
chapters = ['Python', 'Javascript', "HTML/CSS", "Node", "React", "Redux"]

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]


for chapter in chapters:
    print(f"Chapter:{chapter}")
    for day in days: 
        print(day)










# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

# MAIN_MENU = """
# Choose an action:
# P: Print your to-do list
# A: Add a to-do item
# (Or press Enter to exit the program.)
# """

# choice = input(MAIN_MENU)
# choice = choice.upper() 

# while len(choice) > 0:
#     if choice == "P":
    
#         print("To do:")
#         count = 1
#         for todo in todos:
#             print("%d: %s" % (count, todo))
#             count += 1
#     elif choice == "A":
#         new_todo = input("What do you need to do? ")
#         if len(new_todo) > 0:
#             todos.append(new_todo)
#             count = 1
#             print("%d: %s" % (count, new_todo))
#     else:
#         print("***Please enter a valid menu option.***")    

#     choice = input(MAIN_MENU)
#     choice = choice.upper() 

# print("To do:")
# count = 1
# for todo in todos:
#     print("%d: %s" % ( count, todo))
#     count += 1
# print('Have a nice day')


