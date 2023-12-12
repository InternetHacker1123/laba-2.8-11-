#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    line = input("Введите любую строку: ")
    return line


def test_input(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False


def str_to_int(number):
    string_number = int(number)
    return string_number


def print_int(value):
    print(value)


if __name__ == '__main__':
    variable = get_input()

    if test_input(variable):
        return_value = str_to_int(variable)
        print_int(return_value)
    else:
        print("Вы ввели не число")