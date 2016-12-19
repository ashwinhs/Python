class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def setData(self, data):
    self.data = data
  
  def setNext(self, next):
    self.next = next
  
  def getData(self):
    return self.data
  
  def getNext(self):
    return self.next
  
  def __str__(self):
    return "{}".format(self.data)
  
  
class UnorderedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add(self, item):
    newNode = Node(item)
    if self.head == None:
      self.tail = newNode
    newNode.setNext(self.head)
    self.head = newNode
  
  def size(self):
    count = 0
    if self.head == None:
      return 0
    else:
      temp = self.head
      while temp != None:
        temp = temp.getNext()
        count += 1
    return count
  
  def search(self, item):
    found = False
    if self.head == None:
      return False
    else:
      temp = self.head
      while temp != None:
        if temp.getData() == item:
          found = True
        temp = temp.getNext()
    return found
  
  def remove(self, item):
    if self.head == None:
      return False
    else:
      found = False
      temp = self.head
      previous = None
      while temp != None and found == False:
        if temp.getData() == item:
          found = True
        else:
          previous = temp
          temp = temp.getNext()
      if previous == None:
        self.head = temp.getNext()
      else:
        previous.setNext(temp.getNext())
    return True
  
  def listAll(self):
    temp = self.head
    count = 0
    while temp != None:
      print(temp, end="->")
      temp = temp.getNext()
  
  def append(self, item):
    temp = self.head
    while not temp == None:
      last = temp
      temp = temp.getNext()
    newNode = Node(item)
    print(newNode)
    print(last.getNext())
    last.setNext(newNode)
    self.tail = newNode

  def appendv2(self, item):
    newNode = Node(item)
    self.tail.setNext(newNode)
    self.tail = newNode


myList = UnorderedList()
myList.add(10)
myList.add(20)
myList.add(40)

print(myList.size())
print(myList.search(20))

print(myList.size())
myList.append(50)
myList.appendv2(60)
print("-----")
myList.listAll()
print("\n-----")
