Q 1) 
2.5.6   LAB   Improving the Caesar cipher
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.
The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.
Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Test Data :-  

#1
Sample input:
abcxyzABCxyz 123
2
Sample output:
cdezabCDEzab 123

#2
Sample input:
The die is cast
25
Sample output:
Sgd chd hr bzrs



// code

s = input()
n = int(input())

res = list(map(lambda x: ( chr((ord(x)-ord('a') + n)%26 + ord('a')) if x.islower() else chr((ord(x)-ord('A') + n)%26 + ord('A')) if x.isupper() else x ) if x.isalnum() else x,s))
print(''.join(res))







Q 2)
2.5.7   LAB   Palindromes
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent;
there are more than a few correct solutions – try to find more than one.
Test your code using the data we've provided.
#1
Sample input:
Ten animals I slam in a net

Sample output:
It's a palindrome


#2
Sample input:
Eleven animals I slam in a net

Sample output:
It's not a palindrome


// code
n ='Ten animals I slam in a net'
n = n.split(' ')
n = ''.join(n)
if n.lower()[::-1] == n.lower()[::]:
    print('It\'s a palindrome')
else:
    print('Its \'not a palindrome')







Q 3)
2.5.8   LAB   Anagrams
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent
Test your code using the data we've provided.

Test Data
#1
Sample input:
Listen
Silent

Sample output:
Anagrams

#2
Sample input:
modern
norman

Sample output:
Not anagrams


// code
s1 = input().replace(" ","").lower()
s2 = input().replace(" ","").lower()
index = 0
for i in s1:
    if (i not in s2):
        index = 1
        break;
    
else:
    print('Anagrams',end=' ')





Q 4)
2.5.9   LAB   The Digit of Life
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple – you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
Test your code using the data we've provided.

Test Data
#1
Sample input:
19991229

Sample output:
6

#2
Sample input:
20000101

Sample output:
4


// code by me:

x = int(input())

temp = 0
while(1):
    temp += x%10
    x //= 10
    if x == 0:
        break;

x = temp
temp = 0
while(1):
    temp += x%10
    x //= 10
    if x == 0:
        break;
print(temp)

// code by chatgpt
def sum_digits(n):
    return sum(int(d) for d in str(n))

x = int(input())
print(sum_digits(sum_digits(x)))








Q 5)
2.5.10   LAB   Find a word!
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.

Test Data
#1
Sample input:
donor
Nabucodonosor

Sample output:
Yes

#2
Sample input:
donut
Nabucodonosor

Sample output:
No



// code
s1 =input()
s2 = input()
temp = []
start = 0
for index,val  in enumerate(s1):
    res=s2.find(val,start,len(s2))
    if res != -1 :
        start = index
    temp.append(res)
if (-1) in temp and (sorted(temp) != temp):
    print("NO") 
else:
    print("YES")








## for below code IMP Notes

NOTE :- IMP CODE
```
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
//o/p
[[295743861], [431865927], [876192543], [387459216], [612387495], [549216738], [763524189], [928671354], [154938672]]


2)
sudoku = [list(map(int, input().strip())) for _ in range(9)]

//o/p
[[2, 9, 5, 7, 4, 3, 8, 6, 1], [4, 3, 1, 8, 6, 5, 9, 2, 7], [8, 7, 6, 1, 9, 2, 5, 4, 3], [3, 8, 7, 4, 5, 9, 2, 1, 6], [6, 1, 2, 3, 8, 7, 4, 9, 5], [5, 4, 9, 2, 1, 6, 7, 3, 8], [7, 6, 3, 5, 2, 4, 1, 8, 9], [9, 2, 8, 6, 7, 1, 3, 5, 4], [1, 5, 4, 9, 3, 8, 6, 7, 2]]

```
| Aspect                 | Your Code (`split()`)                                       | My Code (`strip()`)                                     |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| **Input format**       | Expects **space-separated digits** like `2 9 5 7 4 3 8 6 1` | Expects **continuous digits** like `295743861`          |
| **How input is split** | Uses `input().split()` → splits on spaces                   | Uses `input().strip()` → treats each character as digit |
| **Fails if input is**  | `295743861` (will give just 1 number, not 9)                | `2 9 5 7 4 3 8 6 1` (will raise ValueError)             |
| **Common use**         | Used when user gives digits **with spaces**                 | Used when user gives digits **without spaces**          |





Q 6)
2.5.11   LAB   Sudoku
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:
reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

Test Data
#1
Sample input:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:
Yes

#2
Sample input:
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:
No


