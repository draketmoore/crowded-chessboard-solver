#from pysat.formula import CNF
from pysat.solvers import Minicard
#import sys
#import importlib
from pysatsolver import make_board, add_horizontals, add_diagonals, add_knight_moves, add_overlap
import unittest


# Our testing is focused on making sure that our solutions 
# follow the constraints of the puzzle we are trying to solve
class TestMake(unittest.TestCase):

	def test_make_2(self):
		self.assertEqual(make_board(0, [], 2), [[0, 1], [2, 3]])

	def test_make_3(self):
		self.assertEqual(make_board(1, [], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	



class TestAddH(unittest.TestCase):

	def testAddH2(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4], k = 2, no_return = False)
		s.add_atmost(lits = [1, 3], k = 1, no_return = False)
		s.add_atmost(lits = [2, 4], k = 1, no_return = False)
		s.add_atmost(lits = [1, 2], k = 1, no_return = False)
		s.add_atmost(lits = [3, 4], k = 1, no_return = False)

		s1 = Minicard()
		rooks = make_board(1, [], 2)
		s1 = add_horizontals(s1, rooks, 2, 2)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())

	def testAddH3(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4, 5, 6, 7, 8, 9], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4, -5, -6, -7, -8, -9], k = 6, no_return = False)
		s.add_atmost(lits = [1, 4, 7], k = 1, no_return = False)
		s.add_atmost(lits = [2, 5, 8], k = 1, no_return = False)
		s.add_atmost(lits = [3, 6, 9], k = 1, no_return = False)

		s.add_atmost(lits = [1, 2, 3], k = 1, no_return = False)
		s.add_atmost(lits = [4, 5, 6], k = 1, no_return = False)
		s.add_atmost(lits = [7, 8, 9], k = 1, no_return = False)

		s1 = Minicard()
		rooks = make_board(1, [], 3)
		s1 = add_horizontals(s1, rooks, 3, 3)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())


class TestAddD(unittest.TestCase):

	def testAddD2(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4], k = 2, no_return = False)
		s.add_atmost(lits = [1, 4], k = 1, no_return = False)
		s.add_atmost(lits = [2, 3], k = 1, no_return = False)



		s1 = Minicard()
		pieces = make_board(1, [], 2)
		s1 = add_diagonals(s1, pieces, 2, 2)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())

	def testAddD3(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4, 5, 6, 7, 8, 9], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4, -5, -6, -7, -8, -9], k = 5, no_return = False)
		s.add_atmost(lits = [1, 5, 9], k = 1, no_return = False)
		s.add_atmost(lits = [4, 8], k = 1, no_return = False)
		s.add_atmost(lits = [2, 6], k = 1, no_return = False)
		s.add_atmost(lits = [3], k = 1, no_return = False)
		s.add_atmost(lits = [7], k = 1, no_return = False)

		s.add_atmost(lits = [7, 5, 3], k = 1, no_return = False)
		s.add_atmost(lits = [4, 2], k = 1, no_return = False)
		s.add_atmost(lits = [8, 6], k = 1, no_return = False)

		s.add_atmost(lits = [1], k = 1, no_return = False)
		s.add_atmost(lits = [9], k = 1, no_return = False)


		s1 = Minicard()
		pieces = make_board(1, [], 3)
		s1 = add_diagonals(s1, pieces, 4, 3)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())

class TestAddK(unittest.TestCase):

	def testAddK3(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4, 5, 6, 7, 8, 9], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4, -5, -6, -7, -8, -9], k = 4, no_return = False)
		s.add_atmost(lits = [1, 8], k = 1, no_return = False)
		s.add_atmost(lits = [1, 6], k = 1, no_return = False)
		s.add_atmost(lits = [2, 7], k = 1, no_return = False)
		s.add_atmost(lits = [2, 9], k = 1, no_return = False)
		s.add_atmost(lits = [3, 4], k = 1, no_return = False)
		s.add_atmost(lits = [3, 8], k = 1, no_return = False)
		s.add_atmost(lits = [4, 3], k = 1, no_return = False)
		s.add_atmost(lits = [4, 9], k = 1, no_return = False)
		s.add_atmost(lits = [6, 1], k = 1, no_return = False)
		s.add_atmost(lits = [6, 7], k = 1, no_return = False)

		s1 = Minicard()
		pieces = make_board(1, [], 3)
		s1 = add_knight_moves(s1, pieces, 5, 3)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())


	def testAddK4(self):
		s = Minicard()
		s.add_clause([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], no_return = False)
		s.add_atmost(lits = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16], k = 8, no_return = False)
		s.add_atmost(lits = [1, 7], k = 1, no_return = False)
		s.add_atmost(lits = [1, 10], k = 1, no_return = False)

		s.add_atmost(lits = [2, 9], k = 1, no_return = False)
		s.add_atmost(lits = [2, 8], k = 1, no_return = False)
		s.add_atmost(lits = [2, 11], k = 1, no_return = False)

		s.add_atmost(lits = [3, 5], k = 1, no_return = False)
		s.add_atmost(lits = [3, 10], k = 1, no_return = False)
		s.add_atmost(lits = [3, 12], k = 1, no_return = False)

		s.add_atmost(lits = [4, 6], k = 1, no_return = False)
		s.add_atmost(lits = [4, 11], k = 1, no_return = False)

		s.add_atmost(lits = [5, 14], k = 1, no_return = False)
		s.add_atmost(lits = [5, 3], k = 1, no_return = False)
		s.add_atmost(lits = [5, 11], k = 1, no_return = False)

		s.add_atmost(lits = [6, 4], k = 1, no_return = False)
		s.add_atmost(lits = [6, 13], k = 1, no_return = False)
		s.add_atmost(lits = [6, 15], k = 1, no_return = False)
		s.add_atmost(lits = [6, 12], k = 1, no_return = False)

		s.add_atmost(lits = [7, 1], k = 1, no_return = False)
		s.add_atmost(lits = [7, 9], k = 1, no_return = False)
		s.add_atmost(lits = [7, 14], k = 1, no_return = False)
		s.add_atmost(lits = [7, 16], k = 1, no_return = False)

		s.add_atmost(lits = [8, 15], k = 1, no_return = False)
		s.add_atmost(lits = [8, 10], k = 1, no_return = False)
		s.add_atmost(lits = [8, 2], k = 1, no_return = False)


		s.add_atmost(lits = [9, 15], k = 1, no_return = False)
		s.add_atmost(lits = [9, 7], k = 1, no_return = False)
		s.add_atmost(lits = [9, 2], k = 1, no_return = False)


		s.add_atmost(lits = [10, 1], k = 1, no_return = False)
		s.add_atmost(lits = [10, 3], k = 1, no_return = False)
		s.add_atmost(lits = [10, 8], k = 1, no_return = False)
		s.add_atmost(lits = [10, 16], k = 1, no_return = False)


		s.add_atmost(lits = [11, 2], k = 1, no_return = False)
		s.add_atmost(lits = [11, 4], k = 1, no_return = False)
		s.add_atmost(lits = [11, 13], k = 1, no_return = False)
		s.add_atmost(lits = [11, 5], k = 1, no_return = False)

		s.add_atmost(lits = [12, 14], k = 1, no_return = False)
		s.add_atmost(lits = [12, 6], k = 1, no_return = False)
		s.add_atmost(lits = [12, 3], k = 1, no_return = False)

		s1 = Minicard()
		pieces = make_board(1, [], 4)
		s1 = add_knight_moves(s1, pieces, 8, 4)
		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())




class TestAddOverlap(unittest.TestCase):


	def testOverlap3(self):
		N = 3
		#print("HIHIHI"*20)
		s = Minicard()

		s.add_atmost(lits = [1, 10], k = 1, no_return = False)
		s.add_atmost(lits = [2, 11], k = 1, no_return = False)
		s.add_atmost(lits = [3, 12], k = 1, no_return = False)
		s.add_atmost(lits = [4, 13], k = 1, no_return = False)
		s.add_atmost(lits = [5, 14], k = 1, no_return = False)
		s.add_atmost(lits = [6, 15], k = 1, no_return = False)
		s.add_atmost(lits = [7, 16], k = 1, no_return = False)
		s.add_atmost(lits = [8, 17], k = 1, no_return = False)
		s.add_atmost(lits = [9, 18], k = 1, no_return = False)

		s1 = Minicard()
		pieces1 = make_board(1, [], N)
		pieces2 = make_board(10, [], N)
		s1 = add_overlap(s1, [pieces1, pieces2], N)

		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())

	def testOverlap4(self):
		N = 4
		#print("HIHIHI"*20)
		s = Minicard()

		s.add_atmost(lits = [1, 17], k = 1, no_return = False)
		s.add_atmost(lits = [2, 18], k = 1, no_return = False)
		s.add_atmost(lits = [3, 19], k = 1, no_return = False)
		s.add_atmost(lits = [4, 20], k = 1, no_return = False)
		s.add_atmost(lits = [5, 21], k = 1, no_return = False)
		s.add_atmost(lits = [6, 22], k = 1, no_return = False)
		s.add_atmost(lits = [7, 23], k = 1, no_return = False)
		s.add_atmost(lits = [8, 24], k = 1, no_return = False)
		s.add_atmost(lits = [9, 25], k = 1, no_return = False)
		s.add_atmost(lits = [10, 26], k = 1, no_return = False)
		s.add_atmost(lits = [11, 27], k = 1, no_return = False)
		s.add_atmost(lits = [12, 28], k = 1, no_return = False)
		s.add_atmost(lits = [13, 29], k = 1, no_return = False)
		s.add_atmost(lits = [14, 30], k = 1, no_return = False)
		s.add_atmost(lits = [15, 31], k = 1, no_return = False)
		s.add_atmost(lits = [16, 32], k = 1, no_return = False)



		s1 = Minicard()
		pieces1 = make_board(1, [], N)
		pieces2 = make_board(17, [], N)
		s1 = add_overlap(s1, [pieces1, pieces2], N)

		self.assertEqual(s.solve(), s1.solve())
		self.assertEqual(s.get_model(), s1.get_model())


class TestPrintBoard(unittest.TestCase):

	def testPrintB3(self):
		



if __name__ == '__main__':
	unittest.main()












