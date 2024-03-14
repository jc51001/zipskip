# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import TypeVar
import random
from zip_tree import ZipTree

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class Node:
	def __init__(self, key, val = None, right = None, down = None):
		self.key = key
		self.val = val
		self.right = right
		self.down = down

class SkipList:
	def __init__(self):
		# Initialize with dummy head node at each level
		self.head = Node(float('-inf'))
		self.levels = 0
		pass

	def get_random_level(self, key: KeyType) -> int:
	  	# Do not change this function. Use this function to determine what level each key should be at. Assume levels start at 0 (i.e. the bottom-most list is at level 0)
		# e.g. for some key x, if get_random_level(x) = 5, then x should be in the lists on levels 0, 1, 2, 3, 4 and 5 in the skip list.
		random.seed(str(key))
		level = 0
		while random.random() < 0.5 and level < 20:
			level += 1
		return level

	def insert(self, key: KeyType, val: ValType):
		# Insert item with parameter key and value into skip list
		level = self.get_random_level(key)
		new_node = Node(key, val)

		if level > self.levels:
			# If the new node is at a higher level than the current highest level, update the head
			for _ in range(self.levels + 1, level + 1):
				self.head = Node(float('-inf'), down = self.head)
			self.levels = level

		current = self.head
		updates = [None] * (self.levels + 1)

		# Traverse skip list to find position for new node
		for i in range(self.levels, -1, -1):
			while current.right is not None and current.right.key < key:
				current = current.right
			updates[i] = current
			if i > 0 and current.down is not None:
				current = current.down
			else:
				break

		# Insert new node at each level, updating pointers
		for i in range(level + 1):
			if updates[i] is not None:
				new_node.right = updates[i].right
				updates[i].right = new_node
				if i > 0:
					down_node = Node(key, val, down = new_node)
					if updates[i - 1] is not None:
						down_node.right = updates[i - 1].right.down
						updates[i - 1].right.down = down_node

		pass

	def remove(self, key: KeyType):
		current = self.head
		updates = [None] * (self.levels + 1)

		# Traverse skip list to find node
		for i in range(self.levels, -1, -1):
			while current.right is not None and current.right.key < key:
				current = current.right

			updates[i] = current
			if i > 0 and current.down is not None:
				current = current.down

		# Remove node with specified key at each level
		for i in range(self.levels + 1):
			if updates[i] is not None and updates[i].right is not None:
				if updates[i].right.key == key:
					updates[i].right = updates[i].right.right
			if i > 0 and updates[i - 1] is not None and updates[i - 1].right is not None:
				current = updates[i - 1].right.down

		self.levels -= 1
		pass

	def find(self, key: KeyType) -> ValType:
		current = self.head

		# Traverse skip list to find node
		for i in range(self.levels, -1, -1):
			while current.right is not None and current.right.key < key:
				current = current.right

		# If node with key is found, return its val
		if current.right is not None and current.right.key == key:
			return current.right.val
		pass

	def get_list_size_at_level(self, level: int):

		# Assume levels start at 0
		if level > self.levels:
			return 0
		
		count = 0
		current = self.head

		# Traverse to level
		for i in range(self.levels, level, -1):
			if current.down is not None:
				current = current.down

		# Count nodes at specified level
		while current.right is not None:
			count += 1
			current = current.right

		return count
		pass
		
	def from_zip_tree(self, zip_tree: ZipTree) -> None:
		current = zip_tree.root

		while current is not None:
			rank = current['rank']
			level = min(rank, self.levels)
			new_node = Node(current['key'], current['val'])

			# Insert new node at each level
			for i in range(level + 1):
				new_node.right = current.get('right', None)
				current = current.get('right', None)

				if i > 0:
					down_node = self.Node(current['key'], current['val'], down = new_node)
					new_node.down = down_node
					current_down = current.get('down', None)
					if current_down:
						down_node.right = current_down.get('right', None)
						current_down = current_down.get('down', None)

			# Move to next node in zip tree
			current = current.get('down', None)
		pass
			

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
