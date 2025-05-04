# 2.1.3 Code points and code pages

| **Term** | **Explanation** |
|----------|-----------------|
| **Code Point** | A number representing a character. For example, 32 is a space in ASCII encoding. |
| **Code Page** | A standard for using the upper 128 code points to store specific national characters. |
| **Unicode** | A character encoding standard that assigns unique characters to over a million code points. |
| **UCS-4** | A Unicode standard using 32 bits to store each character. It is memory-inefficient but covers all Unicode characters. |
| **UTF-8** | A more efficient Unicode encoding system that uses variable bits (8, 16, or 24 bits) based on the character. It's the most common encoding in modern applications. |
| **BOM (Byte Order Mark)** | A special combination of bits announcing the encoding of a file's content, such as UCS-4 or UTF-8. |

### Python 3 and I18N
Python 3 fully supports Unicode and UTF-8, meaning it is completely internationalized (I18Ned). You can use Unicode characters in variable names, input, and output.


# 2.1.5 SECTION QUIZ

| **Question** | **Answer** | **Example** |
|--------------|------------|-------------|
| **What is BOM?** | BOM (Byte Order Mark) is a special combination of bits announcing the encoding used by a file's content (e.g., UCS-4 or UTF-8). | Example: In UTF-8 encoded files, the BOM might be `EF BB BF` at the beginning of the file. |
| **Is Python 3 I18Ned?** | Yes, Python 3 is completely internationalized. It fully supports Unicode and UTF-8 encoding for input, output, and code. | Example: You can use characters like `汉` (Chinese) or `日本` (Japanese) in Python 3 variable names. |








### imp pro.
```
1)
# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))


//output
2
0
3



2)
multiline = '''Line #1
Line #2'''

print(len(multiline))

//output
15

NOTE :-
above one extra space for '\n'

3)
multiline = """Line #1
Line #2"""

print(len(multiline))

// output
15



3)
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

//output
97
32



4)
print(chr(97))
print(chr(945))
//output
a
α


5)
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
//output
bd
efg
abd
e
e
adf
beg


// Note :-
The string is "abdefg", so starting from the first character ('a' at index 0), we select every second character:

'a' (index 0)

'd' (index 2)

'f' (index 4)

The output of alpha[::2] will be:
'adf'
```



## string in python is immutable
| Concept                         | Explanation                                                                 | Example Code                                                             | Output Example           |
|----------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------|
| Immutability of Strings         | Python strings are immutable, meaning their values cannot be changed once created. | `alphabet = "abcdefghijklmnopqrstuvwxyz"`<br>`del alphabet[0]`             | Error: `TypeError`       |
| No Append Method                | Strings do not have an `append()` method to add characters to them.           | `alphabet = "abcdefghijklmnopqrstuvwxyz"`<br>`alphabet.append("A")`        | Error: `AttributeError`  |
| No Insert Method                | Strings do not have an `insert()` method to insert characters at specific positions. | `alphabet = "abcdefghijklmnopqrstuvwxyz"`<br>`alphabet.insert(0, "A")`   | Error: `AttributeError`  |
| Modifying Strings               | Since strings are immutable, you need to create a new string if modifications are needed. | `alphabet = "abcdefghijklmnopqrstuvwxyz"`<br>`alphabet = "A" + alphabet`  | `Aabcdefghijklmnopqrstuvwxyz` |










### img prog.
```
1)
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))
print()
print(ord('a'))
print(ord('A'))
print(ord(' '))


//output
A
[ ]
0

97
65
32



2)
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))


//output
z
[y]
2


3)
# Demonstrating the index() method:
print("aAbbByYzZabA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

//output
2
7
1

4)
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

//
2
0

5)
# Demonstrating the list() function:
print(list("abcabc"))

//output
['a', 'b', 'c', 'a', 'b', 'c']


6)
print(len("\n\n"))
// output
2
```


## string method 
```
1)
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

// output
Alpha
Alpha
 alpha
123
Αβγδ

2)
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
//o/p
[  alpha   ]


3)
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
//o/p
[Beta]  # argument 2 pass kiya hai but character string jada hai isliye only string output aaya hai
[Beta]
[ Beta ]   # total 6 space inside []

4)
print('[' + 'gamma'.center(20, '*') + ']')
//o/p
[*******gamma********]


5)
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
// o/p
yes

6)
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
//o/p
True
False
False
True

7)
# Demonstrating the find() method:
print("abcdEta".find("ta"))
print("abcdEta".find("mma"))
print("abnakuhs".index('a'))
print("abnakuhs".index('ak'))
print("abnakuhs".index('Z'))

//o/p
5
-1
0
3
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    print("abnakuhs".index('Z'))
ValueError: substring not found


// NOTE :-
find() :- It not genrate error if value not exits in the given strings
index() :- It genrate error if value not exits in the given strings




8)
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

//o/p
15
80
198
221
238



9)
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

// o/p
1
-1


// Note :
.find(sub, start, end)
```


# Demonstrating the `isalnum()` method and isalnum allows string and number

| Expression | Result | Explanation |
|:-----------|:-------|:------------|
| `'lambda30'.isalnum()` | `True`  | Contains only letters and digits. |
| `'lambda'.isalnum()`   | `True`  | Contains only letters. |
| `'30'.isalnum()`       | `True`  | Contains only digits. |
| `'@'.isalnum()`        | `False` | `@` is a special character, not alphanumeric. |
| `'lambda_30'.isalnum()`| `False` | Underscore `_` is not considered alphanumeric. |
| `''.isalnum()`         | `False` | Empty string returns `False`. |

---


## img programe
```
t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())
//o/p
False
False
True
```

## isalpha() method is more specialized – it's interested in letters only.
```
1)
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

//o/p
True
False

2)

```
## isdigit() method looks at digits only – anything else produces False as the result.
```
1)
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

True
False
```

### img keyword
```
1)

# Example: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

//o/p
False
True

2)
# Example: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
//o/p
True
True
False


3)
# Example: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
//o/p
False
False
True


4)
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
//o/p
omicron,pi,rho


5)
# Demonstrating the lower() method:
print("SiGmA=60".lower())
//o/p
sigma=60


6)
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

//o/p
[tau ]

// Note :-
The parameterless version of the lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.



7)
print("www.cisco.com".lstrip("w."))
//o/p
cisco.com


8)
print("pythoninstitute.org".lstrip(".org"))
//o/p
pythoninstitute.org

// Note :-
Your string is: "pythoninstitute.org"
First character: p → not in .org, so stop stripping immediately.

Nothing removed | Because first character p is not ., o, r, or g
.lstrip() only affects leftmost side | Doesn't find ., o, r, g immediately, so it keeps the string unchanged



9)
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
//o/p
www.pythoninstitute.org
Thare are it!
Apple


10)
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
print("This is is it!".replace("is", "are", 2))
print("This is is it!".replace("is", "are", 3))

//o/p
Thare is it!
Thare are it!
Thare are is it!
Thare are are it!

11)
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

//
8
-1
4

//Note :-
The one-, two-, and three-parameter versions of the rfind() method do nearly the same things as their counterparts (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning (hence the prefix r, for right).

Code | Explanation | Output
.rfind("ta") | Full string, right se search karega → last "ta" at index 8 | 8
.rfind("ta", 9) | Index 9 ke baad "ta" nahi milta | -1
.rfind("ta", 3, 9) | Index 3 to 8 ke beech "ta" milta hai at index 4 | 4




12)
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

//o/p
[ upsilon]
cis

//NOTE :--
Code | Explanation | Output
" upsilon ".rstrip() | Right ka space hata diya | [ upsilon]
"cisco.com".rstrip(".com") | Right se "m", "o", "c", "." hata diye | cisc


13)
# Demonstrating the split() method:
print("phi       chi\npsi".split())
//o/p
['phi', 'chi', 'psi']


14)
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

//o/p
False
True




15)
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

//o/p
[aleph]




16)
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()
//o/p
i KNOW THAT i KNOW NOTHING.



17)
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
print("I know that I know nothing. Part 1.".capitalize())

print()
//o/p
I Know That I Know Nothing. Part 1.
I know that i know nothing. part 1.



18)
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
//o/p
I KNOW THAT I KNOW NOTHING. PART 2.


```

# String Methods Summary

| **Method** | **Description** |
|:-----------|:----------------|
| `capitalize()` | Changes the first character to uppercase. |
| `center(width)` | Centers the string in a field of given width. |
| `count(sub)` | Counts occurrences of a substring. |
| `join(iterable)` | Joins elements of a list/tuple into a single string. |
| `lower()` | Converts all letters to lowercase. |
| `lstrip()` | Removes whitespace from the beginning. |
| `replace(old, new)` | Replaces occurrences of a substring. |
| `rfind(sub)` | Finds the last occurrence of a substring. |
| `rstrip()` | Removes whitespace from the end. |
| `split(sep)` | Splits the string into a list using a separator. |
| `strip()` | Removes whitespace from both ends. |
| `swapcase()` | Swaps case of each letter. |
| `title()` | Capitalizes the first letter of each word. |
| `upper()` | Converts all letters to uppercase. |

# String Content Checking Methods

| **Method** | **Description** |
|:-----------|:----------------|
| `endswith(sub)` | Checks if the string ends with a given substring. |
| `isalnum()` | Checks if all characters are alphanumeric. |
| `isalpha()` | Checks if all characters are letters. |
| `islower()` | Checks if all letters are lowercase. |
| `isspace()` | Checks if the string contains only whitespace. |
| `isupper()` | Checks if all letters are uppercase. |
| `startswith(sub)` | Checks if the string starts with a given substring. |






# Python String Methods Quiz

## Quiz Questions and Answers

| Question No. | Question | Code | Expected Output | Explanation |
|--------------|----------|------|-----------------|-------------|
| 1            | What is the expected output of the following code? | ```python for ch in "abc123XYX": if ch.isupper(): print(ch.lower(), end='') elif ch.islower(): print(ch.upper(), end='') else: print(ch, end='') ``` | `ABC123xyx` | The code checks each character. If it's uppercase, it prints the lowercase of the character; if it's lowercase, it prints the uppercase of the character; else, it prints the character as is. |
| 2            | What is the expected output of the following code? | ```python s1 = 'Where are the snows of yesteryear?' s2 = s1.split() print(s2[-2]) ``` | `of` | The `split()` method breaks the string into a list of words. `s2[-2]` fetches the second-to-last word from the list, which is `'of'`. |
| 3            | What is the expected output of the following code? | ```python the_list = ['Where', 'are', 'the', 'snows?'] s = '*'.join(the_list) print(s) ``` | `Where*are*the*snows?` | The `join()` method joins all items in the list with the `'*'` separator, resulting in `'Where*are*the*snows?'`. |
| 4            | What is the expected output of the following code? | ```python s = 'It is either easy or impossible' s = s.replace('easy', 'hard').replace('im', '') print(s) ``` | `It is either hard or possible` | The `replace()` method first replaces `'easy'` with `'hard'`, then it removes `'im'`, resulting in `'It is either hard or possible'`. |









## 2.4 module
### String Comparison in Python

| **Code**                        | **Explanation**                                                                                                                                                       | **Output** |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `'alpha' == 'alpha'`             | Both strings are identical.                                                                                                                                            | `True`     |
| `'alpha' != 'Alpha'`             | The strings are compared case-sensitively, so `'alpha'` is different from `'Alpha'` because of the first letter's case.                                               | `True`     |
| `'alpha' < 'alphabet'`           | Lexicographically, `'alpha'` comes before `'alphabet'` as it is a prefix of `'alphabet'`.                                                                            | `True`     |
| `print('10' == '010')`           | The strings `'10'` and `'010'` are not the same because they have different lengths, as the second string has a leading zero.                                         | `False`    |
| `print('10' > '010')`            | Lexicographically, `'10'` is greater than `'010'` because `'1' > '0'` in string comparison.                                                                          | `True`     |
| `print('10' > '8')`              | `'10'` is greater than `'8'` lexicographically because `'1' > '8'`.                                                                                                 | `True`     |
| `print('20' < '8')`              | Lexicographically, `'20'` is not less than `'8'` because `'2' > '8'`.                                                                                                | `False`    |
| `print('20' < '80')`             | Lexicographically, `'20'` is less than `'80'` because `'2' < '8'`.                                                                                                 | `True`     |

### Key Point:
String comparisons in Python are lexicographical, meaning they are compared character by character based on their Unicode values. This does not account for numerical values but compares the characters themselves.



## img prog
```
1)
print('10' == 10) # TRUE
print('10' != 10) # FALSE 
print('10' == 1)  # FALSE
print('10' != 1)  # TRUE
print('10' > 10)  # genrate error



2)
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

//o/p
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']


3)
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

//o/p
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

4)
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)

//0/p
['Where', 'are', 'the', 'snows', 'of', 'yesteryear?']


5)
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
print(s3[1])
//
['Where', 'are', 'the', 'snows', 'of', 'yesteryear?']
['Where', 'are', 'of', 'snows', 'the', 'yesteryear?']
are

```




## img question
```
1)
s1 = '12'      # have integer string value
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

//o/p
True

2)
s1 = '12.8'   # have float string value
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

//o/p
Genrate ValueError 

```


## 2.4.5 SECTION QUIZ

| **Question** | **Code** | **Answer** | **Explanation** |
|--------------|----------|------------|-----------------|
| **Question 1:** Which of the following lines describe a true condition? <br> 'smith' > 'Smith' <br> 'Smiths' < 'Smith' <br> 'Smith' > '1000' <br> '11' < '8' | `'smith' > 'Smith'` <br> `'Smiths' < 'Smith'` <br> `'Smith' > '1000'` <br> `'11' < '8'` | 1, 3, and 4 | Strings are compared lexicographically based on their Unicode code points. 'smith' > 'Smith' because lowercase letters have higher Unicode values than uppercase letters. |
| **Question 2:** What is the expected output of the following code? <br> s1 = 'Where are the snows of yesteryear?' <br> s2 = s1.split() <br> s3 = sorted(s2) <br> print(s3[1]) | `s1 = 'Where are the snows of yesteryear?'` <br> `s2 = s1.split()` <br> `s3 = sorted(s2)` <br> `print(s3[1])` | `are` | The `split()` method breaks the string into words. The `sorted()` method sorts the list alphabetically. 'are' is the second word in the sorted list. |
| **Question 3:** What is the expected result of the following code? <br> s1 = '12.8' <br> i = int(s1) <br> s2 = str(i) <br> f = float(s2) <br> print(s1 == s2) | `s1 = '12.8'` <br> `i = int(s1)` <br> `s2 = str(i)` <br> `f = float(s2)` <br> `print(s1 == s2)` | The code raises a ValueError exception | The `int()` function cannot convert a string with a decimal point ('12.8') into an integer, leading to a ValueError. |



## img prog.
```
print(10)
print(ord('1'))
print(ord('a'))
print('A')

//o/p
10
49
97
A
```


## imp exception
```
1)
try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

//o/p
zero


2)
try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

//o/p
airth



1)
def bad_fun(n):
    raise ZeroDivisionError  # This raises a specific error.

try:
    bad_fun(0)  # This calls the function where ZeroDivisionError is raised.
except ArithmeticError:  # This will catch any error that is a type of ArithmeticError.
    print("What happened? An error?")

print("THE END.")


//o/p
What happened? An error?
THE END.

//Note:-
The ZeroDivisionError is caught by the except ArithmeticError: block because ZeroDivisionError is a subclass of ArithmeticError. In Python, when an exception is raised, the catching block can catch that error if the error type matches, or if it's a subclass of the type specified in the except block.



2)
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

//o/p
I did it again!
I see!
THE END.



//Note Airthmatic and ZeroDivision  both error similar


3)

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
//o/p
below written anwser
```


| **Code/Action**                               | **Explanation**                                                                                                                                                                | **Example 1 (Valid Input)**                  | **Example 2 (Invalid Input)**              |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------|
| `x = float(input("Enter a number: "))`        | Takes user input, converts it into a floating-point number.                                                                                                                     | Input: `9`                                 | Input: `-9`                                |
| `assert x >= 0.0`                             | Asserts that the input number must be non-negative. If the condition is `False`, an `AssertionError` is raised.                                                                | `x = 9` (Condition is True)                | `x = -9` (Condition is False)              |
| `x = math.sqrt(x)`                           | Calculates the square root of `x` if the assertion is passed.                                                                                                                   | `math.sqrt(9)` → `3.0`                     | (Does not execute due to AssertionError)   |
| `print(x)`                                    | Prints the square root of `x`.                                                                                                                                                  | Output: `3.0`                              | No output due to the error.               |
| **Outcome**                                   | If the assertion is true, the program continues and prints the square root of the number. If the assertion fails, an `AssertionError` occurs, stopping the program.           | No error. The program prints `3.0`.         | AssertionError raised, program stops.     |









# Python Exceptions

| **Error Type**     | **Description**                                      | **Example** |
|--------------------|------------------------------------------------------|-------------|
| **LookupError**     | Raised when an invalid index is used in a sequence (list, tuple, etc.) or an invalid key is used in a dictionary. | `list = [1, 2, 3] \nprint(list[5])`<br> This will raise a `IndexError`, but can be caught with `LookupError`. |
| **IndexError**      | Raised when trying to access an index that is out of the range of a sequence. | `list = [1, 2, 3] \nprint(list[5])`<br> This will raise an `IndexError`, which indicates that the index is out of range for the given list. |
| **ValueError**      | Raised when an operation or function receives an argument of the correct type but an inappropriate value. | `int("abc")`<br> This will raise a `ValueError` because `"abc"` cannot be converted to an integer. |
| **KeyError**        | Raised when a dictionary key is not found. | `d = {"a": 1, "b": 2} \nprint(d["c"])`<br> This will raise a `KeyError` because "c" is not a valid key in the dictionary. |
| **TypeError**       | Raised when an operation or function is applied to an object of an inappropriate type. | `a = "5" + 3`<br> This will raise a `TypeError` because you cannot add a string and an integer. |
| **ZeroDivisionError**| Raised when dividing by zero. | `x = 1 / 0`<br> This will raise a `ZeroDivisionError`. |
| **FileNotFoundError**| Raised when trying to open a file that does not exist. | `open("nonexistentfile.txt")`<br> This will raise a `FileNotFoundError`. |
| **NameError**       | Raised when a local or global name is not found. | `print(undeclared_variable)`<br> This will raise a `NameError` because `undeclared_variable` has not been defined. |

---

### Example Code for Handling Exceptions

#### Example 1: `IndexError` & `LookupError`
```
python
try:
    # Risky code: accessing an index out of range
    lst = [1, 2, 3]
    print(lst[5])
except LookupError:
    # Dealing with erroneous lookups (e.g., invalid index or key)
    print("Caught a LookupError!")
except IndexError:
    # IndexError will not be caught here as it is a subclass of LookupError
    print("Caught an IndexError!")
```



# 2.7.3 Section Quiz

| **Question** | **Code** | **Expected Output** | **Explanation** |
|--------------|----------|---------------------|-----------------|
| **Question 1**: What is the expected output of the following code? | ```python<br>try:<br>    print(1/0)<br>except ZeroDivisionError:<br>    print("zero")<br>except ArithmeticError:<br>    print("arith")<br>except:<br>    print("some")``` | **zero** | The `ZeroDivisionError` is raised first, and the corresponding exception handler prints "zero". |
| **Question 2**: What is the expected output of the following code? | ```python<br>try:<br>    print(1/0)<br>except ArithmeticError:<br>    print("arith")<br>except ZeroDivisionError:<br>    print("zero")<br>except:<br>    print("some")``` | **arith** | The `ArithmeticError` is a superclass of `ZeroDivisionError`, so the first matching handler is executed. |
| **Question 3**: What is the expected output of the following code? | ```python<br>def foo(x):<br>    assert x<br>    return 1/x<br><br>try:<br>    print(foo(0))<br>except ZeroDivisionError:<br>    print("zero")<br>except:<br>    print("some")``` | **some** | The `assert` statement fails for 0, causing an `AssertionError`, which is caught by the general `except` block, printing "some". |


















## all type of exception
```
1) assert exception
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))



2)
IndexError
Location: BaseException ← Exception ← LookupError ← IndexError

Description: a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)

Code:

# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')




```


# 📚 Python Built-in Exceptions (Simplified Table)

Python programming mein galtiyan aur errors normal hote hain. Python ne inko sambhalne ke liye kuch built-in exceptions diye hain. Yaha hum important exceptions ko asaan aur simple language mein table ke form mein samjhayenge.

---

| No. | Exception Name    | Short Description (Easy Language)                                                                          | Example Code | Output |
|---- |-------------------|------------------------------------------------------------------------------------------------------------|--------------|--------|
| 1. | **ArithmeticError** | Maths calculation mein galti (jaise divide by zero ya wrong input)                                          | ```python\nfrom math import tan, radians\nangle = int(input('Enter angle: '))\nassert angle % 180 != 90\nprint(tan(radians(angle)))\n``` | Angle agar 90, 270 ho to error |
| 2. | **AssertionError**  | Jab `assert` ka condition galat ho jaye. Developer check ke liye use karta hai.                            | ```python\nassert 2 + 2 == 5\n``` | AssertionError |
| 3. | **BaseException**   | Sabse upar wali exception. Sare exceptions iske under aate hain.                                            | ```python\ntry:\n    x = 1/0\nexcept BaseException:\n    print("Caught base exception")\n``` | Caught base exception |
| 4. | **IndexError**      | Jab list ya tuple ke wrong index ko access karein.                                                          | ```python\nthe_list = [1, 2, 3]\nprint(the_list[5])\n``` | IndexError |
| 5. | **KeyboardInterrupt** | Jab user program ko beech mein Ctrl+C se band karne ki koshish kare.                                     | ```python\ntry:\n    while True:\n        pass\nexcept KeyboardInterrupt:\n    print("Program stopped by user")\n``` | Program stopped by user |
| 6. | **LookupError**     | Jab list, dictionary jaise collection mein galat key ya index ka use karein.                               | ```python\nmy_list = [1,2]\nprint(my_list[5])\n``` | LookupError |
| 7. | **MemoryError**     | Jab program itna bada ho jaye ki system ki memory khatam ho jaye.                                            | ```python\nstring = 'x'\ntry:\n    while True:\n        string += string\nexcept MemoryError:\n    print('Out of Memory!')\n``` | Out of Memory! |
| 8. | **OverflowError**   | Jab koi calculation number ko itna bada bana de ki Python store nahi kar paaye.                             | ```python\nfrom math import exp\nex = 1\ntry:\n    while True:\n        print(exp(ex))\n        ex *= 2\nexcept OverflowError:\n    print('Number too big')\n``` | Number too big |
| 9. | **ImportError**     | Jab kisi galat ya missing module ko import karne ki koshish karein.                                          | ```python\ntry:\n    import math\n    import abracadabra\nexcept ImportError:\n    print('Import failed')\n``` | Import failed |
| 10. | **KeyError**        | Jab dictionary mein aisi key access karen jo exist nahi karti.                                               | ```python\ndictionary = {'a': 'apple'}\nprint(dictionary['b'])\n``` | KeyError: 'b' |

---

# 📌 2.8.2 LAB: Safely Reading Integers (Simple Input Validation)

User se safe integer input lena hai. Agar galat input aaye to message dena hai aur phir se input lena hai.

### Sample Code:

```
python
def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if value < min or value > max:
                print(f"Error: the value is not within permitted range ({min}..{max})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")

number = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", number)

```




# 📋 2.8.4 SECTION QUIZ

| **Question** | **Answer** |
|:-------------|:-----------|
| Which exception will you use to protect your code from being interrupted through the use of the keyboard? | `KeyboardInterrupt` |
| What is the name of the most general of all Python exceptions? | `BaseException` |
| Which exception will be raised through the following unsuccessful evaluation: `huge_value = 1E250 ** 2`? | `OverflowError` |




# Python Exception Handling Quiz - 1 to 20

| Question | Answer | Code/Explanation |
|----------|--------|------------------|
| **Question 1:** Which of the exceptions will you use to protect your code from being interrupted through the use of the keyboard? | KeyboardInterrupt | The `KeyboardInterrupt` exception is raised when the user interrupts the execution (e.g., using `Ctrl+C`). |
| **Question 2:** What is the name of the most general of all Python exceptions? | BaseException | `BaseException` is the top-most class from which all other exceptions inherit. |
| **Question 3:** Which of the exceptions will be raised through the following unsuccessful evaluation? `huge_value = 1E250 ** 2` | OverflowError | This code leads to an overflow because the number is too large to be stored. |
| **Question 4:** Entering the try: block implies that: | Some of the instructions may not be executed | If an exception occurs inside the `try` block, only the code before the exception executes. |
| **Question 5:** The unnamed except: block: | Must be the last one | The unnamed `except:` block should be placed last to catch any unhandled exceptions. |
| **Question 6:** The top-most Python exception is called: | BaseException | `BaseException` is the most general exception, from which all others inherit. |
| **Question 7:** The following statement: `assert var == 0` | Will stop the program when `var != 0` | The `assert` statement checks if the condition is true. If false, it raises an `AssertionError` and stops the program. |
| **Question 8:** What is the expected output of the following code? `try: print("5"/0) except ArithmeticError: print("arith") except ZeroDivisionError: print("zero") except: print("some")` | zero | `ZeroDivisionError` is raised and handled by the second `except` block, printing "zero". |
| **Question 9:** Which of the following are examples of built-in concrete Python exceptions? | ImportError, IndexError | Both `ImportError` and `IndexError` are concrete exceptions. `BaseException` and `ArithmeticError` are abstract exceptions. |
| **Question 10:** ASCII is: | Short for American Standard Code for Information Interchange | ASCII is a character encoding standard. |
| **Question 11:** UTF‑8 is: | A form of encoding Unicode code points | UTF-8 is a widely used encoding for Unicode. |
| **Question 12:** UNICODE is a standard: | Like ASCII, but much more expansive | Unicode is a universal character encoding standard, whereas ASCII is limited. |
| **Question 13:** The following code: `x = '\'' print(len(x))` prints: | 1 | The string `'\''` represents a single quote, which is one character long. |
| **Question 14:** The following code: `print(ord('c') - ord('a'))` prints: | 2 | The difference between the Unicode code points of 'c' and 'a' is 2. |
| **Question 15:** The following code: `print(chr(ord('z') - 2))` prints: | x | The Unicode character corresponding to the code point of 'z' - 2 is 'x'. |
| **Question 16:** The following code: `print(3 * 'abc' + 'xyz')` prints: | abcabcabcxyz | The string 'abc' is repeated 3 times, and 'xyz' is appended. |
| **Question 17:** The following code: `print('Mike' > "Mikey")` prints: | True | String comparison is lexicographical, and 'Mike' is greater than 'Mikey'. |
| **Question 18:** The following code: `print(float("1, 3"))` prints: | Raises a ValueError exception | The string "1, 3" is invalid for conversion to float because of the comma. |
| **Question 19:** The following code: `x = ' '` print(len(x)) prints: | 1 | The string ' ' (space) has a length of 1. |
| **Question 20:** The following code: `print(ord('a') - ord('A'))` prints: | 32 | The difference between the Unicode code points of 'a' and 'A' is 32. |







NOTE :- IMP CODE
//input below code for both 1 and 2
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672


1)
print([list(map(int, input().split())) for _ in range(9)])
[[295743861], [431865927], [876192543], [387459216], [612387495], [549216738], [763524189], [928671354], [154938672]]
//o/p


2)
sudoku = [list(map(int, input().strip())) for _ in range(9)]

//o/p
[[2, 9, 5, 7, 4, 3, 8, 6, 1], [4, 3, 1, 8, 6, 5, 9, 2, 7], [8, 7, 6, 1, 9, 2, 5, 4, 3], [3, 8, 7, 4, 5, 9, 2, 1, 6], [6, 1, 2, 3, 8, 7, 4, 9, 5], [5, 4, 9, 2, 1, 6, 7, 3, 8], [7, 6, 3, 5, 2, 4, 1, 8, 9], [9, 2, 8, 6, 7, 1, 3, 5, 4], [1, 5, 4, 9, 3, 8, 6, 7, 2]]

| Aspect                 | Your Code (`split()`)                                       | My Code (`strip()`)                                     |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| **Input format**       | Expects **space-separated digits** like `2 9 5 7 4 3 8 6 1` | Expects **continuous digits** like `295743861`          |
| **How input is split** | Uses `input().split()` → splits on spaces                   | Uses `input().strip()` → treats each character as digit |
| **Fails if input is**  | `295743861` (will give just 1 number, not 9)                | `2 9 5 7 4 3 8 6 1` (will raise ValueError)             |
| **Common use**         | Used when user gives digits **with spaces**                 | Used when user gives digits **without spaces**          |

