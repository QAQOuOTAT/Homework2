# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:05:59 2024

@author: LAM Quincy
"""
print('=======================================','\ntype x to exit','\n=======================================')
while True:
    try :
        n=str(input('please input your name: '))
        if n == 'x':
            print('=======================================')
            print('Exit','Thanks for using')
            print('=======================================')
            break
    
        a=int(input('please input your age: '))
        h=float(input('please input your hight: '))
        c=str(input('please input your favorite color: '))
    
        if h>3:
            h1=h/100
            print('=======================================')
            print(n,",",a,"years old ,",h1,"m"," , \nfavorite color is ",c,'\n=======================================')
        elif h<=0:
            print('=======================================')
            print(n,",",a,"years old ,favorite color is ",c,'\nAlso please input correct hight','\n=======================================')
        else :
            print('=======================================')
            print(n,",",a,"years old ,",h,"m"," , \nfavorite color is ",c,'\n=======================================')
    except ValueError:
        print('please input a correctly','\n=======================================')