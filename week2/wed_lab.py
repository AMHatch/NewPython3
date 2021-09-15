# class Student:
#     class Campus:
#         print('DigitalCrafts-Houston')
#     def __init__(self, first_name,last_name):
#         print('i am a constructor')
#         self.first_name = first_name
#         self.last_name = last_name

#     def say_hello(self,first):
#         print(f'Good Morning {self.first_name}!')

# Andrew = Student('Andrew','Hatch')
# Matt = Student('Matt','Fisher')
# Matt.say_hello()

# Victoria = Student('Victoria','Walker')
# Victoria.say_hello()

# Stephen = Student('Stephen',"Doty")
# Stephen.say_hello()

# Mercer = Student('Mercer','Mahaffey')
# Mercer.say_hello()
# Student.Campus()
# Andrew.Campus()



# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print(f'Hello {other_person.name}, I am {self.name}!')
#     def contact(self):
#         print(f"{self.name}'s contact info: Phone:{self.phone} Email: {self.email}")

# sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# jordan = Person('Jordan','jordan@aol.com','495-586-3456')

# sonny.greet(jordan)
# jordan.greet(sonny)

# sonny.contact()
# jordan.contact()

# class Test:
#     def __init__(self):
#         self._a = 'a'





# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color

#     def greeting(self):
#         print('Here are the detail of this car')
    
#     def carDetails(self):
#         print(f'{self.make} {self.color} {self.model}')

# class Hybrid(Car):
#     def __init__(self, mpg,make,model,color): 
#         self.mpg = mpg
#         super(Hybrid, self).__init__(make, model, color)
        
#     def carType(self):
#         print(f'I am a hybrid car and I get {mpg} mpg')

# class Electric(Car):
#     def __init__(self,battery_life,make,model,color):
#         self.battery_life = battery_life
#         super(Electric,self).__init__(make, model, color)

#     def carType(self):
#         print(f'I am an electric car and I have {self.battery_life} range!')


# prius = Hybrid(40,'toyota', 'prius', "lime green")

# prius.carDetails()
# prius.greeting()

# tesla = Electric("100%","Tesla", "Roadster", "Purple")
# tesla.greeting()
# tesla.carDetails()

# tesla.carType()

# class Student:
#     def __init__(self, firstName, lastName, campus):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.campus = campus

#     def printStudent(self):
#         print(f"{self.firstName} {self.lastName} campus: {self.campus}")

