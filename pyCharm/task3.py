#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    mult = 1
    number = int(input("Введите число: "))

    while number != 0:
        mult *= number
        number = int(input("Введите число: "))

    print(mult)


if __name__ == '__main__':
    multiply()