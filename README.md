# Mycaptain-Project
#Task 1
import math
radius = float(input("the radius of the circle: "))
area = math.pi * radius**2
print("The area of the circle with radius", radius, "is", area)

Output:
Enter the radius of the circle: 1.1
The area of the circle with radius 1.1 is 3.8013271108436504


#Task 2
filename = input("Filename: ")
extension = filename.split(".")[-1]
print("The extension of the file is: " + extension)

Output:
Filename: abc.py
The extension of the file is: py
