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
  
  
class OrderedList:
  def __init__(self):
    self.head = None
    
  def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()

    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        temp.setNext(current)
        previous.setNext(temp)


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
    stop = False
    temp = self.head
    count = 0
    while temp != None and not stop:
      if temp.getData() == item:
        found = True
      elif temp.getData() > item:
        stop = True
      temp = temp.getNext()
      count += 1
      print("Ashwin " + str(count))
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
    while temp != None:
      print(temp, end="<--")
      temp = temp.getNext()
  
myList = OrderedList()
myList.add(10)
myList.add(20)
myList.listAll()
#myList.add(40)
#myList.add(50)

