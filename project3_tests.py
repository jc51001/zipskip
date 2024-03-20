import requirements

from typing import TypeVar, NamedTuple
from copy import deepcopy

# Some test cases for the ZipTree and SkipList classes can be found below.
#
# Note that passing the test cases here does not necessarily mean that your zip tree/skip list
# is correctly implemented / will pass other cases. It is a good idea to try and create different
# test cases for both.

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int

def create_tree_with_data(data: [InsertType]) -> requirements.ZipTree:
	tree = requirements.ZipTree()
	for item in data:
		tree.insert(item.key, item.val, item.rank)

	return tree

def zip_tree_tests():
	print('testing ZipTree')

	data = [InsertType(4, 'a', 0), InsertType(5, 'b', 0), InsertType(2, 'c', 2), InsertType(1, 'd', 1)]
	tree = create_tree_with_data(data)

	print(f'find(4): {tree.find(4)}, Expected: a')
	print(f'get_size(): {tree.get_size()}, Expected: 4')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 1')
	tree.insert(0, 'e', 1)
	print(f'get_size(): {tree.get_size()}, Expected: 5')
	print(f'get_height(): {tree.get_height()}, Expected: 2')
	print(f'get_depth(2): {tree.get_depth(2)}, Expected: 0')
	print(f'get_depth(1): {tree.get_depth(1)}, Expected: 2\n')

	data2 = [InsertType(4, 'a', 2), InsertType(5, 'b', 3), InsertType(2, 'c', 1), InsertType(1, 'd', 0), InsertType(0, 'e', 1)]
	tree2 = create_tree_with_data(data2)

	print(f'find(4): {tree2.find(4)}, Expected: a')
	print(f'get_size(): {tree2.get_size()}, Expected: 5')
	print(f'get_height(): {tree2.get_height()}, Expected: 4')
	print(f'get_depth(2): {tree2.get_depth(2)}, Expected: 3')
	print(f'get_depth(1): {tree2.get_depth(1)}, Expected: 4')

	print('\ntesting random rank generation')
	rank_sum = 0
	num_ranks = 10000
	for _ in range(num_ranks):
		try:
			rank_sum += requirements.ZipTree.get_random_rank()
		except:
			break

	rank_mean = rank_sum / num_ranks

	print(f'random rank mean: {rank_mean}, Expected: ~1\n\n')

	# add new tests...

	data3 = [InsertType(6, 'F', 4), InsertType(4, 'D', 2), InsertType(7, 'G', 0), InsertType(8, 'H', 2), InsertType(19, 'S', 4), InsertType(10, 'J', 0), InsertType(12, 'L', 1), InsertType(13, 'M', 2), InsertType(24, 'X', 2)]
	tree3 = create_tree_with_data(data3)

	print(f'find(19): {tree3.find(19)}, Expected: S')
	print(f'find(6): {tree3.find(6)}, Expected: F')
	print(f'find(4): {tree3.find(4)}, Expected: D')
	print(f'find(7): {tree3.find(7)}, Expected: G')
	print(f'find(8): {tree3.find(8)}, Expected: H')
	print(f'find(10): {tree3.find(10)}, Expected: J')
	print(f'find(12): {tree3.find(12)}, Expected: L')
	print(f'find(13): {tree3.find(13)}, Expected: M')
	print(f'find(24): {tree3.find(24)}, Expected: X')
	print(f'get_size(): {tree3.get_size()}, Expected: 9')
	print(f'get_height(): {tree3.get_height()}, Expected: 5')
	print(f'get_depth(10): {tree3.get_depth(10)}, Expected: 5')
	print(f'get_depth(6): {tree3.get_depth(6)}, Expected: 0')
	print(f'get_depth(4): {tree3.get_depth(4)}, Expected: 1')
	print(f'get_depth(7): {tree3.get_depth(7)}, Expected: 3')
	print(f'get_depth(8): {tree3.get_depth(8)}, Expected: 2')
	print(f'get_depth(19): {tree3.get_depth(19)}, Expected: 1')
	print(f'get_depth(12): {tree3.get_depth(12)}, Expected: 4')
	print(f'get_depth(13): {tree3.get_depth(13)}, Expected: 3')
	print(f'get_depth(24): {tree3.get_depth(24)}, Expected: 2')
	tree3.insert(11, 'K', 3)
	print(f'find(19): {tree3.find(19)}, Expected: S')
	print(f'find(6): {tree3.find(6)}, Expected: F')
	print(f'find(4): {tree3.find(4)}, Expected: D')
	print(f'find(7): {tree3.find(7)}, Expected: G')
	print(f'find(8): {tree3.find(8)}, Expected: H')
	print(f'find(10): {tree3.find(10)}, Expected: J')
	print(f'find(12): {tree3.find(12)}, Expected: L')
	print(f'find(13): {tree3.find(13)}, Expected: M')
	print(f'find(24): {tree3.find(24)}, Expected: X')
	print(f'find(11): {tree3.find(11)}, Expected: K')
	print(f'get_size(): {tree3.get_size()}, Expected: 10')
	print(f'get_height(): {tree3.get_height()}, Expected: 4')
	print(f'get_depth(10): {tree3.get_depth(10)}, Expected: 4')
	print(f'get_depth(6): {tree3.get_depth(6)}, Expected: 0')
	print(f'get_depth(4): {tree3.get_depth(4)}, Expected: 1')
	print(f'get_depth(7): {tree3.get_depth(7)}, Expected: 4')
	print(f'get_depth(8): {tree3.get_depth(8)}, Expected: 3')
	print(f'get_depth(19): {tree3.get_depth(19)}, Expected: 1')
	print(f'get_depth(12): {tree3.get_depth(12)}, Expected: 4')
	print(f'get_depth(13): {tree3.get_depth(13)}, Expected: 3')
	print(f'get_depth(24): {tree3.get_depth(24)}, Expected: 2')
	print(f'get_depth(11): {tree3.get_depth(11)}, Expected: 2')
	tree3.remove(11)
	print(f'find(19): {tree3.find(19)}, Expected: S')
	print(f'find(6): {tree3.find(6)}, Expected: F')
	print(f'find(4): {tree3.find(4)}, Expected: D')
	print(f'find(7): {tree3.find(7)}, Expected: G')
	print(f'find(8): {tree3.find(8)}, Expected: H')
	print(f'find(10): {tree3.find(10)}, Expected: J')
	print(f'find(12): {tree3.find(12)}, Expected: L')
	print(f'find(13): {tree3.find(13)}, Expected: M')
	print(f'find(24): {tree3.find(24)}, Expected: X')
	print(f'get_size(): {tree3.get_size()}, Expected: 9')
	print(f'get_height(): {tree3.get_height()}, Expected: 5')
	print(f'get_depth(10): {tree3.get_depth(10)}, Expected: 5')
	print(f'get_depth(6): {tree3.get_depth(6)}, Expected: 0')
	print(f'get_depth(4): {tree3.get_depth(4)}, Expected: 1')
	print(f'get_depth(7): {tree3.get_depth(7)}, Expected: 3')
	print(f'get_depth(8): {tree3.get_depth(8)}, Expected: 2')
	print(f'get_depth(19): {tree3.get_depth(19)}, Expected: 1')
	print(f'get_depth(12): {tree3.get_depth(12)}, Expected: 4')
	print(f'get_depth(13): {tree3.get_depth(13)}, Expected: 3')
	print(f'get_depth(24): {tree3.get_depth(24)}, Expected: 2')

def skip_list_tests():
	print("testing skip list")
	skip_list = requirements.SkipList()
	skip_list.insert(2.4, 'a')
	skip_list.insert(2.5, 'b')
	skip_list.insert(2.2, 'c')
	skip_list.insert(2.1, 'd')
	skip_list.insert(2.6, 'e')
	# skip list levels should look like 
	#																		-> 2.1 -> 		 2.4 -> 	   2.6
	#														 				-> 2.1 -> 		 2.4 -> 	   2.6
	#															 			-> 2.1 -> 2.2 -> 2.4 -> 2.5 -> 2.6

	print(f'find(2.4): {skip_list.find(2.4)}, Expected: a')
	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 5')
	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 3')
	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 3\n')
	skip_list.remove(2.6)
	# skip list levels should look like 
	#																		-> 2.1 -> 		 2.4
	#														 				-> 2.1 -> 		 2.4
	#															 			-> 2.1 -> 2.2 -> 2.4 -> 2.5
	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 4')
	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 2')
	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 2\n')



	print("testing skip list construction from a zip tree")
	data = [InsertType(4, 'a', 0), InsertType(5, 'b', 0), InsertType(2, 'c', 2), InsertType(1, 'd', 1)]
	tree = create_tree_with_data(data)

	skip_list = requirements.SkipList()
	skip_list.from_zip_tree(tree)

	# skip list levels should look like 
	#																		->		2
	#														 				-> 1 -> 2
	#															 			-> 1 -> 2 -> 4 -> 5
	print(f'find(4): {skip_list.find(4)}, Expected: a')
	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 4')
	print(f'get_list_size_at_level(1): {skip_list.get_list_size_at_level(1)}, Expected: 2')
	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 1\n')
	skip_list.remove(2)
	# skip list levels should look like 
	#														 				-> 1
	#															 			-> 1 -> 4 -> 5
	print(f'get_list_size_at_level(0): {skip_list.get_list_size_at_level(0)}, Expected: 3')
	print(f'get_list_size_at_level(2): {skip_list.get_list_size_at_level(2)}, Expected: 0')

	# add new tests...
	
if __name__ == '__main__':
	zip_tree_tests()
	skip_list_tests()
