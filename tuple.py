# goats = ("Cristiano", "Messi", "Neymar", "Zidane", "Pele")
# print(goats[0])
# print(goats[-1])
# print(goats[1:3])
# for goat in goats:
#     print(goat)

# numbers = (10, 20, 10, 30, 10)
# print(numbers.count(10))
# print(numbers.index(30))

# student = ("Kamalesh", 26, "Coimbatore")
# name, age, city = student
# print(name)
# print(age)
# print(city)

# student = ("Kamalesh", 26, "Coimbatore", "Python")
# name, age, city, course = student
# print(f"Name : {name}\nAge : {age}\nCity : {city}\nCourse : {course}")

student = ("Kamalesh", 26, "Coimbatore", "Python")
name, age, *details = student
print(name)
print(age)
print(details)