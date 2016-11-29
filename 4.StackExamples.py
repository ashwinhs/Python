from stack import Stack

#Reverse a Strung using a Stack
def revString(string):
	s = Stack()
	for c in string:
		s.push(c)
	
	while not s.isEmpty():
		print(s.pop(), end = '')

#Check if the parantheses are balanced
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

#Match function used by parcheckMulti
def matches(top, current):
  dict = {'[':']', '{':'}', '(':')'}
  return dict[top] == current
 
#Check if the brackets includes ( or [ or {, are balanced
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

#Convert a Decimal number to Binary
def dec2bin(num):
	s = Stack()
	while num > 0:
		s.push(num % 2)
		num = num //2
	
	while not s.isEmpty():
		print(s.pop(), end = '')

#Convert a Decimal number to Any other base number
def baseConverter(num, base):
	s = Stack()
	numStr = '0123456789ABCDEF'
	fNum = ''
	while num > 0:
		rem = num % base
		s.push(rem)
		num = num // base

	while not s.isEmpty():
	  fNum = fNum + numStr[s.pop()] if base == 16 else str(s.pop())
	return fNum
