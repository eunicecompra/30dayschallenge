#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

class BubbleSort:
    def __init__(self):
        self.swap_cnt = 0

    def do_bubble_sort(self, size, array):
        swapped = True

        while(swapped):
            swapped = False
            for i in range(size):
                if i+1 == size:
                    break

                if array[i] > array[i+1]:
                    tmp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = tmp
                    swapped = True
                    self.swap_cnt += 1

        return array

