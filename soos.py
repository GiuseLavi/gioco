class Entity:

	def __init__(self, x, y):

		self.x = x
		self.y = y


	def move(self, map_x, map_y, direction):

		if direction == "N" or direction == "n":

			self.y -= 1

		elif direction == "S" or direction == "s":

			self.y += 1

		elif direction == "E" or direction == "e":

			self.x += 1

		elif direction == "W" or direction == "w":

			self.x -= 1

class Player(Entity):

	def __init__(self, x, y, max_hp):

		Entity.__init__(self, x, y)
		self.max_hp = max_hp
		self.cur_hp = max_hp


class Monster(Entity):

	def __init__(self, x, y, damage):

		Entity.__init__(self, x, y)
		self.damage = damage

	def attack(self, player):

		print("Il mostro ti attacca")
		player.cur_hp -= self.damage


class World:
	
	def __init__(self, x, y):

		self.x = x
		self.y = y

	def draw(self, p_x, p_y, m_x, m_y, e_x, e_y):

		c = [p_x, p_y, m_x, m_y, e_x, e_y]


		for i in range(self.y):

			if i != p_y and i != m_y and i != e_y:

				for n in range(self.x):

					print("[ ]", end = "")

			elif i in c:

				for n in range(self.x):

					if n == p_x and i == p_y:

						print("[P]", end = "")

					elif n == m_x and i == m_y:

						print("[M]", end = "")

					elif n == e_x and i == e_y:

						print("[E]", end = "")

					else:
						print("[ ]", end = "")

			print()

p_x = 0
p_y = 0
m_x = 8
m_y = 6
e_x = 4
e_y = 2

lv1 = World(10,10)
player = Player(p_x, p_y, 100)
monster = Monster(e_x, e_y, 20)
medal = Entity(m_x, m_y)
	
lv1.draw(p_x, p_y, m_x, m_y, e_x, e_y)

while True:

	player.move(lv1.x, lv1, input())
	lv1.draw(player.x, player.y, m_x, m_y, e_x, e_y)

	if player.x == m_x and player.y == m_y:

		print("hai vinto")
		break