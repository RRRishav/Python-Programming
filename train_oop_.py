class Train:

  def __init__(self,name,fair,seats):
    self.name =name
    self.fair = fair
    self.seats = seats

  def getDetails(self):
    print(f"name: {self.name}")
    print(f"fair: {self.fair}")
    print(f"seats: {self.seats}")

  def fareInfo(self):
    print(f"The price of the train is: {self.fair}")


  def Booktick(self):
    if self.seats > 0:
      print(f"your ticket booked seat number {self.seats}")
      self.seats= self.seats -1

    else:
      print("sorry the train is full")


intercity = Train("RAJDHANI",70,300)
intercity.getDetails()
intercity.fareInfo()
intercity.Booktick()
intercity.Booktick()
