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

		player.cur_hp -= self.damage


class World:
	
	def __init__(self, x, y):

		self.x = x
		self.y = y

	def draw(self, p_x, p_y, m_x, m_y, e_x, e_y):

		c = [p_x, p_y, m_x, m_y, e_x, e_y]


		for i in range(self.y):

			if i != p_y and i != m_y and i != e_y:

				print("[ ]", end = "")

			elif i in c:

				for n in range(self.x):

					if n == p_x:

						print("[P]", end = "")

					elif n == m_x:

						print("[M]", end = "")

					elif n == e_x:

						print("[E]", end = "")

					else:
						print("[ ]", end = "")

			print()

