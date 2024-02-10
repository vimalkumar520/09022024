#Triangle Classifier
#Write a program that classifies a triangle based on its side lengths.
print("####Triangle Classifier####")
side1 = int(input("Enter the 1st Side of triangle: "))
side2 = int(input("Enter the 2nd Side of triangle: "))
side3 = int(input("Enter the 3rd Side of triangle: "))
if side1 == side2 == side3:
    print("All sides of the triangle are equal, Its an Equilateral Triangle")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("Exactly two sides are equal only equal, Its an Isosceles  Triangle")
else:
    print("No sides are equal, Its an Scalene Triangle")
