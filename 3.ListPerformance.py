from timeit import Timer


#Concatenate
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
#Append
def test2():
    l = []
    for i in range(1000):
        l.append(i)

#Create using Compehension
def test3():
    l = [i for i in range(1000)]

#Using Range and list function
def test4():
    l = list(range(1000))
  
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
   
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
					   
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))

import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)} #Create dictionary
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
