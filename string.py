#INTRODUCTION TO STRING
'''
a string is a sequence of character enclosed with single quotes('..') or double quotes
string can contain letters,numbers,symbols and white spaces
string are immutable
string cannot be modified once created because string are immutable'''


#string operator
'''
concatenation:use '+' operator two concatenate two or more string
repetation:use '*' operator to repeat string a certain number of time
indexing: use [] bracket to find indexing
length:use len() operator to find length of string
'''

#string manipulation
'''
isalpha():check if all the character in string are alphabets
isdigit():check if all the characters in string is digit
isalnum():check if all the characters in string are in alphabet or in number
islower():check if all the characters in string are in lowercase alphabets
isupper():check if all the characters in string are in uppercase alphabets
startswith():check if string starts with a value
endswith():check if string ends with a value'''


#CODE

#<1>concatenation
'''str1='aditya'
str2='sinha'
print(str1 + str2)'''

#<2>repetaion
'''str1='aditya'
str2=str1*3
print(str2)'''

#<3>indexing
'''str1='aditya'
print(str1[3])
print(str1[4])
print(str1[1])
print(str1[0])'''

#<4>length
'''str='aditya'
print(len(str))'''


#STRING MANIPULATION
x="aditya"
print(x)
print(x.isalpha())
print(x.isdigit())
print(x.isalnum())
print(x.upper())
print(x.lower())
print(x.isupper())
print(x.islower())
print(x.endswith(x))