# -*- coding: utf-8 -*-
"""
Objective
In this challenge, we practice calculating standard deviation. 

Task
Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the respective elements of the array.

Constraints

, where  is the  element of array .
Output Format

Print the standard deviation on a new line, rounded to a scale of  1 decimal place


"""


import math

t = int(input())
ls = list(map(int,input().split(" ")))

"""
# can be easily calculated using numpy
import numpy as np
print(np.std(ls))
"""
m = sum(ls)/len(ls)
sd = math.sqrt((sum((i-m)**2 for i in ls))/(len(ls)))

print(round(sd,1))