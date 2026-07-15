a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid triangle.")
else:
    print("The sides can not form a valid triangle.")
