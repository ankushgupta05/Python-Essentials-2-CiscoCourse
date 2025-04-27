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






