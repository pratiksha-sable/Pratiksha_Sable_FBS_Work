D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter Amount : "))

count = 0

for note in D:
    if (amount >= note):
        n = amount // note
        count = count + n
        amount = amount % note
        print(note, "notes : ", n)

print("Minimum number of notes : ", count)