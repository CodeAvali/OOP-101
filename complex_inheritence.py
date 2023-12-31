class Monster:
  def __init__(self,health,energy, **kwargs):
    self.health = health
    self.energy = energy
    super().__init__(**kwargs)

  # methods
  def attack(self, amount):
    print('The monster has attacked')
    print(f'{amount} damage was dealt')
    self.energy -= 20 

  def move(self, speed):
    print('The monster has moved')
    print(f'It has a speed of {speed}')

class Fish:
  def __init__(self, speed, has_scales):
    self.speed = speed
    self.has_scales = has_scales
    super().__init__()  #Allows for redundancy

  def swim(self):
    print(f'The fish is swimming at a speed of {self.speed}')

class Shark(Monster, Fish):   #All obj to inherit from should be in class parameter
  def __init__(self, bite_strength, health, energy, speed, has_scales):
    self.bite_strength = bite_strength
    super().__init__(health = health,energy = energy, speed = speed, has_scales = has_scales)

#MRO -> method resolution order
#print(Shark.mro())    #Method does not display in repl.it - use an online compiler for results
#Shark -> Monster -> Fish -> Object


shark = Shark(
    bite_strength = 50, 
    health = 200, 
    energy = 55, 