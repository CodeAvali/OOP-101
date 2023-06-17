#Procedural technique

def update_health(amount):
  monster.health += amount

#health = 10 
#print(health)
#update_health(20)
#print(health)

#ERROR: Local variable health referenced before assignment 

#------

class Monster:
  def __init__(self,health,energy):
    self.health = health
    self.set_energy(energy)

  def update_energy(self, amount):
    self.energy += amount 

  def set_energy(self,energy):
    new_energy = energy * 2
    self.energy = new_energy

  def get_damage(self, amount):
    self.health -= amount

monster = Monster(health = 100, energy = 50)
#update_health(20)
print(monster.health)
#monster.update_energy(20)
print(monster.energy)

#-------
#3. Create a hero class with 2 parameters: 1. damage, 2. monster

class Hero:
  def __init__(self, damage, monster):
    self.damage = damage
    self.monster = monster
    
#2. the monster class should have a method 
#that lowers the health -> get_damage(amount)
    
#3. the hero class should have an attack method that get damage method from the monster, the amount of damage is hero.damage

  def attack(self):
    self.monster.get_damage(self.damage)

hero = Hero(damage = 15, monster = monster)
print(monster.health)
hero.attack()
print(monster.health)