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

intercity = Train("RAJDHANI",70,300)
intercity.getDetails()
intercity.fareInfo()
