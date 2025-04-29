# 1.10 SECTION QUIZ

| Question | Answer | Explanation |
|----------|--------|-------------|
| **Question 1:** If we assume that pythons, vipers, and cobras are subclasses of the same superclass, what would you call it? | Snake, reptile, vertebrate, animal – all these answers are acceptable. | Any of these can be an appropriate name for the superclass as they all represent categories that could include pythons, vipers, and cobras. |
| **Question 2:** Try to name a few python class subclasses. | [Your Answer] | [Explanation of the subclasses you would name.] |
| **Question 3:** Can you name one of your classes just "class"? | No, you can't – class is a keyword! | "class" is a reserved keyword in Python, so it cannot be used as a class name. |






## __str__  and __repr__ concept
```
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f"{self.name} in {self.galaxy} (for humans)"

    def __repr__(self):
        return f"Star(name='{self.name}', galaxy='{self.galaxy}')"


# Creating object
sun = Star("Sun", "Milky Way")

# __str__ is used here:
print("Using print():", sun)

# __repr__ is used when inspected or logged (like in lists, debugger etc.)
print("Using repr():", repr(sun))

# If you print a list containing object:
print("Object in list:", [sun])


//o/p
Using print(): Sun in Milky Way (for humans)
Using repr(): Star(name='Sun', galaxy='Milky Way')
Object in list: [Star(name='Sun', galaxy='Milky Way')]

```



## subClass and Super Class
```
1)
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

//o/p
The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.



2)
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

//o/p
True	False	False	
True	True	False	
True	True	True

//NOTE :-
There is one important observation to make: each class is considered to be a subclass of itself.


3)
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

//o/p
True	False	False	
True	True	False	
True	True	True


4)
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)

//o/p
False
False
True
1 2 1
True False



```


## imp prog.
```

1)
# Base class
class Super:
    def __init__(self, name):
        self.name = name  # name attribute set kar raha hai

    def __str__(self):
        return "My name is " + self.name + "."  # print(obj) pe yeh call hoga


# Derived class (child class)
class Sub(Super):
    def __init__(self, name):
        # 👇 Base class ka constructor ko explicitly call kar rahe hain
        Super.__init__(self, name)  # Python 2 style, kam flexible

# Object banaya
obj = Sub("Andy")

# print(obj) => __str__ method call karega
print(obj)

// o/p
# Output: My name is Andy.





2)
# Base class
class Super:
    def __init__(self, name):
        self.name = name  # name attribute set kar raha hai

    def __str__(self):
        return "My name is " + self.name + "."  # print(obj) pe yeh call hoga


# Derived class (child class)
class Sub(Super):
    def __init__(self, name):
        # 👇 Parent constructor ko super() se call kar rahe hain
        super().__init__(name)  # ✅ Python 3 style, dynamic and safer

# Object banaya
obj = Sub("Andy")

# print(obj) => __str__ method call karega
print(obj)

//o/p
# Output: My name is Andy





// Note for quesion 1 and 2 :
# Dono version me output same hai, lekin:
# Super.__init__(...) = explicit, hard-coded base class
# super().__init__(...) = dynamic, flexible, recommended in Python 3+
# Multiple inheritance me super() zyada useful hota hai.






3)
# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)

//o/p
2
1



4)
# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

//o/p
12
11



```
## Multy Inheritence
```
1)
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

//o/p
10 11
20 21

```


## overriding
```
1)
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

//o/p
200 201




2)
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):   # first priority to the 'Left' and second priority to 'Right'  
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

//o/p
L LL RR Left

//NOTE :-
Python MRO (Method Resolution Order):
Python looks for attributes and methods in the following order: Sub → Left → Right → object

so that
obj.var       # Found in Left.var = "L" ✅ (because Left comes first in MRO)
obj.var_left  # Found in Left.var_left = "LL" ✅
obj.var_right # Not in Left, found in Right.var_right = "RR" ✅
obj.fun()     # Left.fun() is chosen because Left comes before Right in MRO ✅

```


## How to build a hierarchy of classes
```
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
    

//o/p
do_it from One
do_it from Two
```



##  What is Method Resolution Order (MRO) and why is it that not all inheritances make sense?

```
1)
# ✔️ Yeh perfectly valid hai. Inheritance chain: Bottom → Middle → Top

class Top:
    def m_top(self):
        print("top")

class Middle(Top):  # Middle inherits from Top
    def m_middle(self):
        print("middle")

class Bottom(Middle):  # Bottom inherits from Middle
    def m_bottom(self):
        print("bottom")

# Object of Bottom can access all 3 methods
object = Bottom()
object.m_bottom()   # Output: bottom
object.m_middle()   # Output: middle
object.m_top()      # Output: top


//o/p
bottom
middle
top





2)
# ✔️ Yeh bhi valid hai. Although Middle already inherits Top,
#      phir bhi humne Bottom me Top ko dobara likh diya hai.
# Python internally duplicate se bachata hai using MRO.

class Top:
    def m_top(self):
        print("top")

class Middle(Top):  # Middle inherits Top
    def m_middle(self):
        print("middle")

class Bottom(Middle, Top):  # Redundant: Middle already has Top
    def m_bottom(self):
        print("bottom")

# Object of Bottom can still access all methods
object = Bottom()
object.m_bottom()   # Output: bottom
object.m_middle()   # Output: middle
object.m_top()      # Output: top

//o/p
bottom
middle
top





3)
# ❌ Yeh chalega nahi.
# Problem: Middle already inherits Top, lekin humne Bottom me Top ko pehle likh diya.
# Python ko confusion hota hai Top class ke order ko resolve karne me.

class Top:
    def m_top(self):
        print("top")

class Middle(Top):  # Middle inherits Top
    def m_middle(self):
        print("middle")

# ❌ ERROR: Inconsistent Method Resolution Order (MRO)
class Bottom(Top, Middle):  # Wrong order: Top first, Middle later (but Middle also inherits Top)
    def m_bottom(self):
        print("bottom")

# This will not run
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

//o/p
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Top, Middle




//NOTE for 1 and 2 and 3
| Case | Code Snippet                  | Runs? | Reason                                                                 |
|------|-------------------------------|-------|------------------------------------------------------------------------|
| 1    | `class Bottom(Middle)`        | ✅ Yes | Simple single inheritance; clear MRO                                   |
| 2    | `class Bottom(Middle, Top)`   | ✅ Yes | Redundant but Python resolves with MRO                                 |
| 3    | `class Bottom(Top, Middle)`   | ❌ No  | MRO conflict due to `Top` appearing before and inside `Middle` as well |
```


## MRO RULE 
| Rule                              | Explanation                                     |
|-----------------------------------|-------------------------------------------------|
| C3 Linearization                  | Python 3 ka MRO algorithm                       |
| Left-to-right lookup              | `class A(B, C)` → B checked before C            |
| No duplication in MRO             | Har class ek hi baar MRO me aata hai            |
| Parents appear **after** children | Parent class child ke baad hi aayega            |



## quize 3.6
```
class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")



1)
Question 1: The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to the __victims property.

print(rocky)
print(luna)

//o/p
Collie says: Woof! Don't run away, Little Lamb!
Dobermann says: Woof! Stay where you are, Mister Intruder!





2)
Question 2: What is the expected output of the following piece of code?

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
 
//o/p
True False
False True





3)
Question 3: What is the expected output of the following piece of code?

print(luna is luna, rocky is luna)
print(rocky.kennel)
 
//o/p
True False
2



4)
Question 4: Define a SheepDog's subclass named LowlandDog, and equip it with an __str__() method overriding an inherited method of the same name. The new dog's __str__() method should return the string "Woof! I don't like mountains!".

//o/p
class LowlandDog(SheepDog):
	def __str__(self):
		return Dog.__str__(self) + " I don't like mountains!"
		
```




## 3.6 Quize
```
1)
import math
 
    try:
        print(math.sqrt(9))
    except ValueError:
        print("inf")
    else:
        print("fine")
 //o/p
3.0
fine


2)
Question 2: What is the expected output of the following code?

import math
 
    try:
        print(math.sqrt(-9))
    except ValueError:
        print("inf")
    else:
        print("fine")
    finally:
        print("the end")

//o/p
inf
the end




3)
Question 3: What is the expected output of the following code?

import math
 
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
 
try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')

//o/p
Enemy warning! Red alert! High readiness!

```


# Final Quize
## Python OOP & Exception Handling Quiz

### Question 1
**A data structure described as LIFO is actually a:**
- ✅ Stack

---

### Question 2
**If the class’s constructor is declared as below, which one of the assignments is valid?**
```python
class Class:
    def __init__(self):
        pass
```
- ✅ object = Class()

---

### Question 3
**Superclass named A and subclass B, which invocation should be used in subclass?**
```python
class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = 2
```
- ✅ A.__init__(self)

---

### Question 4
**What will be the effect of running the following code?**
```python
class A:
    def __init__(self,v):
        self.__a = v + 1

a = A(0)
print(a.__a)
```
- ✅ The code will raise an AttributeError exception

---

### Question 5
```python
class A:
    def __init__(self,v = 1):
        self.v = v

    def set(self,v):
        self.v = v
        return v

a = A()
print(a.set(a.v + 1))
```
- ✅ 2

---

### Question 6
```python
class A:
    X = 0
    def __init__(self,v = 0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)
print(c.X)
```
- ✅ 3

---

### Question 7
```python
class A:
    A = 1

print(hasattr(A,'A'))
```
- ✅ True

---

### Question 8
```python
class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a,'A'))
```
- ✅ it will raise an exception

---

### Question 9
```python
class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'

class C(B):
    pass

o = C()
print(o)
```
- ✅ it will print b

---

### Question 10
```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(C,A))
```
- ✅ True

---

### Question 11
```python
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()
```
- ✅ it will print b

---

### Question 12
```python
class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B):
    pass

o = C()
print(o)
```
- ✅ it will print a

---

### Question 13
```python
class A:
    v = 2

class B(A):
    v = 1

class C(B):
    pass

o = C()
print(o.v)
```
- ✅ it will print 1

---

### Question 14
```python
def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')

f(1)
f(0)
```
- ✅ bcac

---

### Question 15
```python
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))
```
- ✅ 3

---

### Question 16
```python
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
```
- ✅ ex

---

### Question 17
```python
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x,end='')
```
- ✅ abc





