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
