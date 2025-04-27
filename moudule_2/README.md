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





```
