#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print("Input string is " + inputStr)
    print(reverseStr(inputStr))

    print("Does string contain apple? " + containsWord(inputStr, "apple"))
    print("Does string contain banana? " + containsWord(inputStr, "banana"))

    print("Is string a palindrome? " + isPalindrome(inputStr))
    print("Uppercase of string is " + upperCaseStr(inputStr))
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    w = Worker(inputStr)
    #Use the object to call each of the methods in the Worker class
    reverse = w.reverse()
    apple = w.contains("apple")
    banana = w.contains("banana")
    palindrome = w.palindrome()
    upper = w.upper()
    #Print the result of each call
    print(reverse)
    print("Does string contain apple? " + apple)
    print("Does string contain banana? " + banana)
    print("Is string a palindrome? " + palindrome)
    print("Uppercase of string is " + upper)
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




