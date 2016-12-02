from Deque import Deque

d = Deque()
def palinMethod1(string):
    strRev = ""
    for i in string:
        d.addRear(i)
    
    while not d.isEmpty():
        strRev += d.removeRear()
    
    return string.lower() == strRev.lower()

def palinMethod2(string):
    [d.addRear(i) for i in string if i.isalpha()]
    
    isStillEq = True
    while isStillEq and d.size() > 1:
        if not d.removeFront().lower() == d.removeRear().lower():
            isStillEq = False
    
    return isStillEq
        
    
string = "Malayalam1"
print(palinMethod1(string))

string = "Madam I'm Adam"
print(palinMethod2(string))
