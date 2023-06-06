#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Запрашиваем ввод списка чисел у пользователя
    numbers = []
    for i in range(10):
        number = int(input("Введите число: "))
        numbers.append(number)

    # Считаем сумму и количество элементов кратных 2
    sum = 0
    count = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
            count += 1

    # Выводим результаты на экран
    print("Список чисел:", numbers)
    print("Сумма чисел кратных 2:", sum)
    print("Количество чисел кратных 2:", count)

