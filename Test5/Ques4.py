a = [10, 20, 10, 30, 20, 10, 40]

d = {}

for i in a:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)