# Solve the quadratic equation ax² + bx + c = 0
import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

# Test with x² - 5x + 6 = 0 
print(quadratic_solver(1, -5, 6))  # Output: (3.0, 2.0)

