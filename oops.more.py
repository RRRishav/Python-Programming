# class Student:#creating class
#   name = "Rishav"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)




# class Car:
#   color= "black"


# car1 = Car()
# print(car1.color)










#constructor object creation


# class Student:

#   collegeName = "TIET PATIALA"
#   #name = "anony"
#   def __init__(self):
#     pass

#   def __init__(self,fname,love,place):
#     self.fname = fname #obj attr > class attr
#     self.love = love
#     self.place = place
#     #print(self)
#     print(f"creating new weeding {fname} with loves {love} and place is {place}")

#   @staticmethod
#   def hello():
#     print("hello")

#   def welcome(self):
#     print(f"Congratulations to {self.fname} and {self.love}")

#   def palce(self):
#     return self.place

# s1 = Student("Rishav","Akanksha sharma","Banglore")
# print(s1.fname)
# s1.hello()
# s1.welcome()
# print(s1.palce())
# print(s1.collegeName)




class Student:

  def __init__(self,name1,name2,name3,mark1,mark2,mark3):
    self.name1 = name1
    self.name2 = name2
    self.name3 = name3
    self.mark1 = mark1
    self.mark2 = mark2
    self.mark3 = mark3

  def getDeatails(self):

    print(f"details are {self.name1}, {self.name2} {self.name3}")

  def marksAVG(self):
    return (self.mark1+ self.mark2 + self.mark3)/300 * 100


s1 = Student("Rishav","Akanksha","Harsh",91,23,43)
s1.getDeatails()
print(s1.marksAVG())





