#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4, Part 2"""

import time
import random


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
        end = time.time()
    return end-start

def shell_sort(a_list):
    """this function returns the time it takes to run the shell sort on a list"""

    istart = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()
    final = end - istart

    return final


def gap_insertion_sort(a_list, start, gap):
    """this function defines positioning for the shell_sort function"""

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    """this function returns the time it takes to run the builtin python sort on a list"""
    start = time.time()
    a_list.sort()
    end = time.time()
    return end-start


def main():
    """this function test 3 types of sort functions for a worst case scenario; insertion sort, shell sort,
       and the built-in python sort function. It then returns the average run time for each sort"""

    list_a = random.sample(xrange(500), 500)*100
    list_b = random.sample(xrange(1000), 1000)*100
    list_c = random.sample(xrange(10000), 10000)*100

    insertion_sort(list_a)
    insort1 = insertion_sort(list_a)
    insort2 = insertion_sort(list_b)
    insort3 = insertion_sort(list_c)
    insortlist = [insort1, insort2, insort3]
    sum1 = sum(insortlist)
    avg1 = sum1/3

    shell_sort(list_a)
    shell1 = shell_sort(list_a)
    shell2 = shell_sort(list_b)
    shell3 = shell_sort(list_c)
    shlist = [shell1, shell2, shell3]
    sum2 = sum(shlist)
    avg2 = sum2/3

    python_sort(list_a)
    pysort1 = python_sort(list_a)
    pysort2 = python_sort(list_b)
    pysort3 = python_sort(list_c)
    pylist = [pysort1, pysort2, pysort3]
    sum3 = sum(pylist)
    avg3 = sum3/3


    print "Insertion sort took {:.7f}".format(avg1),"seconds to run, on average"
    print "Shell sort search took {:.7f}".format(avg2), "seconds to run, on average"
    print "Python sort search took {:.7f}".format(avg3), "seconds to run, on average"