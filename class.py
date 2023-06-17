
class Monster:

  Attributes
  health = 90 
  energy = 40
  speed = 5

  Methods
  def __init__(self, health, energy):
    self.health = health
    self.energy = energy

  def __len__(self):
    return self.health

  def __abs__(self):
    return self.energy

  def __str__(self):
    eturn f'The monster has {self.health} health, and {self.energy} energy'
  
  def attack(self,amount):
    print("The monster has attacked")
    print(f'{amount} of damage was dealt')
    self.energy -= 20 
    print(self.energy)

  def move(self, speed):
    print("The monster has moved",speed,"spaces")

monster1 = Monster(10,20)
print(len(monster1))
print(abs(monster1))
print(dir(monster1))
print(str(monster1))
print(monster1)

#Task 2 

#1 Create a monster class with a parameter called func, store this func as a parameter

class Pokemon:

  def __init__(self,func):
    self.func = func
  
#2. Create another class, called Attacks, which has 4 methods:
#Bite, strike, slash & kick - [each printing some text]

class Attacks:

  #Methods
  def bite(self):
    print(self,"Bites!")

  def strike(self):
    print(self,"Strikes!")

  def slash(self):
    print(self,"Slashes!")

  def kick(self):
    print(self,"Kicks!")

#3. Create a monster object - giving it one of the attack methods from the attack class

Poke = Pokemon(func = Attacks().bite)  #Returning a class
Poke.func()