#!/usr/bin/env python3
# Name: lab7i.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/07/10

def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:',schoolName)
function1()
print('print() in main on schoolName:',schoolName)
function2()
print('print() in main on schoolName:',schoolName)

