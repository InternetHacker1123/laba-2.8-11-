#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def test():
    number = int(input("Введите целое число: "))
    if number == 0:
        print("Не ноль!", file=sys.stderr)
        exit(1)
    if number > 0:
        positive()
    elif number < 0:
        negative()



def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == '__main__':
    test()