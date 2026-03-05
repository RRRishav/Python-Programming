class Person:


  def __init__(self):
    print("Initialsie person...|\n")



  country = "India"

  def takeBreath(self):
    print("i am breathing")


class Employee(Person):
  company = "Mphasis"


  def __init__(self):
    super().__init__()
    print("Employee person...|\n")




  def getSal(self):
    print(f"salary is {self.salary}")

  def takeBreath(self):
    super().takeBreath()
    print("i am Employee so i am breathing ")


class Programmer(Employee):
  company = "Google"

  def __init__(self):
    super().__init__()
    print("Programmer person...|\n")


  def getSal(self):
    print(f"salary is not found")

  def takeBreath(self):
    super().takeBreath()
    print("i am Programmer so i am breathing ")



p = Person()
# p.takeBreath()

e = Employee()
e.takeBreath()

programmer = Programmer()
# # programmer.takeBreath()
