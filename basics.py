# print("""
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.""")





# import os

# print(os.listdir())




# a = 30
# print(a)

# b= 7.00

# print(b)
# print(type(b))

# name = "Rishav weeds Akanksha"
# print(name)

# print(type(a))




# name = "Akanksha"
# print(f"hello {name} I love you from rishav")

# z = True
# print(z)


# count = input("Dead Count:\n")
# injured = input("Injured Count:\n")
# safe = input("Safe Count:\n")

# if count < 0 or safe < 0 or injured < 0:
#   print("Invalid input")
# else:
#   print("TSUNAMI REPORT OF JAPAN")
#   print("The number of people")
#   print(f"Dead: {count}")
#   print(f"Injured: {injured}")
#   print(f"Safe: {safe}")
#   print("Please help the people  who are suffering!!!")



# age = int(input("Enter visitor age:\n"))

# if age < 0:
#   print("Invalid input")

# elif age <= 12:
#   print("Visitor Type: Child")
#   print("Ticket Price: $100.00")

# elif age >=13 and age <= 64:
#   print("Visitor Type: Adult")
#   print("Ticket Price: $200.00")

# else:
#   print("Visitor Type: Senior")
#   print("Ticket Price: $150.00")




# amount = int(input("Enter amount:"))
# choice = int(input("Enter denomination choice"))

# if amount < 0 or choice < 1 or choice > 3:
#   print("Invalid input")

# elif choice == 1:
#   denom = 100
# elif choice == 2:
#   denom = 200
# elif choice == 3:
#   denom = 500
# else:
#   print("Invalid input")
#   exit()

# if amount < denom:
#   print(f"Balance amount of ${amount} has beeen returned")
# else:






# import re
# id = input("Enter your ID:\n")
# pattern = r"^(DH|DM)-\d{4}$"

# if re.match(pattern,id):
#   print("Valid ID")
# else:
#   print("Invalid ID")



# import re
# statement = input("Enter a statement:\n")
# pattern = r"\b\d+\b"

# numbers = re.findall(pattern, statement)
# print(numbers)











# try:
#   a=int(input("Enter First number:"))
#   b=int(input("Enter Second number:"))
#   op=input("Enter operator (+, -, *, /):")

#   if op == '/':
#     print("The answer is:",a/b)

#   elif op == '+':
#     print("The answer is:",a+b)

#   elif op == '-':
#     print("The answer is:",a-b)

#   elif op == '*':
#     print("The answer is:",a*b)

#   else:
#     raise KeyError

# except KeyError:
#   print("Invalid operator")
# except ZeroDivisionError:
#   print("Cannot divide by zero")
# except ValueError:
#   print("Invalid input, please enter a number")



# class AgeException(Exception):
#     pass

# class SalaryException(Exception):
#     pass


# try:

#   name = input("Enter employee name:\n")
#   age = int(input("Enter employee age:\n"))
#   salary= int(input("Enter employee salary:\n"))
#   gender = input("Enter employee gender (M/F):\n")

#   if age < 18 or age >50:
#     raise AgeException("Invalid age")

#   if salary < 0:
#     raise SalaryException("Invalid salary")

# except AgeException:
#   print(AgeException)
# except SalaryException:
#   print(SalaryException)
# finally:
#   print("Best Wishes")






# a = " 334"
# a =  int(a)
# print( a + 5 )






# # a = int(input("Enter a number:\n"))
# # b = int(input("Enter another number:\n"))

# # print(f"Average of {a} and {b} is {(a+b)/2}")





# name = "AKANKSHA"
# print(name[0:2])
# print(print(bool))


# gretting = "Hello, World!"
# name = "Rishav"

# c= gretting + " " +name
# print(c)

# # or
# print(f"{gretting} {name}")


# print(name[-1])

# # you cannot change string character


# dream = "sde"
# print(dream[1:])

# word = "amazing"
# # print(word[0:3:2])
# print(len(word))


# story = "Harry is good.\n " \
# "he is a good boy."


# name = input("Enter your name")
# print(f"good afternoon {name}")


# ques ->To detect double space
# st = "this is a string   with double space"
# doublespace = st.find("  ")

# print(doublespace)


# friends = ["Rishav", "Akanksha", "Ayasha"]
# print(friends[0])
# print(friends[1])
# print(friends[2])
# for ch in range(len(friends)):
#    print(ch)


# #you can create lsit [] bracket print the list you can chnage items in the list

# we can crate list of item of differnet type

# c = [1, 2.5, "Rishav", True ]
# # for i in range(len(c)):
# #    print(c[i])
# sorted_list = sorted(c)
# print(sorted_list)
# print(c[0:3])#slcingin the list
# l1 =[2,35,454,656,56,1]
# # l1.sort()
# # l1.reverse()
# l1.append(100)
# # print(l1)


# t = (1,2,4,5)

# # for g in t:
# #   print(g)


# print(t.count(1))
# print(t.index(4))


#Dictionary


# collection of key value pairs



myDict = {
  "name":"Akanksha",
  "name2":"Rishav",
  "marks":[90, 95, 85],
 }

# print(myDict["name"])
# print(myDict["name2"])
# print(myDict["marks"])


# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
# for items in myDict.items():
#   print(items)
# print(myDict.get("name"))
# myDict.update({"name1":"Ayasha"})
# print(myDict)
#
#sets

# s = set()
# s.add(1)
# s.add(2)
# print(s)


# a = {1,2,3,4,3,4,5,}
# print(a)
# print(type(a))



# empty set

# s = set()
# s.add("Rishav")
# s.add("Rishav")
# s.add(1)
# print(s)
# print(len(s))
# s.remove(1)
# print(s)
# print(len(s))
# set is collection of not repitive items
# you can put tuple inside set not list or dict


#conditional expression



# # a = 45
# # if a > 4:
# #   print("a is greater than 3")
# # elif a > 7:
# #   print("a is greater than 7")
# # else:
# #   print("a is less than or equal to 3")

# # print("donde")

# num = int(input ("Enter a number:\n"))
# for i in range(1,11):
#   print(f"{num} * {i} = {num * i}")






# l= ["saju","smason"]

# for i in l:
#   if i.startswith("s"):
#     print(i)



#prime number
# number = int(input("Enter a number:\n"))

# for i in range(2, number):
#     if number % i == 0:
#         print(f"{number} is not a prime number")
#         break
# else:
#     print(f"{number} is a prime number")


# sum of n natural
# num = int(input("Enter a number:\n"))
# sum =0
# for i in range(1,num+1):
#   sum = sum+i
# print(f"The sum of first {num} natural number is {sum}")





#factorial
# num = int(input("Enter a number:\n"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")


# marks = [90, 95, 85, 80, 75]

# percentage = (sum(marks)/len(marks))
# print(f"The percentage is {percentage}%")


# def percent(marks):
#   p= (sum(marks)/len(marks))
#   return p

# marks = [90, 95, 85, 80, 75]
# marks2 = [80, 85, 90, 95, 100]
# print(f"The percentage is {percent(marks2)}%")


# def greet(name="Akanksha"):
#   print(f"good days {name}")
# greet()


# def sum(num1, num2):
#   return num1 + num2

# a= int(input("Enter first number:\n"))
# b= int(input("Enter second number:\n"))
# print(f"the sum of {a} and {b} is {sum(a,b)}")


# n = int(input("Enter a number:\n"))
# def factorial(n):
#   if n ==0 or n==1:
#     return 1
#   else:
#     return n * factorial(n-1)

# print(f"The factorial of {n} is {factorial(n)}")

# def gratest(a,b,c):
#   if  a> b and a>c:
#     return a
#   elif b> a and b> c:
#     return b
#   else:
#     return c

# a= int(input("Enter first number:\n"))
# b= int(input("Enter second number:\n"))
# c= int(input("Enter third number:\n"))

# print(f"The greatest number among {a}, {b} and {c} is {gratest(a,b,c)}")


# print("akanksha",end ="\n")
# print("rishav")

# n = int(input("Enter a number:\n"))
# def sum_natural(n):

#   if n == 1:
#     return 1
#   else:
#     return n + sum_natural(n-1)


# print(f"The sum of first {n} natural number is {sum_natural(n)}")



# strip() remove extra space



# n = int(input ("Enter a number:\n"))

# def table(n):
#   for i in range(1,11):
#     print(f'{n} * {i} = {n * i}')


# print(f"The multiplication table of {n} is: {table(n) }")



#snake water gun game
# import random

# choices = ["snake", "water", "gun"]

# computer = random.choice(choices)
# user = input("Enter snake, water, or gun: ")

# print("Computer chose:", computer)

# if user == computer:
#     print("Match Draw")

# elif (user == "snake" and computer == "water") or \
#      (user == "water" and computer == "gun") or \
#      (user == "gun" and computer == "snake"):
#     print("You Win")

# elif user in choices:
#     print("Computer Wins")

# /



# File

#read content of file
#by defaultmode is r
# f = open('smaple.txt','r')
# data=f.read()
# print(data)
# # f.close()


# ********readline function**************



# f = open('smaple.txt','r')
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()


# write to file

# f = open('another.txt','w')
# f.write("This is a new file created by python\n")
# f.close()


# append to file
f = open('another.txt','a')
f.write("i am aing\n")
f.close()


