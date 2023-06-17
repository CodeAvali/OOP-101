class Monster:
  def __init__(self,health,energy):
    self.health = health
    self.energy = energy 

  def attack(self, amount):
    print("The monster has attacked")
    print(f'{amount} damage was dealt')
    self.energy -= 20 

  def move(self, speed):
    print("The monster has moved")
    print(f'It has a speed of {speed}')

class Shark(Monster):
  def __init__(self, speed, health, energy):
    #Monster.__init__(self,health,energy)
    super().__init__(health,energy)
    self.speed = speed

  def move(self):    #To overwrite inheritance, create local function
    print('The shark has moved')
    print(f'The speed of the shark is {self.speed}')

  def bite(self):
    print('The shark has bitten')

shark = Shark(speed = 120, health = 100, energy = 80)
shark.move()
print(shark.health)
print(shark.energy)

#excercise
print("------- EXCERCISE --------")

#create a scorpion class that inherits from monster
#take health and energy from the parent
# posion_damage attribute
# overwrite the damage method to show posion damage

class Scorpion(Monster):
  def __init__(self, scorpion_health, scorpion_energy, poison_damage):
    super().__init__(health = scorpion_health, energy = scorpion_energy)
    self.poison_damage = poison_damage

  def attack(self):
    print('The scorpion attacks!')
    print(f'The scorpion deals {self.poison_damage} poison damage')

scorpion = Scorpion(scorpion_health = 20, scorpion_energy = 10, poison_damage = 30)
scorpion.attack()
scorpion.move(5)
print(scorpion.health)
print(scorpion.energy)

    