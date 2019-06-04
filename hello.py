#!/usr/bin/env python3
import sys

print('HelloWorld')

def hello(name):
    print('Hello %s' % name)

hello('kaotu')

name = input("Enter your name: ")
print("World " + name)

path = str(sys.argv)
print("path: "+ sys.argv[1])