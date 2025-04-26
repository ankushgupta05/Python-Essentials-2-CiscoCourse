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

python
import math

# Example Usage:

x = math.pi/2
print(math.sin(x))      # Output: 1.0

x = math.pi/2
print(math.degrees(x))  # Output: 90.0








# Exponentiation and Logarithmic Functions in Python (`math` Module)

The following table summarizes important exponentiation and logarithmic functions available in Python's `math` module:


## Functions Table

| Function | Description | Example Usage | Output |
|:--------:|:------------:|:-------------:|:------:|
| `e` | Constant value of Euler's number | `math.e` | `2.718281828459045` |
| `exp(x)` | Returns the value of e raised to the power x (eˣ) | `x = 2`<br>`math.exp(x)` | `7.38905609893065` |
| `log(x)` | Returns the natural logarithm (base e) of x | `x = math.e`<br>`math.log(x)` | `1.0` |
| `log(x, b)` | Returns the logarithm of x to base b | `x = 8, b = 2`<br>`math.log(x, b)` | `3.0` |
| `log10(x)` | Returns the base-10 logarithm of x | `x = 1000`<br>`math.log10(x)` | `3.0` |
| `log2(x)` | Returns the base-2 logarithm of x | `x = 8`<br>`math.log2(x)` | `3.0` |
| `pow(x, y)` | Returns the value of x raised to the power y (xʸ) | `x = 2, y = 3`<br>`pow(x, y)` | `8` |


## How to Use

Make sure to import the `math` module before using these functions (except `pow()`, which is built-in):

python
import math

# Example Usage:

x = 2
print(math.exp(x))        # Output: 7.38905609893065

x = math.e
print(math.log(x))        # Output: 1.0

x = 8
b = 2
print(math.log(x, b))     # Output: 3.0

x = 1000
print(math.log10(x))      # Output: 3.0

x = 8
print(math.log2(x))       # Output: 3.0

# pow() does not require math module
x = 2
y = 3
print(pow(x, y))          # Output: 8











## Imp Programe
```
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
    
```



# Rounding Functions in Python (`math` Module)

Python’s `math` module provides functions like `floor()`, `ceil()`, and `trunc()` to **round** floating-point numbers in different ways.

---

## Functions Table

| Function | Description | Example Usage | Output |
|:--------:|:------------:|:-------------:|:------:|
| `floor(x)` | Returns the largest integer less than or equal to x | `floor(1.4)` → `1`<br>`floor(2.6)` → `2`<br>`floor(-1.4)` → `-2`<br>`floor(-2.6)` → `-3` |
| `ceil(x)` | Returns the smallest integer greater than or equal to x | `ceil(1.4)` → `2`<br>`ceil(2.6)` → `3`<br>`ceil(-1.4)` → `-1`<br>`ceil(-2.6)` → `-2` |
| `trunc(x)` | Truncates (removes) the decimal part of x, keeping only the integer part | `trunc(1.4)` → `1`<br>`trunc(2.6)` → `2`<br>`trunc(-1.4)` → `-1`<br>`trunc(-2.6)` → `-2` |

---

## Code Example

```
python
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))   # Output: 1 2
print(floor(-x), floor(-y)) # Output: -2 -3
print(ceil(x), ceil(y))     # Output: 2 3
print(ceil(-x), ceil(-y))   # Output: -1 -2
print(trunc(x), trunc(y))   # Output: 1 2
print(trunc(-x), trunc(-y)) # Output: -1 -2
```


## Random module
```
1)
from random import random

for i in range(5):
    print(random())

// output
0.2973757839075416
0.25461655339320555
0.358163969849571
0.7937167851915783
0.5019736325451979
```

# 🎯 Random Numbers in Python (`random` Module)

# 📚 Conclusion

| Feature | Without `seed()` | With `seed(0)` |
|:-------:|:----------------:|:--------------:|
| Random Numbers | Different every run | Same every run |
| Use Case | Normal randomness | Testing, debugging |

## IMG Programe of random
```
1)// without seed
from random import random

for i in range(5):
    print(random())

print('\n\n')    
    
for i in range(5):
    print(random())
    
    
// output
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335


0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335




2)
from random import random, seed

seed(0)

for i in range(4):
    print(random())
print('\n\n')

seed(0)  # Resetting the seed for the second loop
for i in range(4):
    print(random())

//output
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335



0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335


4)
from random import randrange, randint

print('randrange(1) : ',randrange(1))
print('randrange(0, 1) : ',randrange(0, 1))
print('randrange(0, 1, 1): ',randrange(0, 1, 1))
print(randint(0, 1))
print()
print('randrange(2) : ',randrange(2))
print('randrange(0, 2) : ',randrange(0, 2))
print('randrange(0, 2, 1): ',randrange(0, 2, 1))
print(randint(0, 2))
print()

// output
randrange(1) :  0
randrange(0, 1) :  0
randrange(0, 1, 1):  0
1

randrange(2) :  0
randrange(0, 2) :  1
randrange(0, 2, 1):  0
0
```
