import sys
from datetime import datetime
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import camelcase


# class Red_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Red")

# class Green_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Green")
  

# class Yellow_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Yello")
  

# pomegranate = Red_fruit("pomegranate", "Iran")
# kiwi = Green_fruit("Kiwi", "Poland")
# pineapple = Yellow_fruit("Pineapple", "Spain")


# for fruit in (pomegranate, kiwi, pineapple):
#   print(fruit.color())


# class Fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Red")

# class Green_fruit(Fruit):
#   def color (self):
#     return ("Green")
  
# class Yellow_fruit(Fruit):
#   def color (self):
#     return ("Yello")
  

# pomegranate = Fruit("pomegranate", "Iran")
# kiwi = Green_fruit("Kiwi", "Poland")
# pineapple = Yellow_fruit("Pineapple", "Spain")

# for fruit in (pomegranate, kiwi, pineapple):
#   print(fruit.color())


fruits = ["peach", "pineapple", "grap", "cherry", "Kiwi"]


# try:
#   print("nectarin" in fruits)
# except:
#   print("There is not nectarin in fruits")
# else:
#   print("There is nectarin in fruits")
# finally:
#   print("I like fruits")

# try:
#   for fruit in fruits:
#     if "Kiwi" not in fruits:
#       raise Exception("There is not kiwi")
# except:
#   print("There is not my favorite fruite")
# else:
#   print("I like it")
# finally:
#   print("🥝🥝🥝")



# price_clothes = 30
# total_cost = f"The price of coat is {'Expensive' if price_clothes > 40 else 'cheap'}"
# print(total_cost)


# price = 60
# jacket_price = "The price of this coat is {}"
# total_cost = jacket_price.format(price)
# print (total_cost)


# price = 60
# jacket_price = "The price of this coat is {:.2f}"
# total_cost = jacket_price.format(price)
# print (total_cost)


# price = 60.12
# quantity = 3

# notebook_price = "I want to buy {} pieces of notebooks and they have {:.2}"
# total_cost = notebook_price.format(quantity, price)
# print (total_cost)


# quantity = 3
# price = 60.54

# notebook_price = "I want to buy {0} pieces of notebooks and they have {1:2}"
# total_cost = notebook_price.format(quantity, price)
# print (total_cost)


# print("Enter your firstname")
# name = input("Your name please")
# lastname = input("Your lastname please")
# age = input("Your age please")
# city = input("Your city please")
# country = input("Your country please")
# print(f"Hello {name} {lastname}. You are {age} years old and you was borne in {city} from {country}")

# text_file = open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt")
# print(text_file.read())

# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   print(text_file.read())


# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   print(text_file.read(4))




# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   print(text_file.readline())
#   print(text_file.readline())
#   print(text_file.readline())
#   print(text_file.readline())



# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   for line in text_file:
#     print(line)

# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt", "a") as text_file:
#   text_file.write("Wow I can writ on it")

# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   print(text_file.read())
 
# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt", "w") as text_file:
#   text_file.write("Nice job")

# with open(r"C:\Users\sahar\OneDrive\Desktop\Test.txt") as text_file:
#   print(text_file.read())
 
# with open(r"C:\Users\sahar\OneDrive\Desktop\Example.txt", "w") as example:
#   example.write("Nice job")

# with open(r"C:\Users\sahar\OneDrive\Desktop\Example.txt") as example:
#   print(example.read())

# if os.path.exists(r"C:\Users\sahar\OneDrive\Desktop\Example.txt"):
#   os.remove(r"C:\Users\sahar\OneDrive\Desktop\Example.txt")
# else :
#   print("The file is not exist")


# print(matplotlib.__version__)

xpoints = np.array([0,5,6,9,20, 9,50,10,7])
ypoints = np.array([0,10, 20, 8,6, 30 ,23,15, 40])

# graph = plt.plot(ypoints, marker="D")
# plt.title("Uv index")
# plt.show()

# # the itterval lines are dotted 
# graph = plt.plot(ypoints, "D-.b", ms = 6) 
# plt.title("Uv index")
# plt.show()

# the itterval lines are dotted 
graph = plt.plot(xpoints, ypoints, color = "#ab1465", linewidth = "2")

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.xlabel("Uv index")
plt.ylabel("Time of day")
plt.title("UV degree", fontdict= font1, loc="left")
plt.show()