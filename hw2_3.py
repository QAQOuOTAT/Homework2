# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:25:29 2024

@author: LAM Quincy
"""
print('=======================================')
print('This program is use to decide a number','\n\t (Even or Odd)')
print('---------------------------------------','\nType x to exit ')
print('=======================================')
while True:
    try :
        x=input('please input a number: ')
        if x == 'x':
            print('---------------------------------------')
            print('Exit','Thanks for using')
            print('=======================================')
            break
        print('---------------------------------------')
        num=int(x)  
        if num%2==0:
            print(x,'is an even number')
        else:
            print(x,'is an odd number')
        print('=======================================')
    except ValueError:
        print('please input a correct number')
        print('=======================================')
