import random

name = 'Рыцарь'

hp = 170
damage_range =  ( 30, 40 )

coins = 170

loot = [ random.choice(['shield', 'knight_helmet', 'knight_sword', 'knight_knee']) ]

def enter(user, reply):
	reply('Весь в доспехах')

	if user.story_level < 3:
		reply('Я не бью маленьких девочек типа тебя')
		user.leave(reply)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(0, dmg - 50)

	if hp <= 0:
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)