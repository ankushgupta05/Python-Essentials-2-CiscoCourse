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




5)
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

// output
7,8,2,7,5,2,7,9,6,9,
```


## imp programe of choice and sample
```
1)
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


// output
7
[10, 7, 5, 4, 9]
[10, 4, 2, 3, 9, 6, 5, 1, 7, 8]
```



# Platform Module in Python (Simple Explanation)

Python's `platform` module is used to:
- Find details about your hardware (machine/processor).
- Identify the operating system (OS) you are using.
- Get information about your Python version.

---

## Important Functions and Their Usage

| Function | Purpose | Example | Example Output |
|:--------|:--------|:--------|:---------------|
| `platform()` | Full info about OS + Hardware | `platform()` | Windows-10-10.0.22631-SP0 |
| `platform(aliased=True)` | Alternative OS name | `platform(1)` | Windows-10-10.0.22631-SP0 |
| `platform(terse=True)` | Short version info | `platform(0, 1)` | Windows-10 |
| `machine()` | Hardware/Processor type | `machine()` | x86_64 |
| `processor()` | Real Processor Name | `processor()` | Intel64 Family 6 Model 142 |
| `system()` | OS Name | `system()` | Windows |
| `version()` | OS Version | `version()` | 10.0.22631 |
| `python_implementation()` | Python implementation used | `python_implementation()` | CPython |
| `python_version_tuple()` | Python version split into parts | `python_version_tuple()` | ('3', '12', '2') |

---

## Code Examples with Output

### 1. platform()
```python
from platform import platform
print(platform())
```
**Output Example:**
```
Windows-10-10.0.22631-SP0
```

---

### 2. machine()
```python
from platform import machine
print(machine())
```
**Output Example:**
```
x86_64
```

---

### 3. processor()
```python
from platform import processor
print(processor())
```
**Output Example:**
```
Intel64 Family 6 Model 142 Stepping 10 GenuineIntel
```

---

### 4. system()
```python
from platform import system
print(system())
```
**Output Example:**
```
Windows
```

---

### 5. version()
```python
from platform import version
print(version())
```
**Output Example:**
```
10.0.22631
```

---

### 6. python_implementation()
```python
from platform import python_implementation
print(python_implementation())
```
**Output Example:**
```
CPython
```

---

### 7. python_version_tuple()
```python
from platform import python_version_tuple
print(python_version_tuple())
```
**Output Example:**
```
('3', '12', '2')
```

---

## Final Easy Summary

| Function | Gives Information About |
|:---------|:-------------------------|
| `platform()` | Full environment summary |
| `machine()` | Hardware CPU type |
| `processor()` | Real processor name |
| `system()` | Operating System Name |
| `version()` | Operating System Version |
| `python_implementation()` | Type of Python used (e.g., CPython) |
| `python_version_tuple()` | Python version broken into parts |

---

## Notes:
- `platform()` combines many details into a single string.
- `machine()` and `processor()` focus on hardware details.
- `system()` and `version()` describe the operating system.
- `python_implementation()` and `python_version_tuple()` focus on Python interpreter info.

---

Feel free to run these codes on your machine to see different outputs depending on your OS and hardware!




## module 1.2 quize
# Python - Questions 1 to 4

This file contains the **Questions 1 to 4** with corresponding **code**, **answers**, and **explanations** in table format.

---

## Questions, Code, Answers, and Explanations

| Question | Code | Answer | Explanation |
|:--------:|:----:|:------:|:-----------:|
| **1** | ```python
import math
result = math.e == math.exp(1)
print(result)
``` | `True` | `math.e` is the mathematical constant **e (~2.71828)** and `math.exp(1)` calculates **e^1**, which is also **e**. So, both are equal, and `result` becomes `True`. |
| **2** | _No code required._ | _... the pseudo-random values emitted from the random module will be exactly the same._ | Setting a random number generator's **seed** to the same value ensures that the sequence of random numbers generated will always be **identical** every time the program is run. |
| **3** | ```python
from platform import processor
print(processor())
``` | `processor()` | To determine the **CPU name**, use the `processor()` function from the `platform` module. It returns a string showing the real processor name (e.g., Intel, ARM, etc.). |
| **4** | ```python
import platform
print(len(platform.python_version_tuple()))
``` | `3` | `platform.python_version_tuple()` returns a tuple of 3 elements: **(major, minor, patch)** parts of the Python version. So, `len()` of this tuple is **3**. |

---

### Notes
- Make sure the `platform` and `math` modules are correctly imported.
- Random seeds are especially useful for reproducibility in testing and simulations.

---



## Packages
```
1)
if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")

// output
I prefer to be a module.
```
