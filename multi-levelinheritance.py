class Person:
  country = "India"

  def takeBreath(self):
    print("i am breathing")


class Employee(Person):
  company = "Mphasis"

  def getSal(self):
    print(f"salary is {self.salary}")

  def takeBreath(self):
    print("i am Employee so i am breathing ")


class Programmer(Employee):
  company = "Google"

  def getSal(self):
    print(f"salary is not found")



p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.company)
programmer = Programmer()
programmer.takeBreath()
