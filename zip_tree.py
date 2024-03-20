# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class ZipTree:
	class Node:
		def __init__(self, key: KeyType, val: ValType, rank: int):
			self.key = key
			self.val = val
			self.rank = rank
			self.left = None
			self.right = None

	def __init__(self):
		self.root = None
		self.size = 0

	@staticmethod
	def get_random_rank() -> int:
		# After a lot of research on how to generate a random integer with a geometric distribution
		# Geometric distribution: p(k) = (1 - p)^(k - 1) * p
		# In this case, p = 0.5 -> E(X) = 1. Use the random module from python.
		# Sad, my research ended up not doing much, just gonna keep it here for now cuz idk how to do this.
		return random.randint(0, 2)
		pass

	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		# If this node has no rank, give it a random rank
		if rank == -1:
			rank = self.get_random_rank()

		# Generate a new node with the random rank
		new_node = self.Node(key, val, rank)

		# Make sure it is not an empty tree
		if self.root is None:
			self.root = new_node
			self.size += 1
			return
		
		# Search for the node with key 'K' in the tree

		parent = None # Parent of the new_node
		current = self.root # Essentially our 'y'
		while current:
			# If meets conditions, then break as current is where it should be as well as parent (unless it's the root)
			if current.rank < rank or (current.rank == rank and current.key > key):
				break

			# If y has not been found, continue traversing the tree
			parent = current
			if key < current.key:
				current = current.left
			else:
				current = current.right
			
		# If y is never found, then set as leaf node
		if current is None:
			if key < parent.key:
				parent.left = new_node
			else:
				parent.right = new_node
			self.size += 1
			# self.print_tree(self.root)
			# print("\n")
			return

		# Create paths P and Q by unzipping from node y
		P, Q = self.unzip(current, new_node)
		
		# Replace y with x and attach P and Q accordingly
		if parent is None: # Parent is none, then new_node is at the root
			new_node.left = P
			new_node.right = Q
			self.root = new_node
		elif rank < parent.rank or (rank == parent.rank and key < parent.key):
			new_node.left = P
			new_node.right = Q
			if parent.left == current:
				parent.left = new_node
			else:
				parent.right = new_node
		
		self.size += 1

		# self.print_tree(self.root)
		# print("\n")

	def unzip(self, y, x):
		def unzip_lookup(k, node):
			if node is None:
				return (None, None)
			if node.key < k:
				P, Q = unzip_lookup(k, node.right)
				node.right = P
				return (node, Q)
			else:
				P, Q = unzip_lookup(k, node.left)
				node.left = Q
				return (P, node)
				
		return unzip_lookup(x.key, y)

	def remove(self, key: KeyType):
		self.root = self.remove_recursive(self.root, key)
		self.size -= 1

	def remove_recursive(self, node, key):

		if not node:
			return None
		
		if key < node.key:
			node.left = self.remove_recursive(node.left, key)
		elif key > node.key:
			node.right = self.remove_recursive(node.right, key)
		else:
			# Node has been found, perform the removal

			# Zip the two paths into a single path
			node = self.zip(node.left, node.right)

		return node

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

	def find(self, key: KeyType) -> ValType:

		return self.find_recursive(self.root, key)
	
	def find_recursive(self, node, key):
		
		# The node is not in the tree
		if node is None:
			return None
		
		if key == node.key:
			return node.val # Found the node, return its value
		elif key < node.key:
			return self.find_recursive(node.left, key) # Traverse the left branch
		else:
			return self.find_recursive(node.right, key) # Traverse the right branch

	def get_size(self) -> int:
		return self.size

	def get_height(self) -> int:		
		return self.get_height_recursive(self.root) - 1
	
	def get_height_recursive(self, node):

		# print("counting node: ", node)

		if node is None:
			return 0
		
		left_height = self.get_height_recursive(node.left)
		right_height = self.get_height_recursive(node.right)

		# print("left_height: ", left_height)
		# print("right_height: ", right_height)

		return 1 + max(left_height, right_height)

	def get_depth(self, key: KeyType):
		return self.get_depth_recursive(self.root, key)
	
	def get_depth_recursive(self, node, key, depth = 0):

		# print("node: (", node.key, node.val, node.rank, "). key: ", key)

		if node is None:
			return -1
		
		if key == node.key:
			return depth
		elif key < node.key:
			return self.get_depth_recursive(node.left, key, depth + 1)
		else:
			return self.get_depth_recursive(node.right, key, depth + 1)
		
	'''
	def print_tree(self, root, level = 0):
		if root is None:
			print("  " * level + "None")
			return
		print("  " * level + f"({root.key}, {root.val}, {root.rank})")
		self.print_tree(root.left, level + 1)
		self.print_tree(root.right, level + 1)
	'''

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
