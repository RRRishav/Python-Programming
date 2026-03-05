class Employee:
  company = "Reynolds"
  salary= 200
  location = "Delhi"

  # def changeSal(self,salary):
  #   self.__class__.salary=salary

  @classmethod
  def changeSal(cls,salary):
    cls.salary=salary



e = Employee()

print(e.salary)
e.changeSal(300)
print(e.salary)

