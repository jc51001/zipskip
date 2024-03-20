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
			# self.print_tree(self.root)
			# print("\n")
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
		parent = None
		current = self.root
		while current:
			if key < current.key:
				parent, current = current, current.left
			elif key > current.key:
				parent, current = current, current.right
			else:
				break

		if current:
			self.root = self.remove_node(current, parent)
			self.size -= 1

	def remove_node(self, node, parent):
		if not node.left and not node.right:
			if parent:
				if parent.left == node:
					parent.left = None
				else:
					parent.right = None
			else:
				return None
		elif node.left and node.right:
			P, Q = self.unzip(node.left, node.right)
			if parent:
				if parent.left == node:
					parent.left = self.zip(P, Q)
				else:
					parent.right = self.zip(P, Q)
			else:
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
				return child
			
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
