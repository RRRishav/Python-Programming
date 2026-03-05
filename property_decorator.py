class Employee:
  company = "Mphasis"
  salary = 45
  salbonus =67

  #  totalsal

  @property
  def totalSal(self):
    return self.salary + self.salbonus


e = Employee()
print(e.totalSal)

