# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
from collections import deque
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class ZipTree:

	class Node:
		def __init__(self, key: KeyType, val: ValType, rank: int):
			self.key = key
			self.val = val
			self.rank = rank
			self.right = None
			self.left = None

	

	
	def __init__(self):
		self.root = None
		self.size = 0

	@staticmethod
	def get_random_rank() -> int:
		k = 0
		while random.random() < 1 / (2 ** (k + 1)):
			k += 1
		return k
		
		# Have no idea how to do this part


	def insert(self, key: KeyType, vals: ValType, rank: int = -1):
		# GO UP TO LAST HIGHER RANK NODE:

		# If this node has no rank, give it a random rank
		if rank == -1:
			rank = self.get_random_rank()

		# Generate a new node with the random rank
		new_node = self.Node(key, vals, rank)

		# Make sure it is not an empty tree
		if self.root is None:
			self.root = new_node
			new_node.right = None
			new_node.left = None
			self.size += 1
			return

		curr = self.root
		while curr is not None and (new_node.rank < curr.rank or (new_node.rank == curr.rank and new_node.key > curr.key)):
			prev = curr
			if new_node.key < curr.key:
				curr = curr.left
			else:
				curr = curr.right

		if curr == self.root:
			new_node = self.root

		elif new_node.key < prev.key:
			prev.left = new_node
		else:
			prev.right = new_node

		if curr == None:
			new_node.left = None
			new_node.right = None
			self.size += 1
			return 
		if new_node.key < curr.key:
			new_node.right = curr
		else:
			new_node.left = curr

		prev = new_node

		while curr is not None:
			fix = prev
			if curr.key < new_node.key:
				prev = curr
				curr = curr.right

			else:
				prev = currcurr = curr.left

			if fix.key > new_node.key or fix == new_node and prev.key > new_node.key:
					fix.left = curr
			else:
				fix.right = curr
			self.size += 1
			return		
	'''

		# If this node has no rank, give it a random rank
		if rank == -1:
			rank = self.get_random_rank()

		self.root = self.insert_recursive(self.root, key, val, rank)
		self.size += 1
		pass

	# a helper function to recursively insert
	def insert_recursive(self, node, key, val, rank):
		# if root is empty
		if not node:
			return {'key': key, 'val': val, 'rank': rank, 'left': None, 'right': None}
		#if our rank is less tahn curr , we continue left , else continue right
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
	'''



	def remove(self, key:KeyType):
		curr = self.root
		prev = None
		while key != curr.key:
			prev = curr
			if key < curr.key:
				curr = curr.left
			else:
				curr = curr.right
		left = curr.left
		right = curr.right

		if left is None:
			curr = right
		elif right is None:
			curr = left

		elif left.rank >= right.rank:
			curr = left
		else:
			curr = right

		if self.root.key == key:
			self.root = curr
		elif key < prev.key:
			prev.left = curr

		else:
			prev.right = curr
	
		while left is not None and right is not None:
			if left.rank >= right.rank:
				while left is not None and left.rank >= right.rank:
					prev= left
					left = left.right
				prev.right = right
			else:
				while right is not None and left.rank <  right.rank:
			
					prev = right
					right = right.left
				prev.left = left
		return self.root






	pass
	'''
def remove(self, key: KeyType):
		
		parent = None
		current = self.root
		# search for node
		while current:
			if key < current.key:
				parent, current = current, current.left
			elif key > current.key:
				parent, current = current, current.right
			else:
				print(f"removing{key, current.key, current.val, current.rank}")
				break
			# once found , romove via unzip	
		if current:
			self.root = self.remove_node(current, parent)
			self.size -= 1

def remove_node(self, node, parent):
		# if its a leaf node, make the parents pointer to it  = none
		if not node.left and not node.right:
			if parent:
				if parent.left == node:
					parent.left = None
				else:
					parent.right = None
			else:
				print(f'removal of {node.key, node.val, node.rank} success v 1')
				return None
			
			# if it has both a left and right , we zip
		elif node.left and node.right:
			P, Q = self.zip(node.left, node.right)
			if parent:
				if parent.left == node:
					parent.left = self.zip(P, Q)
				else:
					parent.right = self.zip(P, Q)
			else:
				print(f'removal of {node.key, node.val, node.rank} success v 2')
				return self.zip(P, Q)
		else:
			if node.left:
				child = node.left
			else:
				child = node.right

			if parent:
				if parent.left == node:
					parent.left = child
				else:
					parent.right = child
			else:
				print(f'removal of {node.key, node.val, node.rank} success v 3')
				return child
		print(f'removal of {node.key, node.val, node.rank} success v 4')	
		return self.root

def zip(self, P, Q):
		if P is None:
			return Q
		if Q is None:
			return P
		if Q.rank > P.rank:
			Q.left = self.zip(P, Q.left)
			return Q
		else:
			P.right = self.zip(P.right, Q)
			return P
	'''
	def find(self, key: KeyType) -> ValType:

		current = self.root

		while current:
			if key == current.key:
				return current.val
			elif key < current.key:
				current = current.left
			else:
				current = current.right

		return None

	def get_size(self) -> int:
		return self.size

	def get_height(self) -> int:		
		if not self.root:
			return -1
		
		height = -1
		stack = [(self.root, 0)]

		while stack:
			node, node_height = stack.pop()
			height = max(height, node_height)
			if node.left:
				stack.append((node.left, node_height + 1))
			if node.right:
				stack.append((node.right, node_height + 1))

		return height

	def get_depth(self, key: KeyType):
		depth = 0
		current = self.root

		while current:
			if key == current.key:
				return depth
			elif key < current.key:
				current = current.left
			else:
				current = current.right
			depth += 1

		return -1
		

	def print_tree(self, root, level = 0):
		if root is None:
			print("  " * level + "None")
			return
		print("  " * level + f"({root.key}, {root.val}, {root.rank})")
		self.print_tree(root.left, level + 1)
		self.print_tree(root.right, level + 1)


# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
