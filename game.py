import random

# create hero object
class Hero():
    def __init__(self, lifePoints, damage, dodgeChance, description):
        self.lifePoints = lifePoints
        self.damage  = damage
        self.dodgeChance  = dodgeChance
        self.description  = description

# create enemy object
class Enemy():
    def __init__(self, lifePoints, damage, dodgeChance, description, hitChance):
        self.lifePoints = lifePoints
        self.damage  = damage
        self.dodgeChance  = dodgeChance
        self.description  = description
        self.hitChance = hitChance

# resolve hero 
def resolveGear(gearCode):
    if(gearCode == "1"):
        hero = Hero(20, 3, 20, "light")
    elif(gearCode == "2"):
        hero = Hero(30, 2, 15, "medium")
    else:
        hero = Hero(40, 2, 7, "heavy")
    return hero

# resolve enemy
def resolveEnemy(enemyCode):
    if(enemyCode < 5):
        enemy = Enemy(3, 1, 5, "an easy", 2)
    elif(enemyCode > 5 & enemyCode < 8):
        enemy = Enemy(6, 2, 7, "a medium", 3)
    else:
        enemy = Enemy(9, 3, 10, "a hard", 5)
    return enemy

# fight logic
def fight(character, enemy):
    
    while (enemy.lifePoints > 0):
        enemyValue = random.randint(0, (enemy.hitChance - 1))
        print(f"select your hit value. you will hit if your hitvalue is the same as the enemyvalue. in other case the enemy will hit you\nselect a number between 0 and {(enemy.hitChance-1)}")
        characterValue = int(input())

        if(characterValue == enemyValue):
            if(random.randint(0, 99) < enemy.dodgeChance):
                print("the enemy dodged your attack")
            else:
                enemy.lifePoints -= character.damage
                print(f"you hit the enemy with {character.damage} damage. now the enemy got {enemy.lifePoints} lifepoints")
        else:
            if(random.randint(0, 99) < character.dodgeChance):
                print("you dodged the enemys attack")
            else:
            
                character.lifePoints -= enemy.damage
                print(f"you got hit with {enemy.damage} damage. now you got {character.lifePoints} lifepoints")
        
        if(character.lifePoints < 1):
            print("you died")
            quit()

# start of game, choose gear
print("welcome to your dungeon adventure \n select your gear! insert: \n 1 for light \n 2 for medium \n 3 for heavy")
character = resolveGear(input())
print(f"you selectd {character.description}.\nyour stats:\nlifepoints = {character.lifePoints},\ndamage = {character.damage} and\ndodge chance = {character.dodgeChance}")

#run the dungeon
rooms = 7
while(True):
    
    randomEnemyCode = random.randint(0,9)
    enemy = resolveEnemy(randomEnemyCode)
    print(f"\n\nyou entered the next room.\nthere are {rooms} rooms left in the dungeon\n{enemy.description} enemy is appears")
    fight(character, enemy)
    
    # search for healt potions
    if(random.randint(0, 3) == 0):
        print("\nyou found a heal potion!\nyour lifepoints increase by 5")
        character.lifePoints += 5
    
    # are there remeining rooms left
    rooms = rooms - 1 
    if(rooms == 0):
        print("you completed the dungeon!")
        quit()

