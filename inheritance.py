#use to preserve DRY PRINCIPLE -> DONOT REPEAT YOURSELF

#single inheritance


class Employee:
  company = "Mphasis"


  def showDetails(self):
    print("this is an employee")

class Programmer(Employee):

  language = "python"
  #company = "Google"

  def GetName(self):
    print(f"The language is {self.language}")

  def showDeatils(self):#overiding
    print("show")



e = Employee()
p = Programmer()
e.showDetails()
p.showDeatils()
p.GetName()
print(p.company)
