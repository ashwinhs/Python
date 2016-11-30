d = {'(' : 1, ')' : -1}

floor = 0
i = 0
char = ""
with open('Day1.in') as f:
    for i, char in enumerate(f.read(), 1):
        floor += d[char]
        print(floor)
        if floor < 0:
            break
print("{} {}".format(i, char))
        
