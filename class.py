from collections import OrderedDict
from abc import ABC
# import cowsay

# cowsay.cow("Good Mooooorning!")
# 
# # inheritance 
# class Flower_information:
#   def __init__(self, name, color, country):
#     self.name = name
#     self.color= color
#     self.country = country

#   def flower_name (self):
#     return f"this {self.name} is one of the nice flower you can find here"


# class Flower_color():
#   def flowe_color(self):
#     return f"The {self.name} has {self.color} and in this season it is really nice."


# class Flower_location(Flower_information, Flower_color):
#   def flower_location(self):
#     flower_details = f"The {self.name} has {self.color} color and you can find it in {self.country}."
#     return flower_details

# rose_flower = Flower_location("Rose", "Red", "Iran")
# print(rose_flower.flower_name())
# print(rose_flower.flowe_color())
# print(rose_flower.flower_location())


# inverted_tulip = Flower_location(" inverted tulip", "Red", "Iran")
# print( inverted_tulip.flower_name())
# print( inverted_tulip.flowe_color())
# print( inverted_tulip.flower_location())


## OOP principles / polymorphism 
# class Cat_sound:
#   def sound(self):
#     meow_sound = f"Cats make sound like Meaw"
#     return meow_sound

# class Dog_sound(Cat_sound):
#   def sound(self):
#     bark_sound = f"Dogs are barking"
#     return bark_sound
  
# class Rosster_sound(Cat_sound):
#   def sound(self):
#     ghooghooli_sound = f"Rossters are making sound like ghooghooli ghooghoo"
#     return ghooghooli_sound

# animal_sound = [Cat_sound(), Dog_sound(), Rosster_sound()]

# for sound in animal_sound:
#   print(sound.sound())

# ## encapsulation 

# class Car:
#   def __init__(self, name, model, number):
#     self.name = name
#     self._model = model
#     self.__number = number
#   def get_number(self):
#     return self.__number
#   def set_number(self, number):
#     if number > 4000:
#       self.__number = number
#     else : 
#      self.__number = 2000
  

# class Car_advertisement(Car):
#   def car_announcement(self):
#     result = f"We can see the result"
#     return result

# BMW = Car ("BMW", "16464jk", 1000); 
# print(BMW.name)
# print(BMW._model)
# print(BMW.get_number())
# print(BMW.set_number(3000))
# print(BMW._Car__number)
# # print(BMW.__number)


# BMW = Car_advertisement ("BMW", "16464jk", 2500); 
# print(BMW.name)
# print(BMW._model)
# print(BMW.get_number())
# print(BMW.set_number(800))
# print(BMW._Car__number)
# # print(BMW.__number)


# ####################

# car_model = "BMW '12358KJ'"
# print(car_model)

# for element in car_model:
#   print(element)


# Break lines example
scadual_class = """We have programming class \n from Monday to Friday everyday except \n weekend days"""
print(scadual_class)
print(scadual_class.find("d"))

# Boolean example 
programming_language_classes = "We have C++ and JavaScript class in this semester"

if "Python" in programming_language_classes:
  print("Python")
elif "JavaScript" in programming_language_classes:
 print("I can select JavaScript")

#  Split string
car_information = "Volvo c14564"
splited_information = car_information.split(" ")
print(splited_information)

if 'Benze' in splited_information:
  print("What is the model of Benz")
else: print("this Car is not Benz")


