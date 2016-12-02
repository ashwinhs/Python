class Deque:
	def __init__(self):
		self.deque = []
	
	def isEmpty(self):
		return self.deque == []
	
	def size(self):
		return len(self.deque)

	def addRear(self, item):
		self.deque.insert(0, item)
	
	def addFront(self, item):
		self.deque.append(item)
	
	def removeRear(self):
		return self.deque.pop(0)

	def removeFront(self):
		return self.deque.pop()

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())	