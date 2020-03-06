# -*- coding: utf-8 -*-
"""

Objective
 In this challenge, we practice calculating a weighted mean. 

Task
Given an array,X ,N of  integers and an array, W, representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Input Format

The first line contains an integer,N , denoting the number of elements in arrays X and W .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .


Print the weighted mean on a new line. Your answer should be rounded to a scale of 1  decimal place.


"""


t = int(input())
a = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))


def w_mean(a,w):
    c = sum([a[i]*w[i] for i in range(len(a))])
    w_m = c/(sum(w))
    print(round(w_m,1))


w_mean(a,w)
