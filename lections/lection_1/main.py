# import numpy as np


# np.random.seed(1)
# n = 60
# b = np.random.randint(1, 7, n)
# a = b[b == 3]
# m = len(a)
# W = m / n
#
# print(f'Mассив событий: {b} \n'
#       f'Mассив выпавших 3: {a}  \n'
#       f'Количество 3:  {m}, \n'
#       f'Вероятность выпадения: {W}')

# Смоделируем ситуацию, когда бросают две игральные кости одновременно 360 раз.
# Посчитаем относительную частоту события, когда на одной кости выпадает 1 , а на другой 2
# n = 360
# np.random.seed(1)
# c = np.random.randint(1, 7, size = n)
# d = np.random.randint (1, 7, size = n)
#
# a=c[(c==1) & (d==2)]
# m = len(a)
# W = m / n
# print(f'Mассив c= {c} \n'
#       f' \n'
#       f'Mассив d= {d}\n'
#       f' \n'
#       f'Mассив выпавших = {a} \n'
#       f'Количество: {m} \n'
#       f'Вероятность выпадения: {W}')


# Определить сочетания, размещения или перестановки используются для решения этой задачи.
# # Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты?
# import math
# n = int(input('n: '))
# k = int(input('k: '))
# def combination(n,k):
#       return math.math.factorial(n) // (math.math.factorial(k)*math.math.factorial(n-k))
# print(combination(n,k))


# Определить сочетания, размещения или перестановки
# используются для решения этой задачи. В магазине 20 покупателей. Сколькими способами они
# могут образовать очередь из 5 человек?

# import math
# n = int(input('n: '))
# k = int(input('k: '))
# def arrangement(n,k):
#       return math.math.factorial(n) // math.math.factorial(n-k)
# print(arrangement(n,k))


# 3)	Сколькими способами 5 покупателей могут образовать очередь?
# import math
# n = int(input('n: '))
# def arrangement(n):
#       return math.math.factorial(n)
# print(arrangement(n))

# Из колоды, состоящей из 36 карт, случайным образом выбраны 5.
# Сколько можем получить комбинаций, содержащих 2 туза без учета порядка

# n = 36
# k = 32
# m = 4
import math

n = math.factorial(52) / (math.factorial(4)*math.factorial(52 - 4))
P1 = (math.factorial(4) / (math.factorial(1)*math.factorial(4 - 1))) * (math.factorial(48) / (math.factorial(3)*math.factorial(48 - 3))) / n
P2 = (math.factorial(4) / (math.factorial(2)*math.factorial(4 - 2))) * (math.factorial(48) / (math.factorial(2)*math.factorial(48 - 2))) / n
P3 = (math.factorial(4) / (math.factorial(3)*math.factorial(4 - 3))) * (math.factorial(48) / (math.factorial(1)*math.factorial(48 - 1))) / n
P4 = math.factorial(4) / (math.factorial(4)*math.factorial(4 - 4)) / n
P = P1 + P2 + P3 + P4
print(f'n = {n} \n'
      f'P1 = {P1 :.2f} \n'
      f'P2 = {P2 :.3f} \n'
      f'P3 = {P3 :.5f} \n'
      f'P4 = {P4 :.7f} \n'
      f'Вероятность того, что из 4 вытащенных из колоды хотя бы один туз = {P :.2f} ')