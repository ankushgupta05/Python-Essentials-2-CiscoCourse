## Module 1


```
## Note :-
pi → a constant with a value that is an approximation of π;
radians(x) → a function that converts x from degrees to radians;
degrees(x) → acting in the other direction (from radians to degrees)


```


# Trigonometric Functions in Python (`math` Module)

The following table summarizes important trigonometric functions and constants available in Python's `math` module:

---

## Functions Table

| Function | Description | Example Usage | Output |
|:--------:|:------------:|:-------------:|:------:|
| `sin(x)` | Returns the sine of x radians | `x = math.pi/2`<br>`math.sin(x)` | `1.0` |
| `cos(x)` | Returns the cosine of x radians | `x = 0`<br>`math.cos(x)` | `1.0` |
| `tan(x)` | Returns the tangent of x radians | `x = math.pi/4`<br>`math.tan(x)` | `1.0` |
| `asin(x)` | Returns the arcsine (inverse sine) of x | `x = 1`<br>`math.asin(x)` | `1.5707963267948966 (π/2)` |
| `acos(x)` | Returns the arccosine (inverse cosine) of x | `x = 0`<br>`math.acos(x)` | `1.5707963267948966 (π/2)` |
| `atan(x)` | Returns the arctangent (inverse tangent) of x | `x = 1`<br>`math.atan(x)` | `0.7853981633974483 (π/4)` |
| `pi` | Constant value of π | `math.pi` | `3.141592653589793` |
| `radians(x)` | Converts degrees to radians | `x = 90`<br>`math.radians(x)` | `1.5707963267948966` |
| `degrees(x)` | Converts radians to degrees | `x = math.pi/2`<br>`math.degrees(x)` | `90.0` |

---

## How to Use

Make sure to import the `math` module before using these functions:

```python
import math

# Example Usage:

x = math.pi/2
print(math.sin(x))      # Output: 1.0

x = math.pi/2
print(math.degrees(x))  # Output: 90.0

