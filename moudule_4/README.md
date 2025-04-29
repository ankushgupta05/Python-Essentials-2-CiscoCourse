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



5)

```


