def prime(n):
	#returning True if n is a prime number
	if type(n) != int: return None
	if n<2:
		return False
	if n == 2:
		return True
	for x in range(2,int(n**(1/2))+2):
		if n%(x) == 0:
			return False
	return True


class Spiral:
	directions = {'left': (-1,0,'up'), 'up': (0,-1,'right'), 'right': (1,0,'down'), 'down': (0,1,'left')}

	def __init__(self):
		self.max = 1
		self.n = 1
		self.diagonal = {1}
		self.primes = set()
	
	def add(self, n=1):
		#adding n cycles of spiral
		for x in range(n):
			for x in range(4):
				new = self.max + (self.n + 1)*(x+1)
				self.diagonal.add(new)
				if prime(new):				
					self.primes.add(new)
			self.n = self.n + 2
			self.max = self.n * self.n
	
	def show(self):
		print(self.n, self.max, self.percent())

	def percent(self):
		#what percentage of numbers on both diagonals are prime numbers
		return (len(self.primes)/len(self.diagonal))*100

	def draw(self):
		#draw method prints Ulam spiral with a side length of self.n
		#creating NxN board matrix filled with 0s:
		board = []	
		for x in range(self.n):
			board.append([])
			for y in range(self.n):
				board[x].append(0)

		k = self.max
		x = self.n-1
		y = self.n-1
		where = 'left'
		#board is filled with values inside the while loop
		#starting in the bottom right corner clockwise:
		while k != 0:
			board[x][y] = k
			x1,y1 = (x+self.directions[where][0],y+self.directions[where][1])

			#if board[x1][y1] is already filled or outside the board: change direction
			if(x1 < 0 or y1 < 0 or x1 == self.n or y1 == self.n or board[x1][y1] != 0):
				where = self.directions[where][2]

			x,y = (x+self.directions[where][0],y+self.directions[where][1])
			k = k-1

		#printing spiral:
		for x in range(self.n):
			for y in range(self.n):
				print(str(board[y][x]) + ' '*(len(str(self.max))-len(str(board[y][x]))+1), end = '')
			print('')
	
#just testing:
a = Spiral()
a.add(5)
a.show()
a.draw()

