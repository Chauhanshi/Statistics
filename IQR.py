# -*- coding: utf-8 -*-
"""
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .
"""

t = int(input())
n = list(map(int,input().split(" ")))
f = list(map(int,input().split(" ")))

"""
#it can be easily calculated with scipy.stats
from scipy.stats import iqr
import numpy as np
iqr(ls)
"""

n_ls =[]

for i in range(len(n)):
    t = f[i]
    for j in range(t):
        n_ls.append(n[i])

def med(ls):
    if len(ls)%2==0:
        i = sum(ls[len(ls)//2-1:len(ls)//2+1])/2
        m = i
    else:
        i = len(ls)//2
        m = ls[i] 
    return(m)


def iqr(ls):
    if len(ls)%2!=0:
        h = int(len(ls)/2)
        l = ls[:h]
        u= ls[h+1:]
    else:
        h=int(len(ls)//2)
        l= ls[:h]
        u = ls[h:]
    first = med(l)
    third = med(u)
    print(round(float(third-first),1))


f_ls = sorted(n_ls)
iqr(f_ls)