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

def convertToPostFix(string):
	finalString = ''
	wordList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	opsList = '+,/*'
	s = Stack()
	for i in string:
		if i in wordList:
			finalString += i
		if i in opsList:
			if s.isEmpty():
				s.push(i)
			elif opsList.find(s.peek()) >= opsList.find(i):
				finalString += s.pop()
				s.push(i)
			else:
				finalString += i
		if i == ')'
			finalString += s.pop()
	while not s.isEmpty():
		finalString += s.pop()
		
print(convertToPostFix('A * B + C * D'))
print(convertToPostFix("( A + B ) * C - ( D - E ) * ( F + G )")) #A B + C * D E - F G + * -
print(convertToPostFix("( A + B ) * ( C + D )")) #'A B + C D + *'
print(convertToPostFix("( A + B ) * C")) #'A B + C *'
print(convertToPostFix("A + B * C")) #'A B C * +'