# 0x06. Python - Classes and Objects

# Learning Objectives

## General

Why Python programming is awesome

What is OOP

“first-class everything”

What is a class

What is an object and an instance

What is the difference between a class and an object or instance

What is an attribute

What are and how to use public, protected and private attributes

What is self

What is a method

What is the special __init__ method and how to use it

What is Data Abstraction, Data Encapsulation, and Information Hiding

What is a property

What is the difference between an attribute and a property in Python

What is the Pythonic way to write getters and setters in Python

How to dynamically create arbitrary new attributes for existing instances of a class

How to bind attributes to object and classes

What is the __dict__ of a class and/or instance of a class and what does it contain

How does Python find the attributes of an object or class

How to use the getattr function

# Tasks

## mandatory

### Write an empty class Square that defines a square:

You are not allowed to import any module

```guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$
```
