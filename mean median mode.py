# -*- coding: utf-8 -*-
"""
Objective
In this challenge, we practice calculating the mean, median, and mode. 

Task
Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Constraints

, where  is the  element of the array.
Output Format

Print  lines of output in the following order:

Print the mean on a new line, to a scale of  decimal place (i.e., , ).
Print the median on a new line, to a scale of  decimal place (i.e., , ).
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

"""

import numpy as np
from scipy import stats

a = int(input())
numbers = list(map(int, input().split(" ")))

mean = np.mean(numbers)
median = np.median(numbers)
mode = stats.mode(numbers)

print(mean)
print(median)
print(mode[0][0])
