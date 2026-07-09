# ATM Machine Simulator

# balance = 10000
# print("Display menu\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
# choice = int(input("Enter your choice : "))

# match choice:
#     case 1:
#         print("Current Balance = ",balance)
#     case 2:
#         deposit_Amount = int(input("Enter the amount : "))
#         current_balance = balance + deposit_Amount
#         print(f"Deposit Successful.\nYour Current balance is {current_balance}")
#     case 3:
#         withdraw_amt = int(input("Enter the amount : "))
#         if(withdraw_amt<balance):
#             bal = balance - withdraw_amt
#             print(f"Withdraw Successful.\nYour Current balnce is {bal}")
#         else:
#             print("Insuffient Balance")
#     case 4:
#         print("Thank You!")
            
            
            
# Student Result Analyzer

# m1 = int(input("Enter Mark 1 : "))
# m2 = int(input("Enter Mark 2 : "))
# m3 = int(input("Enter Mark 3 : "))
# m4 = int(input("Enter Mark 4 : "))
# m5 = int(input("Enter Mark 5 : "))

# total = m1 + m2 + m3 + m4 + m5
# avg = total / 5

# if(m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40):
#     if(avg >= 90):
#         print("Grade : A")
#     elif(avg >= 75):
#         print("Grade : B")
#     elif(avg >= 60):
#         print("Grade : C")
#     elif(avg >= 40):
#         print("Grade : D")
#     else:
#         print("Fail")
# else:
#     print("Fail")
    
    
    
# Password Strength Checker

# password = input("Enter Password : ")
# l = len(password)
# for ch in password:
#     r1 = ch.isdigit()
#     if(r1==True):
#         break
# for ch in password:
#     r2 = ch.isupper()
#     if(r2==True):
#         break
# for ch in password:
#     r3 = ch.isalnum()
#     if(r3==False):
#         break

# if(l>=8 and r1==True and r2==True and r3==False):
#     print("Strong Password")
# else:
#     print("Weak Password")
    
    

# Shopping Cart Bill Generator

# total = 0
# count = 0
# n = 0
# while True:
#     n = int(input("Enter item price : "))
    
#     if(n==0):
#         break
    
#     total += n
#     count += 1
    
# print("Total Bill : ", total)
# print("No of Products : ", count)

# if(total>5000):
#     print("Discount = 20%")
#     discount = (total*20)/100
#     final = total - discount
#     print("Final = ", final)
# elif(total>3000):
#     print("Discount = 10%")
#     discount = (total*10)/100
#     final = total - discount
#     print("Final = ", final)
# else:
#     print("No Discount")
    


# Guess the Secret Number

# secret_number = 27
# i=0
# while(i<5):
#     n = int(input("Guess the Secret Number: "))
#     i += 1
#     if(n > secret_number):
#         print("Too High")
#     elif(n < secret_number):
#         print("Too Low")
#     else:
#         print("Correct")
# if i == 5 and n != secret_number:
#     print("Game Over")



# Employee Salary Processor

# basic = int(input("Basic salary : "))
# exp = int(input("Years of experience : "))
# att = float(input("Attendance percentage : "))

# bonus = 0
# if(exp >= 10):
#     bonus = (basic * 20)/100
# elif(exp >= 5):
#     bonus = (basic * 10)/100
# else:
#     bonus = 0
    
# att_bonus = 0

# if(att > 95.00):
#     att_bonus = 5000
# else:
#     att_bonus = 0
    
# tax = 0
# if basic > 100000:
#     tax = (basic * 10)/100
# elif basic > 50000:
#     tax = (basic * 5)/100
# else:
#     tax = 0
    
# total_bonus = bonus + att_bonus
# final = (basic + total_bonus) - tax
    
# print("Basic Salary : ", basic)
# print("Bonus : ", total_bonus)
# print("Tax : ", tax)
# print("Final Salary : ", final)


# # 7. Movie Ticket Booking System
# n = int(input("How many tickets : "))
# total_price = 0
# child_price = 0
# adult_price = 0
# senior_price = 0
# extra_charge = 0
# discount = 0
# final_price = 0
# for i in range(1,n+1):
#     age = int(input(f"Enter age of person {i} :"))
#     if(age < 12):
#         price = 100
#         child_price += price
#     elif(age > 60):
#         price = 120
#         senior_price += price
#     else:
#         price = 200
#         adult_price += price
        
# total_price = child_price + adult_price + senior_price

# day = input("Choose your day weekend/weekday : ")
# if(day == "weekend"):
#     extra_charge = (total_price*20)/100
#     print("20% Extra charge")
# else:
#     extra_charge = 0
    
# if(n > 5):
#     discount = (total_price*10)/100
#     print("10% Discount")
    
# final_price = total_price + extra_charge - discount
# print(f"final_price is : {final_price:.2f}")
