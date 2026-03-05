#objects oriented programming


#class is blueprint of creating object
#object is instance of class
# __init__ is constructor which is used to initialize the object
# self act like wiring which connect the object to the class

#procedure oriented programming
# a = 12
# b= 44

# print(a+b)



#object oriented programming -> DRY -> Don't Repeat Yourself -> principal of software development

# class Number:
#     def sum(self):
#       return self.a + self.b
# num = Number()
# num.a = 12
# num.b = 44
# s =num.sum()
# print(s)


# class Employee:
#   pass




# e =  Employee()#object initialtion
# print(e)





















# class RailwayForm:
#   formType = "RailwayForm"

#   def printData(self):
#     print(f"The name is {self.name}")
#     print(f"The train is {self.train}")



# Risha = RailwayForm()
# Risha.name = "Rishav"
# Risha.train = "Rajdhani Express"
# # Risha.age =  22
# Risha.printData()





# ********************/

# import pandas as pd

# dataframe is a class in pandas library which is used to store data in tabular form
# pd.DataFrame()


#***********************/





#****class attribute *******

# class Employee:
#   company = "Mphasis"


# rishav = Employee()
# rajni = Employee()
# rishav.company
# print(rishav.company)
# Employee.company = "Google"
# print(rajni.company)


#********instance attribute*******


# class Employee:
#   addresss = "Bangalore"# class attribute
#   company = "Mphasis"
#   salary = 100# second it will check for class attribute if instance attribute is not found then it will check for class attribute


# rishav = Employee()
# rajni = Employee()
# rishav.salary = 100000# first it will check for instance attribute if it is not found then it will check for class attribute
# rajni.salary = 20000
# print(rishav.salary)
# print(rajni.salary)
# print(rajni.addresss)


#********self****


# class Employee:
# #   company = "Mphasis"
#   def getSal(self):
#     print(f"salary of rishav is  {self.salary}")




# rishav = Employee()
# rishav.salary = 1000000
# # rishav.getSal()
# Employee.getSal(rishav)



















# # static method



# class Employee:
#   company = "Mphasis"
#   def getSal(self,sig,name):
#     print(f"salary of rishav is  {self.salary} and {sig} weeds {name}")

#   @staticmethod
#   def greet():
#     print("Good Morning")




# rishav = Employee()
# rishav.salary = 1000000
# rishav.getSal("Akanksha","Rishav")

# rishav.greet()


















# #__init__  constructor method






# class Employee:
#   def __init__(self,name):
#     self.name = name



# r = Employee("Rishav")



# more example of constructor



# class Employee:
#   company = "Mphasis"


#   def  __init__(self,name,salary,subunit):
#     self.name = name
#     self.salary = salary
#     self.subunit = subunit
#     print("Constructor is called")



#   def getDetails(self):
#     print(f"The name of employee is {self.name}")
#     print(f"The salary of employee is {self.salary}")
#     print(f"The subunit of employee is {self.subunit}")


#   def getSal(self):
#     print(f"salary of rishav is  {self.salary}")

#   def greet():
#     print("Good Morning")




# rishav = Employee("Akanksha",1000000,"AI")
# rishav.getDetails()

# class Employee:

#     def __init__(self,name,salary,subunit):
#         self.name = name
#         self.salary = salary
#         self.subunit = subunit
#         print("Constructor is called")

# emp1 = Employee("Rishav",1000000,"IT")


# class Employee:

#     def __init__(self, name, salary, subunit):
#         self.name = name
#         self.salary = salary
#         self.subunit = subunit
#         print("Constructor is called")

#     def printDetails(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Subunit:", self.subunit)


# emp1 = Employee("Rishav", 1000000, "IT")
# emp1.printDetails()
