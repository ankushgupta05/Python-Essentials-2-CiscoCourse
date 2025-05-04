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



