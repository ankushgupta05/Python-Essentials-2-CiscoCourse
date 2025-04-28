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









