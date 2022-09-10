#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#


def reverseStr(inputStr):
    x = len(inputStr) - 1
    s = ""
    while x >= 0:
        s += inputStr[x]
        x-=1
    return s


def containsWord(containingStr, containedStr):
    if containedStr in containingStr:
        return "Yes"
    else:
        return "No"
    
def isPalindrome(inputStr):
    s = reverseStr(inputStr)
    
    if s == inputStr:
        return "Yes"
    else:
        return "No"    

def upperCaseStr(inputStr):
    return inputStr.upper()
