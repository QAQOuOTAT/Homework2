# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:05:59 2024

@author: LAM Quincy
"""
print('=======================================','\nType x to exit','\n=======================================')
while True:
    try :
        n=str(input('please input your name: '))
        if n == 'x':
            print('---------------------------------------')
            print('Exit','Thanks for using')
            print('=======================================')
            break
    
        a=int(input('please input your age: '))
        h=float(input('please input your hight: '))
        c=str(input('please input your favorite color: '))
        print('---------------------------------------')
        if a<=0:
            if h<=0:
                print(n,",favorite color is ",c,'\nAlso please input correct age and hight.')
            elif h>3:
                h1=h/100 
                print(n,",",h1,"m"," , favorite color is ",c,'\nAlso please input correct age.')
            else:
                print(n,",",h,"m"," , favorite color is ",c,'\nAlso please input correct age.')
        elif h>3:
            h1=h/100
            print(n,",",a,"years old ,",h1,"m"," , \nfavorite color is ",c,".")
        elif h<=0:
            print(n,",",a,"years old ,favorite color is ",c,'\nAlso please input correct hight.')
        else :
            print(n,",",a,"years old ,",h,"m"," , \nfavorite color is ",c,".")
        print('=======================================')
    except ValueError:
        print('---------------------------------------')
        print('please input a correctly','\n=======================================')