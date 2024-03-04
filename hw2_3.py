# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:25:29 2024

@author: LAM Quincy
"""
print('This program is use to decide a number','\n\t type x to exit ')
while True:
    try :
        x=input('please input a number: ')
        if x == 'x':
            print('Exit','Thanks for using')
            break
        
        num=int(x)  
        if num%2==0:
            print(x,'is an even number')
        else:
            print(x,'is an odd number')
    except ValueError:
        print('please input a correct number')