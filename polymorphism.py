# class Complex:

#   def __init__(self,real,imag):
#     self.real = real
#     self.imag = imag

#   def showNumber(self):
#     print(f"{self.real}i  + {self.imag}j")

#   def __add__(self,num2):
#     newReal = self.real + num2.real
#     newImag = self.imag + num2.imag
#     return Complex(newReal,newImag)

# num1 = Complex(2,3)
# num2 = Complex(4,5)


# num1.showNumber()
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()


# class Circle:

#   def __init__(self,r):
#     self.r = r

#   def area(self):
#     return 3.14 * self.r * self.r

#   def peri(self):
#     return 2 * 3.14 * self.r

# c = Circle(7)
# print(c.area())



class Order:

  def __init__(self,item,price):
    self.item = item
    self.price = price

  def __gt__(self, odr2):
    return self.price > odr2.price

odr1 = Order("kurkure",20)
odr2 = Order("Chips",25)

print(odr1 > odr2)
















