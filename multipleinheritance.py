class Employee:
  company= "Mphasis"
  ecode = 120


class Freelancer:
  company = "Google"

  def upgLvl(self):
    self.lvl =self.lvl+1

class Programmer(Employee,Freelancer):
  name = "Akanksha"
  lvl =2



p= Programmer()
p.upgLvl()
p.upgLvl()
print(p.company)
print(p.lvl)
