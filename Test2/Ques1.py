n = int(input("Enter Number : "))
count = 0
num = 2
while (count < n):
    c = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            c += 1
    if (c == 2):
        print(num, end = " ")
        count += 1
    num += 1