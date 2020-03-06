# -*- coding: utf-8 -*-
"""
Objective
In this challenge, we practice calculating quartiles. 

Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.


"""

t = int(input())
ls = list(map(int,input().split(" ")))

"""
import numpy as np
np.quartile(ls,0.25)
np.quartile(ls,0.5)
np.quartile(ls,0.75)
"""

n_ls = sorted(ls)

def med(ls):
    if len(ls)%2==0:
        i = sum(ls[len(ls)//2-1:len(ls)//2+1])/2
        m = i
    else:
        i = len(ls)//2
        m = ls[i] 
    return(m)


def Qrt(ls):
    if len(ls)%2!=0:
        h = int(len(ls)/2)
        l = ls[:h]
        u= ls[h+1:]
    else:
        h=int(len(ls)//2)
        l= ls[:h]
        u = ls[h:]
    print(int(med(l)))
    print(int(med(ls)))
    print(int(med(u)))


Qrt(n_ls)