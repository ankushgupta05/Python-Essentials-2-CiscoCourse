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

