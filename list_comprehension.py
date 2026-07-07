# a = [i*5 for i in range(1,6)]
# print(a)

# b = [i*2 for i in range(1,7)]
# print(b)

# c = [i for i in range(1,20) if i % 3 == 0]
# print(c)

# numbers = [1, 2, 3, 4, 5]
# double = [i*2 for i in numbers]
# print(double)

#task
numbers = [10, 15, 20, 25, 30]
a = [i for i in numbers if i % 10 == 0]
print(a)

def square(x):
    return x * x

s = [2, 4, 6]
result = list(map(square, s))
print(result)

student = {
    "name": "Kamalesh",
    "age": 26,
    "city": "Coimbatore"
}

student["Course"] = "Python"
student.pop("city")

for key in student:
    print(key)
    
for value in student.values():
    print(value)
    
def biggest(a,b):
    if(a > b):
        return a
    else:
        return b
    
print(biggest(15,9))
