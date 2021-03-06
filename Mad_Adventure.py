import random
import string
# the class below is the room code meant for creating rooms in dungeons and open world for the player to interact 
class Room(object):
	def __init__(self):
		self.initial_text = None
		self.mchecks = None
		self.schecks = None
		self.choices = None
		self.monsters = None
		self.objects = None
		self.traps = None
		self.actions = None
# this class creates combat instances, not sure if I still want it to be this way, however it may be the best way to add story combats 
class Combat(object):
	def __init__(self):
		self.player_health = None
		self.player_AC = None
		self.Monster_health = None
		self.Monster_AC = None
		self.Monsters = None
	def order(self):
		i = {}
		for monster in Monsters:
			monster.initiative = monster_check('Dexterity')
			i[monster.name] = monster.initiative
		player.initiative = skill_check('Dexterity',char.stats, char.proficiency)
		i[char.name] = player.initiative
# before this comment need to write a piece of code to find the combat order from the dictionary and sort it into a two dimensional array 
	def player_attack(self):
#here we need to set up a system for clicking on the monster they wish to attack or at least have a sequence of buttons
#we want to check the conditions of the fight, so how much range the weapon has, which monsters are within range, all that jazz
#movement should be set up a bit like a chess board 
	def monster_attack(self):
# here is mainly just calling info from turn order, then having each monster ai choose what it wants to do 
class Monster(object):
	def __init__(self):
		self.AC = None
		self.health = None
		self.attack_1 = None
		self.attack_2 = None
		self.dmg_1 = None
		self.dmg_2 = None
		self.state = None
		self.m_stats = None
		self.initiative = None
# this is the player class which holds and keeps the player state	
class Player(object):
	def __init__(self):
		self.name = None
		self.level = None
		self.stats = None
		self.player_class = None
		self.hitdice = None
		self.health = None
		self.inventory = []
		self.weapon = None
		self.spells = []
		self.gold = None
		self.armour = None
		self.initiative = None
		self.state = None
		self.proficiency = None
	def Access_Inv(self):
		print(self.inventory)
		input("Is there something you would like to grab?")
	def Check_Health(self):
		print(self.health)
	def Summary(self):
		self.Check_Health()
		self.Access_Inv()
		print(self.stats)
	def Alive(self):
		if self.state == 'dead':
			print('You Are Dead')
#Below are the dice objects used to generate random numbers!! You can make as many as you want!!
class d20(object):
	def __init__(self):
		self.roll = 0
	def Roll(self):
		self.roll = random.randint(1,20)
		return(self.roll)
class d12(object):
	def __init__(self):
		self.roll =0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,12)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n):
			x = self.Roll()
			self.total += x
class d10(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,10)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n):
			x = self.Roll()
			self.total += x
class d8(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,8)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n):
			x = self.Roll()
			self.total += x
class d6(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,6)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n):
			x = self.Roll()
			self.total += x
class d4(object):
	def __init__(self):
		self.roll = 0
		self.total = 0
	def Roll(self):
		self.roll = random.randint(1,4)
		return(self.roll)
	def multiRoll(self,n):
		for i in range(0,n):
			x = self.Roll()
			self.total += x
class d100(object):
	def __init__(self):
		self.roll = 0
	def Roll(self):
		self.roll = random.randint(1,100)	
		return(self.roll)
Stat_Names = ['Strength', 'Constitution', 'Dexterity', 'Intellegence', 'Wisdom', 'Charisma']		
def Stat_Roller(): 
#stat roller function for character creation 
	stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
	return(stat)
def Stat_Assignment():
# stat assignment function for character creation 
	Abillity_Score = {'Strength': 1, 'Constitution': 1, 'Dexterity': 1, 'Intellegence': 1, 'Wisdom': 1, 'Charisma': 1}
	stats = []
	for i in range(0,6):
		stats.append(Stat_Roller())
	print(stats)

	for stat in Stat_Names:
		j = 1
		while j == 1:
			i1 = input('Which number would you like to assign to the '+stat+' score ')
			try:
				i1 = int(i1)
			except ValueError:
					print('')
			if i1 in stats:
				stats.remove(int(i1))
				Abillity_Score[stat] = i1
				j = -1
			else:
				print('Please try again your unassigned values are '+str(stats)+' ! ')		
	return(Abillity_Score)
def player_class():
# function to determine the class a player wants to play
	player_class = ''
	playable = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
	j = 1
	while j == 1:
		i2 = str(input('There are '+str(len(playable))+' classes in this game, please choose one from this list '+str(playable)+' ... '))
		if string.capwords(i2) in playable:
			i3 = input('You have picked the '+string.capwords(i2)+' class, are you sure about playing this class? ')
			if i3.lower() == 'yes':
				player_class = string.capwords(i2)
				j = -1
			else:
				print('Please choose your desired class!')
		else:
			print('Your input is invalid, please try again!')
	return(player_class)
def hitdice(player_class):
#hit dice values for each class 
	hitdice = ''
	d12 = ['Barbarian']
	d10 = ['Cleric','Fighter','Paladin']
	d8 = ['Bard','Druid','Rogue','Ranger','Warlock','Monk']
	d6 = ['Wizard','Sorcerer']
	dice = [d12,d10,d8,d6]
	dicevalue = ['d 12','d 10','d 8','d 6']
	k = 0
	for hdice in dice:
		if player_class in hdice:
			hitdice = dicevalue[k]
			break
		else:
			k += 1
	return(hitdice)
def health(level,stats,hitdice):
# basic health calculation 
	mod = ((stats['Constitution']-10)/2)//1
	jank = hitdice.split()
	value = int(jank[1])
	if level == 1:
		health = value + mod
	else:
		health = health + random.randint(1,value)+ mod
	return(int(health))

	
hundred = d100()
twenty = d20()
twelve = d12()
ten = d10()
eight = d8()
six = d6()
four = d4()
def skill_check(stat, stats, proficiency,bonus):
#player skill checks 
	mod = ((stats[stat]-10)/2)//1
	x = twenty.Roll()
	check = x + mod + proficiency + bonus
	return(int(check))
def monster_check(stat,monster):
#monster skill checks
	mod = ((monster.m_stats[stat]-10)/2)//1
	x = twenty.Roll()
	check = x + mod 
	return(int(check))
print('Welcome to a world of magic and Adventure! Befor we jump in there are few things that you must answer me!')
char = Player()
char.name = input('I require only your name! The rest is up to you! ')
char.level = 1
char.player_class = player_class()
char.hitdice = hitdice(char.player_class)
char.stats = Stat_Assignment()
char.weapon = ['Fist','Short Sword']
char.inventory = ['Rations5','Bedroll','Firestarter']
char.health = health(char.level, char.stats, char.hitdice)
char.armour = 10 + ((char.stats['Dexterity']-10)/2)//1
char.state = 'alive'

print('Well done '+char.name+' now there are only a few more questions you must answer!')

clearing = Room()
clearing.initial_text = 'Its been seven days since you set out from your small town to make for the city of Whitewater. Last night you decided to camp off the road. It is early morning now, roll perception!'
clearing.mchecks = {'Perception' : 15}
clearing.monsters = {'Goblin': 1}
clearing.actions = ['Roll Perception','']

#here I want to have a function that creates monsters, like pulls stats from the book and does a bit of random health rolling
#RELATED NOTE!! IN ANOTHER FILE WE SHOULD MAKE A WEAPON ASSIGNMENT FUNCTION FOR MONSTERS!! 

clearing.mchecks['Perception'] = twenty.Roll()+20
j = 1
while j == 1:
	action_input = input(clearing.initial_text)
	if string.capwords(action_input) in clearing.actions:
		x = skill_check('Wisdom',char.stats)
		if x >> clearing.mchecks['Perception']:
			link = 1
			j = -1
		else:
			link = 2
			j = -1
	else:
		print('That is not a valid action, you may '+str(clearing.actions)+' ...')
clearing1 = Room()
if link == 1:
	clearing1.initial_text = 'Your eyes open to a slight shuffling behind you, turning around you notice that a goblin has infiltrated your campsite!'
	clearing1.monsters = {'Goblin': 1}
	clearing1.actions = ['Attack']
	print(clearing1.initial_text)
	print(str(clearing1.actions))
elif link == 2:
	x = hundred.Roll()
	if x <= 50: 
		clearing1.initial_text = 'You continue to peacefully sleep, the only thing that rouses you is the chirping of birds several hours later'
		char.gold = 0
		char.weapon = ['Fist']
		char.inventory = []
		link = 'a1'
		print(clearing1.initial_text)
	else: 
		clearing1.initial_text = 'You hear a shout and open your eyes to a sword coming down toward you'
		link = 'a2'
if link == 'a2':
	goblin = Monster()
	goblin.AC = 10
	goblin.health = 9
	goblin.attack = 1
	goblin.state = 'alive'
	print(clearing1.initial_text)


