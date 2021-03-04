import sys

if (len(sys.argv) != 2):
	print("Usage: sat-solver.py N")
	quit()


# N represents the board size
N = int(sys.argv[1])

# Represents a piece, with the type (queen, rook, bishop, or knight)
# as well as the x and y position on the board
class piece:
	def __init__(self, type, x, y):
		self.type = type
		self.x = x
		self.y = y

	def __str__(self):
		return ("" + type + x + y)

# Checks if a given x, y location contains a piece or not
def haspiece(board, x, y):
	for p in board:
		if (p.x == x and p.y == y):
			return (" " + p.type + " ")
	return "   "

# Prints a chessboard in a visually accurate manner
def printchessboard(board):
	for x in range(N):
		for y in range(N):
			print(haspiece(board, x, y), end = '')
		print("")

# Compares 2 boards. If they are the same, returns True.
# Returns false if they are not the same
def compareboards(b1, b2):
	if (len(b1) == len(b2)):
		same = True
		for p1 in b1:
			oneofthose = False
			for p2 in b2:
				if (p1.x == p2.x and p1.y == p2.y):
					oneofthose = True
			same = same and oneofthose
		return same
	else :
		return False

# Checks to see if a list of baords contains an instance of another board
# Returns True if it does contain that board, false otherwise
def boardscontains(board, listofb):
	for b in listofb:
		if (compareboards(b, board)):
			return True
	return False



# Returns false if it intersects with another piece, 
# return true if it is clear to place a piece down
def check_linear(placed_piece, board):
	if (not board):
		return True
	for p in board:
		if (p.x == placed_piece.x or p.y == placed_piece.y):
			return False

	return True


# Returns false if it intersects with another piece, 
# return true if it is clear to place a piece down
def check_diagonal(placed_piece, board):
	for p in board:
		if (abs(placed_piece.x - p.x) == abs(placed_piece.y - p.y)):
			return False
	return True


# given a piece and board, return true if the square is not being attacked by a knight
# returns false otherwise
def check_knight(piece, board):
	for p in board:
		if ((p.x == piece.x - 2 and p.y == piece.y - 1) 
			or (p.x == piece.x - 2 and p.y == piece.y + 1)
			or (p.x == piece.x + 2 and p.y == piece.y - 1)
			or (p.x == piece.x + 2 and p.y == piece.y + 1)
			or (p.x == piece.x - 1 and p.y == piece.y - 2)
			or (p.x == piece.x - 1 and p.y == piece.y + 2)
			or (p.x == piece.x + 1 and p.y == piece.y - 2)
			or (p.x == piece.x + 1 and p.y == piece.y + 2)):
			return False
	
	return True



def make_queen_boards(currentboard, y):
	global queen_boards
	global N

	if (y == N):
		return

	for x in range(N):
		if (check_linear(piece("Q", x, y), currentboard)
			and check_diagonal(piece("Q", x, y), currentboard)):

			currentboard.append(piece("Q", x, y))

			if (len(currentboard) == N):
				queen_boards.append(currentboard.copy())

			make_queen_boards(currentboard, y + 1)
			currentboard.pop()


# Generates all possibilities for boards with N rooks following the rules
# of the chess puzzle
def make_rook_boards(currentboard, y):
	global rook_boards
	global N

	if (y == N):
		return

	for x in range(N):
		if (check_linear(piece("R", x, y), currentboard)):
			currentboard.append(piece("R", x, y))

			if (len(currentboard) == N):
				rook_boards.append(currentboard.copy())

			make_rook_boards(currentboard, y + 1)
			currentboard.pop()


# Generates all possibilities for boards with bishops following the rules
# of the chess puzzle
def make_bish_boards():
	for x in range (N):
		for y in range(N):
			make_bish_boards_r([piece("B", x, y)], 0)

# Recursive function for generating bishop boards
def make_bish_boards_r(currentboard, y):
	global bish_boards
	global N

	if (y == N):
		return

	for x in range(N):


		if (check_diagonal(piece("B", x, y), currentboard)):


			currentboard.append(piece("B", x, y))

			if (len(currentboard) == ((2 * N) - 2)):
				if(not boardscontains(currentboard, bish_boards)):
					bish_boards.append(currentboard.copy())

			if (x == N - 1):
				make_bish_boards_r(currentboard, y + 1)
			else:
				make_bish_boards_r(currentboard, y)
			currentboard.pop()
		else:
			if (x == N - 1):
				make_bish_boards_r(currentboard, y + 1)


maxlen = 0
def make_knight_boards(combinedboards):
	for b in combinedboards:
		for x in range (N):
			for y in range(N):
				make_knight_boards_r([piece("K", x, y)], 0, 0, b)

def make_knight_boards_r(currentboard, y, startx, b):
	global knight_boards
	global N
	global maxlen
	global solved

	if (y == N):
		return

	for x in range(startx, N):

		if (check_knight(piece("K", x, y), currentboard) and (haspiece(b, x, y) == "   ")):

			currentboard.append(piece("K", x, y))
			
			if (len(currentboard) > maxlen):
				maxlen = len(currentboard)
				knight_boards = []
				knight_boards.append(currentboard.copy())
				solved = []
				combd = comboard(b, currentboard.copy())
				if (not combd == []):
					solved.append(combd.copy())

			elif (len(currentboard) == maxlen):
				if(not boardscontains(currentboard, knight_boards)):
					knight_boards.append(currentboard.copy())
					combd = comboard(b, currentboard.copy())
					if (not combd == []):
						solved.append(combd.copy())

			if (x == N - 1):
				make_knight_boards_r(currentboard, y + 1, 0, b)
			else:
				make_knight_boards_r(currentboard, y, x + 1, b)
			currentboard.pop()
		else:
			if (x == N - 1):
				make_knight_boards_r(currentboard, y + 1, 0, b)



# prints 
def printboard(board):
	for p in board:
		print(#"Piece, x, y", 
			p.type, p.x, p.y)
	return

# Combines two boards with no overlap in pieces. If there is any overlap,
# it returns an empty list.
def comboard(board1, board2):
	newboard = []
	for p1 in board1:
		for p2 in board2:
			if (p1.x == p2.x and p1.y == p2.y):
				return []

	newboard.extend(board1.copy())
	newboard.extend(board2.copy())

	#printboard(newboard)

	return newboard

# Given 3 lists of boards, it returns all given combinations of the 3 types of boards.
def combineboards(queen_boards, rook_boards, bish_boards):
	combinedall = []
	combinedqr = []
	for q in queen_boards:
		for r in rook_boards:
			combined = comboard(q, r)
			if (combined == []):
				continue
			else:
				combinedqr.append(combined)
				#print("- " * 20)
				#printboard(combined)

	
	
	for c in combinedqr:
		for b in bish_boards:
			combined = comboard(c, b)
			if (combined == []):
				continue
			else:
				combinedall.append(combined)

	return combinedall




rook_boards = []
make_rook_boards([], 0)

bish_boards = []
make_bish_boards()

queen_boards = []
make_queen_boards([], 0)


combined = combineboards(queen_boards, rook_boards, bish_boards)

solved = []

knight_boards = []
make_knight_boards(combined)







for b in solved:
	print('- ' * 20)
	printchessboard(b)
	print('- ' * 20)
print("numsolutions = ", len(solved))
print("length = ", len(solved[0]) - 1)

#print(len(combined))
















