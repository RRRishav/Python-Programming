class Employee:
  company = "Mphasis"
  salary = 45
  salbonus =67

  #  totalsal

  @property
  def totalSal(self):
    return self.salary + self.salbonus

  @totalSal.setter

  def totalSal(self,val):
    self.salbonus  = val  - self.salary



e = Employee()
print(e.totalSal)
e.totalSal = 56
print(e.salary)
print(e.salbonus)
