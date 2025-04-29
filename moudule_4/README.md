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




3)

```



