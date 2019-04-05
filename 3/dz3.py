# 1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# count = 0
# for i in range(2, 1000000):
#     if all([i % j == 0 for j in range(2, 10)]):
#         print(i)
#         count += 1
#
# print(count)

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# def get_array_with_indexes_of_even(m):
#     return [i for i in range(len(m)) if m[i] % 2 == 0]

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


# def swap_min_and_max(m):
#     buf = m[:]
#     max_i = buf.index(max(buf))
#     min_i = buf.index(min(buf))
#     buf[max_i], buf[min_i] = buf[min_i], buf[max_i]
#     return buf

# 4. Определить, какое число в массиве встречается чаще всего.

# def get_stats(m: list) -> dict:
#     stat = dict()
#
#     for i in m:
#         if i in stat:
#             stat[i] += 1
#         else:
#             stat[i] = 1
#
#     return stat
#
#
# def get_most_common(stat: dict) -> tuple:
#     max_num = 0
#     max_count = 0
#     for k, v in stat.items():
#         if k > max_num:
#             max_num = k
#             max_count = v
#
#     return max_num, max_count

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# def get_max_negative_elem_index(m):
#     elem = max([i for i in m if i < 0])
#     return m.index(elem)


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

def get_sum(m):
    min_index = m.index(min(m))
    max_index = m.index(max(m))
    begin, end = min(min_index, max_index)+1, max(min_index, max_index)
    return sum(m[begin:end])

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# def get_two_min(m):
#     return sorted(m)[:2]
#
# print(get_two_min([3,2,1,4,6,7,0,98,73,2,8]))


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# import copy
# import pprint
#
# def input_matrix(N):
#     matr = []
#     for i in range(N):
#         matr.append([])
#         for j in range(N):
#             matr[i].append(int(input(f"Input m[{i}][{j}]:")))
#
#     return matr
#
# def add_sum(matr):
#     res = copy.deepcopy(matr)
#     for i in range(len(res)):
#         res[i].append(sum(res[i]))
#     return res
#
#
# pprint.pprint(add_sum(input_matrix(3)), width=30)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# import random
# from pprint import pprint
#
# def transpose_matrix(matr):
#     return list(zip(*matr))
#
# def get_mins_on_columns(matr):
#     mins = []
#     for i in transpose_matrix(matr):
#         mins.append(min(i))
#     return mins
#
# def generate_matrix(N):
#     res = []
#     for i in range(N):
#         res.append([])
#         for j in range(N):
#             res[i].append(random.randint(1,100))
#     return res
#
# matr = generate_matrix(5)
# pprint(matr, width=30)
# print(max(get_mins_on_columns(matr)))