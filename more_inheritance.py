# class Student:
#   def __init__(self,name):
#     self.name = name

# s1 = Student("Rishav")

# # del s1
# # print(s1.name)


# class Account:


#   def __init__(self,acc_no,acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass# -- make it private

#   def resetPass(self):
#     print(self.__acc_pass)


# acc1 = Account("1234","rianbxsxbsdkd")
# # print(acc1.acc_pass)
# acc1.resetPass()


# class Person:
#   __name = "Akanksha"

#   def __hello(self):
#     print("welcome")

#   def wel(self):
#     self.__hello()

# p = Person()
# # print(p.name)
# p.wel()







# OOPS INHERITANCE


# class Car:
#   color = "Navy"


#   def __init__(self,type):
#     self.type = type

#   @staticmethod
#   def start():
#     print("Car is Started")

#   @staticmethod
#   def stop():
#     print("car is stopped")



# class ToyotaCar(Car):
#     def __init__(self,name,type):
#       super().__init__(type)
#       self.name = name


# car1 = ToyotaCar("fortuner","petrol")
# # car2 = ToyotaCar("Legender")


# print(car1.name)
# print(car1.type)
# car1.start()










#multilevel inheritance




# class Car:


#   @staticmethod
#   def start():
#     print("Car is Started")

#   @staticmethod
#   def stop():
#     print("car is stopped")



# class ToyotaCar(Car):
#     def __init__(self,brand):
#       self.brand = brand



# class Fortuner(ToyotaCar):


#   def __init__(self,type):
#     self.type = type

# car1= Fortuner("Diesel")
# print(car1.type)
# car1.start()








#multiple inheritance

# class A:
#   varA = "welcome to class A"


# class B :
#   varB = "welcome to class B"

# class C(A,B):
#   var= "welcome to the class c"

# c1 = C()

# print(c1.var)
# print(c1.varA)
# print(c1.varB)



# class attribute does not chnage directly

# class Person:
#   name = "Rahul"
#   # def ChangeName(self,name):
#   #   self.__class__.name = name

#   # @classmethod

#   # def changeName(cls,name):
#   #   cls.name = name


# p = Person()
# p.changeName("Rishav")

# print(p.name)
# print(Person.name)






# class Student:

#   def __init__(self,phy,chem,maths):
#     self.phy = phy
#     self.maths = maths
#     self.chem = chem
#     # self.percentage = self.phy + self.maths + self.chem /3


#   # def calPercentage(self):
#   #   self.percentage = self.phy + self.maths + self.chem /3

#   @property
#   def percentage(self):
#     return print(f"{self.phy + self.maths + self.chem /3} %")



# stu = Student(99,56,56)

# (stu.percentage)


























