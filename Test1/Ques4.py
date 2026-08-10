area = int(input("Enter area of one wall : "))
interior_cost = int(input("Enter interior painting cost : "))
exterior_cost = int(input("Enter exterior painting cost : "))

interior_painting_cost = 7 * area * interior_cost
exterior_painting_cost = 6 * area * exterior_cost

total_cost = interior_painting_cost + exterior_painting_cost

print("Interior Painting Cost : ", interior_painting_cost)
print("Exterior Painting Cost : ", exterior_painting_cost)
print("Total Painting Cost : ", total_cost)