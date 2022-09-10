#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
#
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
#
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

class Worker:
    def __init__(self, inputStr):
        self.s = inputStr

    def reverse(Self):
        return reverseStr(Self.s)

    def contains(Self, containedStr):
        return containsWord(Self.s, containedStr)
        
    def palindrome(Self):
        return isPalindrome(Self.s)
       
    def upper(Self):
        return upperCaseStr(Self.s) 
