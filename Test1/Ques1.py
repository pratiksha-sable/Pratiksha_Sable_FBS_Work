length = int(input("Enter length : "))
breadth = int(input("Enter breadth : "))
radius = int(input("Enter radius : "))

area = (length * breadth) + (3.14 * radius * radius) / 2
print("Area : ", area)

perimeter = (2 * length) + breadth + (3.14 * radius)
print("Perimeter : ", perimeter)