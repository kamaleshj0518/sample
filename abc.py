# name = "kamalesh"
# age = 27
# # print("my name is ", name, "and my age is ", age)
# # print(f"my name is {name} and my age is {age}") # f string formatting
# print((name + " ") * 3)
# print((name + " ") * 2 + name) 
# print(" ".join([name] * 3)) # concatenation of string and integer using casting

#print("Enter your name:")
#name = input()
# print("Enter your age:")
# age = int(input())
# print("Enter your city:")
# city = input()
# print(f"Hello {name}!.\nYou are {age} years old.\nYou are from {city}.")

# print("Enter your name:")
# name = input()
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.strip())

# print("Enter your name:")
# name = input()
# print(name.lower().replace("b", "c"))
# print(name.find("a"))

from sympy import false


age = 20
licence = false
if age>=18 and licence:
    print("you are eligible for driving")
else:
    print("you are not eligible for driving")
