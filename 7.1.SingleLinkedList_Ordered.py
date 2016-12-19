class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
  def getNext(self):
    return self.next
  
  def setNext(self, next):
    self.next = next
  
  def getValue(self):
    return self.value
  
  def setValue(self, value):
    self.value = value
  
  def __str__(self):
    return "Node{}".format(self.value)
    

class UnorderedList:
  def __init__(self):
    self.head = None

  def addItem(self, value):
    tempNode = Node(value)
    tempNode.setNext(self.head)
    self.head = tempNode
  
  def search(self, value):
    tempNode = self.head
    found = False
    count = 0
    while tempNode != None and not found:
      print(tempNode)
      if tempNode.getValue() == value:
        found = True
      else:
        tempNode = tempNode.getNext()
        count += 1
    if found:
      print("Found Value {} @ Node {} Position {}".format(value, tempNode, count+1))
    else:
      print("Not Found Value {}".format(value))
    
  def removeItem(self, value):
    tempNode = self.head
    prevNode = None
    found = False
    count = 0
    while tempNode != None and not found:
      if tempNode.getValue() == value:
        found = True
        if prevNode == None:
          self.head = tempNode.getNext()
        else:
          prevNode.setNext(tempNode.getNext())
      else:
        prevNode = tempNode
        tempNode = tempNode.getNext()
        count += 1
  
  def append(self, value):
    tempNode = self.head
    newNode = Node(value)
    if tempNode == None:
      self.addItem(value)
    else:
      while tempNode.getNext() != None:
        tempNode = tempNode.getNext()
      tempNode.setNext(newNode)

  def traverse(self):
    tempNode = self.head
    while tempNode != None:
      print(tempNode)
      tempNode = tempNode.getNext()
  
  def len(self):
    count = 0
    tempNode = self.head
    while tempNode != None:
      count += 1
      tempNode = tempNode.getNext()
    return(count)
  
  def insertItem(self, value, position):
    if self.len() < position:
      self.append(value)
    else:
      newNode = Node(value)
      tempNode = self.head
      if position in [0, 1]:
        newNode.setNext(self.head)
        self.head = newNode
      else:
        for i in range(1, position-1):
          tempNode = tempNode.getNext()
        print("{} {}".format(tempNode, newNode))
        newNode.setNext(tempNode.getNext())
        tempNode.setNext(newNode)
  
  def pop(self):
    tempNode = self.head
    prevNode = None
    while tempNode.getNext() != None:
      prevNode = tempNode
      tempNode = tempNode.getNext()
    
    prevNode.setNext(None)
    return tempNode

UL1 = UnorderedList()
UL1.append(50)
UL1.addItem(10)
UL1.addItem(20)
UL1.addItem(30)
UL1.traverse()
UL1.search(40)
UL1.insertItem(100, 2)
UL1.traverse()
print(UL1.len())
print(UL1.pop())
print("-"*30)
UL1.traverse()

