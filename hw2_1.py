# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:05:59 2024

@author: LAM Quincy
"""
import math
print('====================================','\nThis program is use to calculate \na circle. ')
print('------------------------------------','\nType x to exit ')
while True:
    try:
        print('====================================')
        a=input('please input the radius: ')
        print('====================================')
        if a == 'x':
            print('Exit','Thanks for using')
            print('====================================')
            break
        r=int(a)
        A= round((math.pi)*r**2,2)
        P = round(2*(math.pi)*r,2)
        print("Area = ",A,'\nPerimeter = ',P,'\n\t(correct to 2 decimal places)')
    except ValueError:
        print('please input a correct number')