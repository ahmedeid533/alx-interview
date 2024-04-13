#!/usr/bin/python3
""" N queens problem """
import sys


def is_safe(board, row, col, n):
	""" Check if a queen can be placed on board[row][col] """
	for i in range(col):
		if board[row][i] == 1:
			return False
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	for i, j in zip(range(row, n, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	return True


def solve(board, col, n):
	""" Solve the N queens problem """
	if col == n:
		print([[i, row.index(1)] for i, row in enumerate(board)])
		return
	for i in range(n):
		if is_safe(board, i, col, n):
			board[i][col] = 1
			solve(board, col + 1, n)
			board[i][col] = 0
	
def nqueens(n):
	""" N queens problem """
	if n < 4:
		print("N must be at least 4")
		return
	board = [[0 for i in range(n)] for j in range(n)]
	solve(board, 0, n)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: nqueens N")
		sys.exit(1)
	try:
		n = int(sys.argv[1])
	except ValueError:
		print("N must be a number")
		sys.exit(1)
	nqueens(n)
