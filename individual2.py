#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    # Ввод списка чисел
    nums = input("Введите список чисел через пробел: ").split()

    # Количество положительных элементов списка
    num_pos = len([float(num) for num in nums if float(num) > 0])

    # Сумма элементов после последнего 0
    sum_after_zero = sum([float(num) for num in nums[nums.index("0") + 1:]])

    # Преобразование списка
    nums_new = sorted([float(num) for num in nums], key=lambda x: x <= 1)

    # Вывод результата
    print("Количество положительных элементов: ", num_pos)
    print("Сумма элементов после последнего 0: ", sum_after_zero)
    print("Преобразованный список: ", nums_new)

