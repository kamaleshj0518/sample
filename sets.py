numbers = {10,20,30,20,10,40}
print(numbers)
numbers.add(50)
numbers.remove(20)
numbers.discard(100)
print(len(numbers))

a = {1,2,3,4,5}
b = {4,5,6,7}
print(a | b)
print(a & b)
print(a - b)
print(b - a)