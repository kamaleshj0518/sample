# Movie Ratings

# ratings = (4,5,3,5,4)
# print(f"First rating : {ratings[0]}")
# print(f"Last rating : {ratings[-1]}")
# print(f"Sum of ratings except the first one : {sum(ratings[1:])}")
# sum = sum(ratings)
# avg = sum/len(ratings)
# if avg >= 4:
#     print("Excellent Movie")
# else:
#     print("Good Movie")


# Music Playlist

# friend1 = {"Believer", "Perfect", "Shape of You", "Faded"}
# friend2 = {"Perfect", "Faded", "Senorita", "Levitating"}
# print(f"Songs liked by both : {friend1 & friend2}")
# print(f"All Unique Songs : {friend1 | friend2}")
# print(f"Songs liked only by friend 1 : {friend1 - friend2}")
# if "Believer" in friend2:
#     print("Yes, Believer is liked by friend2")
# else:
#     print("No, Believer is not liked by friend2")

# print(f"No.of Unique Songs : {len(friend1 | friend2)}")

# Library Books

# shelf1 = {"Python", "Java", "C++", "HTML"}
# shelf2 = {"Python", "JavaScript", "CSS", "HTML"}
# print(f"Books available on both shelves : {shelf1 & shelf2}")
# print(f"Books available only on shelf2 : {shelf2 - shelf1}")
# print(f"All available Books : {shelf1 | shelf2}")
# if "Java" in shelf2:
#     print("Yes, java is available on shelf2")
# else:
#     print("No, java is not available on shelf2")
 
# print(f"No.of books available in total : {len(shelf1 | shelf2)}")

# tuple + set

# students = (("Arun", "Red"), ("priya", "Blue"), ("John", "Red"), ("Meena", "Green"), ("Kavin", "Blue"))
# count = 0
# houses = set()
# for i in students:
#     houses.add(i[1])
# print(houses)

# for i in students:
#     if i[1] == "Red":
#         count = count + 1
    
# print(f"No.of students belongs to Red house : {count}")

# if "Yellow" in houses:
#     print("Yello house exists")
# else:
#     print("Yellow house not exist")