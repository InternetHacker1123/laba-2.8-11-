#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    # Определить функцию для нахождения площади круга.
    def circle(radius):
        return math.pi * radius ** 2

    # Ввести радиус и высоту цилиндра.
    radius = float(input("Введите радиус цилиндра: "))
    visota = float(input("Введите высоту цилиндра: "))

    # Посчитать площади боковой и всей поверхностей.
    ploshad_boka = 2 * math.pi * radius * visota
    vsya_ploshad = (ploshad_boka + 2 * circle(radius))

    # Узнать хочет ли получить пользователь всю площадь.
    zapros = input("Вам нужна полная площадь цилиндра?")

    if zapros.lower() == "да":
        print(f"Площадь боковой поверхности цилиндра: "
              f"{ploshad_boka}")
    else:
        print(f"Полная площадь цилиндра: "
              f"{vsya_ploshad}")


if __name__ == '__main__':
    cylinder()