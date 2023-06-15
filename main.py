
class Monster:

  #Attributes
  health = 90 
  energy = 40
  speed = 5

  
  #Methods
  def attack(self,amount):
    print("The monster has attacked")
    print(f'{amount} of damage was dealt')
    monster.energy -= 20 
    print(monster.energy)


  def move(self, speed):
    print("The monster has moved",speed,"spaces")

monster = Monster()
monster.attack(40)
monster.move(monster.speed)