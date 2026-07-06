# fav_movies = ["Leo", "Inception", "The Shawshank Redemption", "Interstellar", "The Dark Knight"]
# print(fav_movies[0])
# print(fav_movies[-1])

# marks = [65, 72, 89, 90, 55]
# for mark in marks:
#     print(mark)

# names = ["kamalesh", "Naveen", "Karthick", "Praveen"]
# names.append("Sathish")
# print(names)

# numbers = [10, 20, 30, 40, 50]
# total = 0
# length = len(numbers)
# for number in numbers:
#      total += number

# avg = total / length
# print(avg)

# names = ["Kamalesh", "Naveen", "Praveen"]
# names.insert(2,"Karthick")
# print(names)
# names.remove("Naveen") #remove by value
# # names.pop(1) #remove by index
# print(names)
# names.pop()
# print(names)
# names.reverse()
# print(names)

# marks = [45, 78, 90, 78, 56]
# print(max(marks))
# print(min(marks))
# print(marks.count(78))
# marks.sort()
# print(marks)

# numbers = [15, 10, 20, 10, 30]
# numbers.append(25)
# numbers.insert(0, 5)
# print(len(numbers))
# print(max(numbers))
# numbers.reverse()
# print(numbers)

# marks = [65, 78, 90, 45, 78, 100]
# print(max(marks))
# print(min(marks))
# print(sum(marks))
# print(int(sum(marks) / len(marks)))
# print(marks.count(78))

# names = ["Ram", "Shyam", "Hari"]
# names.append("Kiran")
# names.insert(1, "Arun")
# names.remove("Hari")
# names.reverse()
# print(names)

# nums = [5, 10, 5, 20, 5, 30]

# first = nums.index(5)
# second = nums.index(5, first + 1)
# nums.pop(second)
# print(nums)

nums = []
for i in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)

print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))
print(int(sum(nums) / len(nums)))
nums.sort()
print(nums)