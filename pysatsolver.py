from pysat.formula import CNF
from pysat.solvers import Minicard
import sys




# Makes a list of size N * N for any type of piece.
# Start indicates the starting number for each location so that
# there is no overlap between pieces
def make_board(start, pieces, N):

	count = start
	for x in range(N):
		col = []
		for y in range(N):
			col.append(count)
			count += 1
		pieces.append(col)

	return pieces



# Adds horizontal checkers for this type of piece, making sure there is a max of 1 piece in each row/column
# S represents the SAT solver
# Pieces represents the list of pieces being passed in (e.g. rooks or queens)
# Num represents the minimum number of pieces required on the board
def add_horizontals(s, pieces, num, N):

	clause = []
	minclause = []
	for x in range(N):
		for y in range(N):
			clause.append(pieces[x][y])
			minclause.append( -1 * pieces[x][y])
	s.add_clause(clause, no_return = False)
	s.add_atmost(lits = minclause.copy(), k = (N * N - num), no_return = False)


	for x in range(N):
		atmostcol = []
		atmostcol.extend(pieces[x])
		s.add_atmost(lits = atmostcol.copy(), k = 1, no_return = False)

	for y in range(N):
		atmostrow = []
		for x in range(N):
			atmostrow.append(pieces[x][y])
		s.add_atmost(lits = atmostrow.copy(), k = 1, no_return = False)
	return s



# Adds diagonal checkers for this type of piece, making sure there is a max of 1 piece in each diagonal
# S represents the SAT solver
# Pieces represents the list of pieces being passed in (e.g. bishops or queens)
# Num represents the minimum number of pieces required on the board
def add_diagonals(s, pieces, num, N):

	clause = []
	minclause = []
	for x in range(N):
		for y in range(N):
			clause.append(pieces[x][y])
			minclause.append( -1 * pieces[x][y])
	s.add_clause(clause, no_return = False)
	s.add_atmost(lits = minclause.copy(), k = (N * N - num), no_return = False)


	for x in range(N):
		atmostrightx = []
		for y in range(N - x):
			atmostrightx.append(pieces[x + y][y])

		s.add_atmost(lits = atmostrightx.copy(), k = 1, no_return = False)

	for y in range(N):
		atmostrighty = []
		for x in range(N - y):
			atmostrighty.append(pieces[x][y + x])
		
		s.add_atmost(lits = atmostrighty.copy(), k = 1, no_return = False)

	for x in range(N):
		atmostleftx = []
		for y in range(x + 1):
			atmostleftx.append(pieces[x - y][y])

		s.add_atmost(lits = atmostleftx.copy(), k = 1, no_return = False)


	for x in range(N):
		atmostlefty = []
		for y in range(N - x):
			atmostlefty.append(pieces[x + y][abs(N - y - 1)])
		
		s.add_atmost(lits = atmostlefty.copy(), k = 1, no_return = False)

	return s



# Adds knight move checkers for this type of piece, making sure there is a max of 1 piece attacking each other
# through a knight move
# S represents the SAT solver
# Pieces represents the list of pieces being passed in (e.g. knights)
# Num represents the minimum number of pieces required on the board
def add_knight_moves(s, pieces, num, N):

	clause = []
	minclause = []
	for x in range(N):
		for y in range(N):
			clause.append(pieces[x][y])
			minclause.append( -1 * pieces[x][y])
	s.add_clause(clause, no_return = False)
	s.add_atmost(lits = minclause.copy(), k = (N * N - num), no_return = False)

	#(p.x == piece.x - 2 and p.y == piece.y - 1) 
	#or (p.x == piece.x - 2 and p.y == piece.y + 1)
	#or (p.x == piece.x + 2 and p.y == piece.y - 1)
	#or (p.x == piece.x + 2 and p.y == piece.y + 1)
	#or (p.x == piece.x - 1 and p.y == piece.y - 2)
	#or (p.x == piece.x - 1 and p.y == piece.y + 2)
	#or (p.x == piece.x + 1 and p.y == piece.y - 2)
	#or (p.x == piece.x + 1 and p.y == piece.y + 2)

	for x in range(N):
		for y in range(N):
			knightmoves = []

			move = [x - 2, y - 1]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x - 2, y + 1]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x + 2, y - 1]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x + 2, y + 1]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x - 1, y - 2]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x - 1, y + 2]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x + 1, y - 2]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)

			move = [x + 1, y + 2]
			if (not (move[0] < 0 or move[1] < 0 or move[0] >= N or move[1] >= N)):
				knightmoves = [pieces[x][y]]
				knightmoves.append(pieces[move[0]][move[1]])
				s.add_atmost(lits = knightmoves, k = 1, no_return = False)



	return s

# Makes sure that there is a maximum of 1 type of piece on each square
def add_overlap(s, pieces, N):

	for x in range(N):
		for y in range(N):
			overlap = []
			for p in pieces:
				overlap.append(p[x][y])
			s.add_atmost(lits = overlap.copy(), k = 1, no_return = False)

	return s

# given the SAT solvers output, prints out the output in a readable manner
def print_board(solution, N):
	print()

	for p in range(N * N):
		rook = solution[p]
		bish = solution[N * N + p]
		queen = solution[2 * N * N + p]
		knight = solution[3 * N * N + p]

		if (knight > 0):
			print(" K ", end = '')
		elif (rook > 0):
			print(" R ", end = '')
		elif (bish > 0):
			print(" B ", end = '')
		elif (queen > 0):
			print(" Q ", end = '')
		else:
			print("   ", end = '')

		if ((p + 1) % N == 0):
			print()


	print()
	return





if __name__ == '__main__':

	# Makes sure user is giving an input for the board size
	if (len(sys.argv) != 2):
		print("Usage: pysat-solver.py N")
		#quit()


	# N represents the board size
	N = int(sys.argv[1])

	# Makes a board for each type of piece
	rooks = []
	rooks = make_board(1, rooks, N)

	bishops = []
	bishops = make_board(N * N + 1, bishops, N)

	queens = []
	queens = make_board(2 * N * N + 1, queens, N)

	knights = []
	knights = make_board(3 * N * N + 1, knights, N)


	s = Minicard()



	# Maximizes the number of knights. If the solver works for X number of knights,
	# it tries again for X + 1
	numknights = N - 1
	while(s.solve()):
		numknights += 1
		s = Minicard()
		s = add_horizontals(s, rooks, N, N)
		s = add_diagonals(s, bishops, (2 * N - 2), N)
		s = add_horizontals(s, queens, N, N)
		s = add_diagonals(s, queens, N, N)
		s = add_knight_moves(s, knights, numknights, N)
		s = add_overlap(s, [rooks, bishops, queens, knights], N)
		
		#print(s.solve())


	# Because the above clause runs until failure, this takes the solver back one step
	# so it demonstrates the maximum number of knights
	numknights -= 1
	s = Minicard()
	s = add_horizontals(s, rooks, N, N)
	s = add_diagonals(s, bishops, (2 * N - 2), N)
	s = add_horizontals(s, queens, N, N)
	s = add_diagonals(s, queens, N, N)

	s = add_knight_moves(s, knights, numknights, N)

	s = add_overlap(s, [rooks, bishops, queens, knights], N)

	print(s.solve())



	maxlen = 0
	models = list(s.enum_models())

	if (len(models) > 0):
		for p in models[0]:
			if (p > 0):
				maxlen += 1

	maxlen = numknights + N + N + (2 * N - 2)


	for n in models:
		#print(n)
		print_board(n, N)
		print('- ' * 20)



	print("numsolutions = ", len(models))
	print("length = ", maxlen)

















