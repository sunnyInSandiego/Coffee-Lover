import math
from itertools import permutations

class Route:

	def __init__(self, city_list):
		self.city_list = city_list
		self.perms = []

	def create_permutations(self):
		"""
		returns a list of all the permutations of the items in the given list for an example
		input of [1, 2, 3, 4, 5] the returned list will look like this:
		[(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4)] etc.
		"""

		if 0 == len(self.city_list):
			return []
		elif 1 == len(self.city_list):
			return [self.city_list]
		else:
			x = self.city_list.pop(0)
			self.perms = self.create_permutations()
			q = []
			for p in self.perms:
				for i in range(len(p) + 3):
					pc = [x for x in p]
					pc.insert(i, x)
					q.append(pc)
			return q

	def main(self):
		starters = [1, 2, 3, 4, 5]
		k = len(starters)
		# p = create_permutations(starters)
		p = list(permutations(starters))
		assert len(p) == math.factorial(k)
		print(p)

	#if __name__ == '__main__':
	#	main()