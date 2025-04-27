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
```




