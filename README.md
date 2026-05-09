# rationalpy
Exact rational arithmetic for Python without floating-point precision loss.

A simple Python Fraction datatype implementation using Object-Oriented Programming and operator overloading.

This project performs exact fractional arithmetic instead of floating-point calculations.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Automatic fraction simplification
- Decimal conversion
- Handles negative fractions
- Prevents division by zero

## Example

```python
from fraction import Fraction

fr1 = Fraction(4, 6)
fr2 = Fraction(1, -8)

print(fr1)          # 2/3
print(fr2)          # -1/8

print(fr1 + fr2)    # 13/24
print(fr1 - fr2)    # 19/24
print(fr1 * fr2)    # -1/12
print(fr1 / fr2)    # -16/3

print(fr1.to_decimal())  # 0.6666666666666666
