#class is a container to hold variables and functions
# a template for what we are going to do.
#instantiation is creating an object from the template.

class Student:
    # constructior is called as soon as an object is created from a class
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    #function in a class is a 
    def say_hello(self):
        print(f'Hello World {self.first_name} {self.last_name}')


Matt = Student('Matt','Fisher')
# Matt.say_hello()

Victoria = Student('Victoria','Walker')
Victoria.say_hello()

# Stephen = Student('Stephen',"Doty")
# # Stephen.say_hello()

# Mercer = Student('Mercer','Mahaffey')
# # Mercer.say_hello()






