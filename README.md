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





3)
















```
