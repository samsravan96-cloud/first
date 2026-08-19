a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a <= 0 or b <= 0 or c <= 0 or a+b+c!=180:
    print("Not a valid triangle")

elif a == b == c:
    print("Equilateral triangle")

elif a == b or b == c or a == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")