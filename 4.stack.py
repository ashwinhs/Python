class Stack:
	def __init__(self):
		self.list = []
	
	def push(self, obj):
		self.list.append(obj)
	
	def pop(self):
		return self.list.pop()
	
	def peek(self):
		return self.list[len(self.list) - 1]
	
	def isEmpty(self):
		return self.list == []
	
	def size(self):
		return len(self.list)
		

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())	

def revString(string):
	s = Stack()
	for c in string:
		s.push(c)
	
	while not s.isEmpty():
		print(s.pop(), end = '')

def parcheck(string):
	s = Stack()
	balanced = True
	for c in string:
		if c == "(":
			s.push(c)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
	return balanced

def matches(top, current):
  dict = {'[':']', '{':'}', '(':')'}
  return dict[top] == current
  
def parcheckMulti(string):
	s = Stack()
	balanced = True
	for c in string:
		if c in "([{":
		  s.push(c)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, c):
				  balanced = False
	return balanced	and s.isEmpty()
