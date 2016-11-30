with open('Day1.in') as f:
    floor = sum(1 if i == '(' else -1 for i in f.read())
print(floor)


