# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import TypeVar
import random
from zip_tree import ZipTree

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class SkipList:
	def __init__(self):
		# Initialize with dummy head node at each level
		self.levels = {}
		self.max_level = -1

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

		if level > self.max_level:
			self.max_level = level
		for i in range(level + 1):
			if i not in self.levels:
				self.levels[i] = ZipTree()
			self.levels[i].insert(key, val)

	def remove(self, key: KeyType):
		for i in range(self.max_level + 1):
			if i in self.levels:
				self.levels[i].remove(key)

	def find(self, key: KeyType) -> ValType:
		if 0 in self.levels:
			return self.levels[0].find(key)

	def get_list_size_at_level(self, level: int):

		if level in self.levels:
			return self.levels[level].get_size()
		return 0
		
	def from_zip_tree(self, zip_tree: ZipTree) -> None:
		self.levels = {}
		self.max_level = zip_tree.get_height()
		self.insert_zip(zip_tree.root, 0)
	
	def insert_zip(self, node, level):
		if node is not None:
			self.insert_zip(node.left, level)
			self.insert_node_at_level(node, node.rank)
			self.insert_zip(node.right, level)

	def insert_node_at_level(self, node, rank):
		for i in range(rank + 1):
			if i not in self.levels:
				self.levels[i] = ZipTree()
			self.levels[i].insert(node.key, node.val)
			

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
