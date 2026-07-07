# def hello():
#     print("Hello Buddy!\nWelcome to Python.")
    
# for i in range(3):
#     hello()
    
# def greet(name):
#     print(f"Hello {name}")
    
# greet("Kamalesh")
# greet("Naveen")
# greet("Cristiano")

# def add(a,b):
#     print(f"Addition of {a} and {b} is : {a+b}")
    
# add(10, 20)
# add(50, 100)
# add(25, 75)

# def multiply(a,b):
#     return a * b
    
# answer = multiply(10, 5)
# print(answer)

# def square(num):
#     return num * num
    
# print(square(4))
# print(square(7))
# print(square(12))

# student = {
#     "name": "Kamalesh",
#     "marks": [85, 90, 78, 92, 88]
# }

# def total_marks(marks):
#     return sum(marks)

# def average_marks(marks):
#     return sum(marks) / len(marks)

# def display(student):
#     print(f"Name : {student['name']}")
#     print(f"Marks : {student['marks']}")
#     print(f"Total Marks : {total_marks(student['marks'])}")
#     print(f"Average Marks : {average_marks(student['marks'])}")
# display(student)

# def analyze_numbers(*nums):
#     Numbers = list(nums)
#     print(f"Numbers : {Numbers}")
#     print(f"Maximum : {max(Numbers)}")
#     print(f"Minimum : {min(Numbers)}")
#     print(f"Sum : {sum(Numbers)}")
#     print(f"Average : {sum(Numbers) / len(Numbers):.2f}")
#     print(f"Sorted : {sorted(Numbers)}")
    
#     even = []
#     odd = []
#     for num in Numbers:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
            
#     print(f"Even : {even}")
#     print(f"Odd : {odd}")
            
# analyze_numbers(10, 5, 8, 20, 15, 7)

def cube(x):
    return x * x * x

numbers = [1, 2, 3, 4, 5]
result = list(map(cube, numbers))
print(result)

def add10(x):
    return x + 10

numbers = [5, 10, 15, 20]
result = list(map(add10, numbers))
print(result)