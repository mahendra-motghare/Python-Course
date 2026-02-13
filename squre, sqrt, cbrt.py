# Print squre, sqrt & cubrt
import math

n = int(input("Enter number (n<1000): "))
if (n <= 9):
    print(n**2)
elif (9 < n <= 99):
    print(f"{math.sqrt(n):.2f}")
elif (n <= 999):
    print(f"{math.cbrt(n):.2f}")
else:
    print("Invalid")
