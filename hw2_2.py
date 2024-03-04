# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:05:59 2024

@author: LAM Quincy
"""
n=str(input('please input your name: '))
a=int(input('please input your age: '))
h=float(input('please input your hight: '))
c=str(input('please input your favorite color: '))
if h>100:
    h1=h/100
    print(n,",",a,"years old , ",h1,"m"," , favorite color is ",c)
elif h<=0:
    print(n,",",a,"years old , favorite color is ",c,'\nAlso please input correct hight')
else :
    print(n,",",a,"years old , ",h,"m"," , favorite color is ",c)
