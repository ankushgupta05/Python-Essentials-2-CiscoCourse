## imp quetion
```
1)
def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)


//o/p
0
1
2
3
4



2)
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

//o/p
1
2
4
8
16
32
64
128

```

##  list comprehensions
```
1)
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

//o/p
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

```

## lambda function
```
print([x for x in range(-2, 3)])
[-2, -1, 0, 1, 2]



1)
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

//o/p
4 4
1 1
0 0
1 1
4 4



2)
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
    
//o/p
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2


```

## Lambdas and the map() function
```
1)
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    
print(map(lambda x: x * x, list_2))

//o/p
[1, 2, 4, 8, 16]
1 4 16 64 256 
<map object at 0x7fbe848f5b90>


2)
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    
print(map(lambda x: x * x, list_2))
print()
print(list(map(lambda x: x * x, list_2)))

//o/p
[1, 2, 4, 8, 16]
1 4 16 64 256 
<map object at 0x7feec216b9d0>

[1, 4, 16, 64, 256]

```


## Lambdas and the filter() function
```
1)
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

//o/p
[9, -4, 6, 0, 7]
[6]


2)
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
print()
print(filter(lambda x: x > 0 and x % 2 == 0, data))

//o/p
[-9, 5, -5, 10, -1]
[10]

<filter object at 0x7fc1b1783ed0>




3)
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

//o/p
1



4)
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
    
//o/p
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64

```

## 4.1.11 SECTION QUIZ
```

1)
Question 1: What is the expected output of the following code?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Yes, we know that y is not always considered a vowel.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
 
//o/p
a e i o u y
```


## Quize
```
Question 1: What is the expected output of the following code?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Yes, we know that y is not always considered a vowel.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
 
//o/p
a e i o u y
Question 2: Write a lambda function, setting the least significant bit of its integer argument, and apply it to the map() function to produce the string 1 3 3 5 on the console.

any_list = [1, 2, 3, 4]
even_list = # Complete the line here.
print(even_list)
 
//o/p
list(map(lambda n: n | 1, any_list))
    

Question 3: What is the expected output of the following code?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))
 
//o/p
And*Now*for*Something*Completely*Different

```




## Module 4.4 is entire remaining



## Module 4 Test - Questions and Answers

### Question 1
**Q:** What keyword would you use to define an anonymous function?
**A:** `lambda`

---

### Question 2
**Q:** Select the true statements. (Select two answers)
**A:**
- The lambda function can evaluate only one expression
- The lambda function can accept any number of arguments

---

### Question 3
**Q:** What code outputs (1, 4, 27)?
**A:** `foo = tuple(map(lambda x: x**x, my_list))`

---

### Question 4
**Q:** What code outputs [2, 3, 4, 5, 6]?
**A:** `foo = list(filter(lambda x: x-0 and x-1, my_tuple))`

---

### Question 5
**Q:** What is printed by the generator I()?
**A:** `ace`

---

### Question 6
**Q:** What does `fun(2)` yield?
**A:** `++`

---

### Question 7
**Q:** What is printed by the closures `r()` and `s()`?
**A:** `***`

---

### Question 8
**Q:** Which open modes allow read operations? (Select two)
**A:**
- `r`
- `r+`

---

### Question 9
**Q:** What does `errno.EEXIST` represent?
**A:** File exists

---

### Question 10
**Q:** What is printed by `bytearray(3)`?
**A:** `bytearray(b'\x00\x00\x00')`

---

### Question 11
**Q:** What is printed after navigating back from `thumbnails`?
**A:** It prints the path to the pictures directory

---

### Question 12
**Q:** What is printed after creating 'small', 'medium', 'large' directories?
**A:** `['large', 'small', 'medium']`

---

### Question 13
**Q:** What is the result of `date_1 - date_2`?
**A:** `345 days, 0:00:00`

---

### Question 14
**Q:** What is the result of the strftime call?
**A:** `19/November/27 11:27:22`

---

### Question 15
**Q:** Which program produces: Mo Tu We Th Fr Sa Su?
**A:** A

---

### Question 16
**Q:** What is the result of `c.iterweekdays()`?
**A:** `0 1 2 3 4 5 6`


