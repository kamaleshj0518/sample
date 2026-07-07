# student = {
#     "name": "Kamalesh",
#     "age": 26,
#     "city": "Coimbatore"
# }
# print(student)
# print(student["name"])
# student["age"] = "27"
# student["course"] = "Python"
# student.pop("city")
# print(student)
# for key in student:
#     print(key)    
# for value in student.values():
#     print(value)
# for key, value in student.items():
#     print(key, ":", value)
    
student = {
    "name": "Kamalesh",
    "age": 26,
}
    
print(student.get("name"))
print(student.get("age"))
print(student.get("city", "City Not Available"))
student["course"] = "Python"
print(student)