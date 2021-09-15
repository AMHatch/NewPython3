# #1
# def greeting():
#     print('Andrew')
# #2
# greeting()
# #3
# # print("Day 1: Students in SRE class")
# # print("lecture: git 101")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")
# # print("Day 2: Students in SRE class")
# # print("lecture: git 102")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")
# # print("Day 3: Students in SRE class")
# # print("lecture: python 101")
# # print("Shu")
# # print("Thomas")
# # print("Gustavo")
# # print("Alim")

# def students():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")


# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# students()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# students()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# students()

# #4
# # Create a function that creates the following recommendation letter.
# # The Parameters for the functions should be the first and last name person you
# # are recommending

# # Karen Jones
# # 1234 Park St
# # Anytown, Pennsylvania 12345

# # April 14, 2019

# # ABC College Admission’s Board
# # 1234 Butler Ave
# # Everywhere, CA 12345

# # Dear ABC College Admission’s Board:

# # My name is Karen Jones. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as Ryan Thomas’s teacher for the past three. 
# # I have also been Ryan’s advisor on the science academic team here at school. Due to his qualifications, I feel that Ryan would be an excellent addition to your school.

# # While he has been a student here, Ryan has always challenged himself academically, taking all of the AP courses that our school has to offer.
# # He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# # Ryan would bring much to your school, both in and out of the classroom. If you have any questions regarding Ryan’s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# # Sincerely,


# # Karen Jones
# # Science Department Head
# # Park Town High School

# def recommendation(first1,last1,first,last):
#     print(f'''

# {first1} {last1}
# 1234 Park St
# Anytown, Pennsylvania 12345

# April 14, 2019

# ABC College Admission’s Board
# 1234 Butler Ave
# Everywhere, CA 12345

# Dear ABC College Admission’s Board:

# My name is {first1} {last1}. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {first} {last}’s teacher for the past three. 
# I have also been {first}’s advisor on the science academic team here at school. Due to his qualifications, I feel that Ryan would be an excellent addition to your school.

# While he has been a student here, {first} has always challenged himself academically, taking all of the AP courses that our school has to offer.
# He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# {first} would bring much to your school, both in and out of the classroom. If you have any questions regarding {first}’s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# Sincerely,


# {first1} {last1}
# Science Department Head
# Park Town High School

#     ''')






# def name(first,last):
#     print(f'My name is {first} {last}')

# name(Andrew,Hatch)

# Temperature Conversions

def to_fahrenheit(C):
    F = (1.8 * C) + 32
    result = f"{F} degrees Fahrenhiet"
    return print(result)

def to_Celcius(F):
    C =(F-32)*(5/9)
    result = f"{C} degrees Centigrade"
    return print(result)

unit = input("Is your current unit F or C?")
unit.upper
temp = float(input("what is the temperature?"))

if unit == 'F':
    to_Celcius(temp)
elif unit == 'C':
    to_fahrenheit(temp)

