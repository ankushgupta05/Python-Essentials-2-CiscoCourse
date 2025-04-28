# img prog.
```
1)

class Stack:
    def __init__(self):
        self.__stack_list = []   # stack_list private variable because __ have apply before starting of the variable


stack_object = Stack()
print(len(stack_object.__stack_list))


// o/p
genrate error because stack_list is a private variable it access only inside of the class




2)
class Stack:
    def __init__(self):
        self.__stack_list = []     # stack_list private variable because __ have apply before starting of the variable


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

// o/p
1
2
3





3) Stack is a class and  AddingStack is a sub-class

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None


class AddingStack(Stack):
    def __init__(self):
        super().__init__()  # Stack ka __init__ bhi chalayenge
        self.total = 0      # apna extra feature: sum track karna

    def push(self, item):
        super().push(item)   # Stack ka push bhi karo   # ye Stack class ke push() ko call kar raha hai
        self.total += item   # aur sum me add karo

    def pop(self):
        item = super().pop()  # Stack ka pop bhi karo  # ye Stack class ke pop() ko call kar raha hai
        if item is not None:
            self.total -= item   # aur sum me se minus karo
        return item


stack = AddingStack()

stack.push(10)
stack.push(20)
print("Sum:", stack.total)  # 30

stack.pop()
print("Sum:", stack.total)  # 10

stack.pop()
print("Sum:", stack.total)  # 0



// o/p
Sum: 30
Sum: 10
Sum: 0

```



## OOPS
```
1)
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val  # ✅ Instance variable 'first' is created here (belongs to object)

    def set_second(self, val):
        self.second = val  # ✅ Instance variable 'second' is created here (only if method called)


# Create objects
example_object_1 = ExampleClass()        
# 👆 Only 'first' is created = 1

example_object_2 = ExampleClass(2)        
example_object_2.set_second(3)  
# 👆 'first' = 2 from constructor
# 👆 'second' = 3 from set_second() method

example_object_3 = ExampleClass(4)
example_object_3.third = 5  
# 👆 'first' = 4 from constructor
# 👆 'third' = 5 added manually (outside the class)

# Print their __dict__
print(example_object_1.__dict__)  # {'first': 1}
print(example_object_2.__dict__)  # {'first': 2, 'second': 3}
print(example_object_3.__dict__)  # {'first': 4, 'third': 5}


//o/p
{'first': 1}
{'first': 2, 'second': 3}
{'first': 4, 'third': 5}


//NOTE :-
Object | Properties inside __dict__
example_object_1 | 'first': 1
example_object_2 | 'first': 2, 'second': 3
example_object_3 | 'first': 4, 'third': 5

Point | Explanation
1 | In Python, every object automatically gets a hidden __dict__ attribute.
2 | __dict__ is a dictionary that stores all variables and their values inside the object.
3 | You can create object variables in the constructor (__init__) or by using methods.
4 | You can even add new properties outside the class anytime (Python allows it).
5 | Using print(object.__dict__), you can see all current variables of the object.

```


## Class variable
```
1)
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val            # first is a private variable
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

//o/p
{'_ExampleClass__first': 1} 3
{'_ExampleClass__first': 2} 3
{'_ExampleClass__first': 4} 3





2)
class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

//o/p
{'_ExampleClass__first': 1} 3
{'_ExampleClass__first': 2} 3
{'_ExampleClass__first': 4} 3




3)
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

//o/p
1
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'




4)
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass

//o/p
1
```


## imp hasattr()
```
1)
class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

//o/p
True
False

//NOTE :-
hasattr(object, name)

Ye function check karta hai:
➔ kya object ke andar koi variable, attribute, ya method exist karta hai ya nahi.
Return karta hai:
True ➔ Agar attribute/method maujood hai
False ➔ Agar attribute/method nahi hai



2)
class ExampleClass:
    a = 1  # → Class Variable

    def __init__(self):
        self.b = 2  # → Instance Variable

example_object = ExampleClass()

print(hasattr(example_object, 'b'))  # (1)
print(hasattr(example_object, 'a'))  # (2)
print(hasattr(ExampleClass, 'b'))    # (3)
print(hasattr(ExampleClass, 'a'))    # (4)

//o/p
True
True
False
True


//NOTE :-
Line | Explanation | Output
(1) hasattr(example_object, 'b') | example_object ke andar b hai (instance variable) | ✅ True
(2) hasattr(example_object, 'a') | example_object class se inherit karke a ko bhi access karta hai | ✅ True
(3) hasattr(ExampleClass, 'b') | ExampleClass khud b ko define nahi karta (b sirf object me hai) | ❌ False
(4) hasattr(ExampleClass, 'a') | ExampleClass ke andar directly a define hai | ✅ True
```



## summar 3.3
```
1)
class Sample:
    gamma = 0 # Class variable.
    def __init__(self):

        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)

//o/p
{'alpha': 1, '_Sample__delta': 3, 'beta': 2}
```



## quize 3.3
# Python Class Variables vs Instance Variables

| Question | Code | Answer | Explanation |
|:---------|:-----|:-------|:------------|
| 1. Which of the Python class properties are instance variables and which are class variables? Which of them are private? | ```python class Python: population = 1 victims = 0 def __init__(self): self.length_ft = 3 self.__venomous = False ``` | `population`, `victims` = class variables; `length_ft`, `__venomous` = instance variables; `__venomous` is private | Class variables are shared across all objects, instance variables are unique for each object. `__venomous` uses name mangling (_Python__venomous) to make it private. |
| 2. How will you negate the private __venomous attribute of version_2? | ```python version_2 = Python() version_2._Python__venomous = not version_2._Python__venomous ``` | Done using name mangling: `_Python__venomous` | Even private variables can be accessed using name-mangled names in Python. |
| 3. How to check if the object has a property named 'constrictor'? | ```python hasattr(version_2, 'constrictor') ``` | Use `hasattr` function | `hasattr(object, 'attribute')` checks if an object has a specific attribute and returns `True` or `False`. |




## 3.4
```
1)
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

//o/p
2 3
```


