# 1. Write a Python program to find the value of PI.

import math

diameter = 20000
circumference = (100 + 4) * 8 + 62000 - 20
aryabhata_pi = circumference / diameter

print("Circumference (Aryabhata):", circumference)
print("Aryabhata's Pi approximation:", aryabhata_pi)
print("Modern Pi:", math.pi)

# 2. 𝐬𝐢𝐧 𝟐 𝜽 + 𝐜𝐨𝐬 𝟐 𝜽 = 𝟏

import math

theta = float(input("Enter angle in degrees: "))
rad = math.radians(theta)

result = (math.sin(rad))**2 + (math.cos(rad))**2

print("sin2θ + cos2θ =", result)

# 3. Write a Python program to compute sine values from 0° to 90° using Aryabhata’s recursive method.

import math

R = 3438
steps = 12
h = (math.pi / 2) / steps
J = [0.0]

print("n Angle(deg) Jya (Aryabhata) sin(theta)")

for n in range(steps):
    next_J = J[n] + R * h - (h**2 / R) * J[n]
    J.append(next_J)

angle_deg = (n + 1) * 90 / steps
modern_sin = math.sin(math.radians(angle_deg))

print(f"{n+1:2d} {angle_deg:8.2f}° {next_J:10.4f} {modern_sin: .6f}")


# 4.Write a Python program to calculate the area of a circle using the Śulba Sūtras approximation method.

diameter = float(input("Enter the diameter of the circle: "))

side = (8/9) * diameter

area = side ** 2

print("Approximate Area of Circle =", round(area, 4))

# 5. the area of a triangle by taking the base and height as input from the user.

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height
print("Area of Triangle =", round(area, 4))

# 6. the area of a cyclic quadrilateral using Brahmagupta’s formula.

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))

s = (a + b + c + d) / 2

area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))
print("Area of Cyclic Quadrilateral =", round(area, 4))

# 7. Write a Python code Using Yavadunam, compute: 97 × 104

def yavadunam_multiplication(a, b, base=100):
    dev_a = a - base
    dev_b = b - base
    left_part = a + dev_b 
    right_part = dev_a * dev_b
    result = left_part * base + right_part
    return result

a = 97
b = 104
answer = yavadunam_multiplication(a, b)

print(f"Using Yavadunam, {a} × {b} = {answer}")

# 8. Write a Python code Using Vyastisamanstih, expand: (x + 5)(x + 7)

a = 5
b = 7

# Using formula (x + a)(x + b) = x2 + (a+b)x + ab
print(f"x2 + {a+b}x + {a*b}")

# 9. Write a Python code Using Vistaran, expand: (x + 6 + 1)²

a = 6
b = 1
total = a + b

print("Expansion using Vistaran:")
print(f"x2 + {2*total}x + {total**2}")

# 10. Write a Python code Using Sesanyan, find remainder of 1345 ÷ 7

number = 1345
divisor = 7

remainder = number % divisor

print("Using Sesanyan Sutra:")
print(f"Remainder of {number} ÷ {divisor} is {remainder}")