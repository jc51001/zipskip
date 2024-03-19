# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
from collections import deque
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class ZipTree:
	def __init__(self):
		self.root = None
		self.size = 0
		pass

	@staticmethod
	def get_random_rank() -> int:
		k = random.randint(0, float('inf'))
        while random.random() >= 1 / (2 ** (k + 1)):
            k = random.randint(0, float('inf'))
        return k
		# Have no idea how to do this part


	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		# If this node has no rank, give it a random rank
		if rank == -1:
			rank = self.get_random_rank()

		self.root = self.insert_recursive(self.root, key, val, rank)
		self.size += 1
		pass

	# a helper function to recursively insert
	def insert_recursive(self, node, key, val, rank):
		if not node:
			return {'key': key, 'val': val, 'rank': rank, 'left': None, 'right': None}
		
		if rank < node['rank']:
			if key < node['key']:
				node['left'] = self.insert_recursive(node['left'], key, val, rank)
			else:
				node['right'] = self.insert_recursive(node['right'], key, val, rank)
		else:
			if key < node['key']:
				# Rotate right
				new_node = {'key': key, 'val': val, 'rank': rank, 'right': node, 'left': node['left']}
				return new_node
			else:
				# Rotate left
				new_node = {'key': key, 'val': val, 'rank': rank, 'left': node, 'right': node['right']}
				return new_node
			
		return node

	def remove(self, key: KeyType):

		self.root = self.remove_recursive(self.root, key)
		self.size -= 1

	def remove_recursive(self, node, key):

		if not node:
			return None
		
		if key < node['key']:
			node['left'] = self.remove(node['left'], key)
		elif key > node['key']:
			node['right'] = self.remove(node['right'], key)
		else:
			if not node['left']:
				return node['right']
			elif not node['right']:
				return node['left']
			else:
				# This is the case where the node has 2 children, so find the min val in the right subtree
				min = self.find_min(node['right'])
				node['key'], node['val'], node['rank'] = min['key'], min['val'], min['rank']
				node['right'] = node(node['right'], min['key'])

		return node
		pass

	def find_min(self, node):
		while node['left']:
			node = node['left']
		return node

	def find(self, key: KeyType) -> ValType:

		return self.find_recursive(self.root, key)['val']
	
	def find_recursive(self, node, key):

		if not node or node['key'] == key:
			return node
		
		if key < node['key']:
			return self.find_recursive(node['left'], key)
		else:
			return self.find_recursive(node['right'], key)
		pass

	def get_size(self) -> int:

		return self.size

	def get_height(self) -> int:

		if not self.root:
			return 0
		
		return self.get_height_recursive(self.root)
	
	def get_height_recursive(self, node):
		if not node:
			return 0
		
		left_height = self.get_height_recursive(node.get('left', None))
		right_height = self.get_height_recursive(node.get('right', None))

		return max(left_height, right_height) + 1

	def get_depth(self, key: KeyType):
		return self.get_depth_recursive(self.root, key, 0)
	
	def get_depth_recursive(self, node, key, depth):
		if not node or node['key'] == key:
			return depth
		if key < node['key']:
			return self.get_depth_recursive(node['left'], key, depth + 1)
		else:
			return self.get_depth_recursive(node['right'], key, depth + 1)

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
