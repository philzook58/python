

# HUH ACTUALLY finding wherethe most recent guy to push on is a bitch
#{left: None, right: None, parent: , val: }

class PriorityQueue:
	"""Array-based priority queue implementation."""
	def __init__(self):
		"""Initially empty priority queue."""
		self.queue = []
		self.min_index = 0
	
	def __len__(self):
		# Number of elements in the queue.
		return len(self.queue)
	
	def append(self, key):
		"""Inserts an element in the priority queue."""
		if key is None:
			raise ValueError('Cannot insert None in the queue')
		self.queue.append(key)
		self.heapify(len(self)-1)
		#self.min_index = None

	def heapify(self,index):
		#level,leaf = self.parent(level, leaf)
		level, leaf = self.levelleaf(index)
		print level,leaf
		while level != 0:
			level,leaf = self.parent(level, leaf)
			index = self.index(level,leaf)
			parVal = self.queue[index]
			leftlevel ,leftleaf = self.left(level,leaf)
			rightlevel, rightleaf = self.right(level,leaf)
			leftVal = self.queue[self.index(leftlevel,leftleaf)]
			print index

			
			if self.index(rightlevel,rightleaf) < len(self):
				rightVal = self.queue[self.index(rightlevel,rightleaf)]
				if parVal <= leftVal and parVal <= rightVal:
					break
				elif leftVal <= parVal and leftVal <= rightVal:
					self.queue[self.index(leftlevel, leftleaf)] = parVal
					self.queue[index] = leftVal
				else: # rightVal <= parVal and rightVal <= leftVal:
					self.queue[self.index(rightlevel,rightleaf)] = parVal
					self.queue[index] = rightVal
			else: # special case for very bottom edge of tree which happens almst every time
				if parVal <= leftVal:
					break
				else:
					self.queue[self.index(leftlevel, leftleaf)] = parVal
					self.queue[index] = leftVal


			
	
	def min(self):
		"""The smallest element in the queue."""
		if len(self.queue) == 0:
			return None
		#self._find_min()
		return self.queue[self.min_index]

	def pop(self):
		"""Removes the minimum element in the queue.
	
		Returns:
			The value of the removed element.
		"""
		#push hole down

		if len(self.queue) == 0:
			return None
		min_key = self.min()

		finallevel, lastleaf = self.levelleaf(len(self.queue))
		level = 0
		leaf = 0
		while level < finallevel:
			leftlevel ,leftleaf = self.left(level,leaf)
			rightlevel, rightleaf = self.right(level,leaf)
			if self.index(leftlevel,leftleaf) >= len(self.queue)-1:
				break
			leftVal = self.queue[self.index(leftlevel,leftleaf)]

			if self.index(rightlevel,rightleaf) >= len(self.queue)-1: #hit last element
				self.queue[self.index(level,leaf)] = leftVal
				leaf = leftleaf
				level = leftlevel
				break

			rightVal = self.queue[self.index(rightlevel,rightleaf)]
			if leftVal < rightVal:
				self.queue[self.index(level,leaf)] = leftVal
				leaf = leftleaf
				level = leftlevel
			else:
				self.queue[self.index(level,leaf)] = rightVal
				leaf = rightleaf
				level = rightlevel
		self.queue[self.index(level,leaf)] = self.queue[-1] 
		self.heapify(self.index(level,leaf))
		self.queue.pop()

		#self._find_min()

		return min_key
	
	def _find_min(self):
		# Computes the index of the minimum element in the queue.
		#
		# This method may crash if called when the queue is empty.
		if self.min_index is not None:
			return
		min = self.queue[0]
		self.min_index = 0
		for i in xrange(1, len(self.queue)):
			key = self.queue[i]
			if key < min:
				min = key
				self.min_index = i
	def index(self, level, leaf):
		return 2**level + leaf - 1
	def parent(self, level, leaf):
		return (level-1, leaf//2)
	def left(self, level, leaf):
		return (level + 1, 2*leaf)
	def right(self, level, leaf):
		return (level + 1, 2*leaf+1)
	def levelleaf(self,index):
		level = 0
		while index >= 2**(level+1)-1:
			#index = index/2
			level = level + 1
		leaf = index - 2**level + 1
		return (level, leaf)