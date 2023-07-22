import numpy as np
from numpy.core.multiarray import empty

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(type(a))
print(a.reshape(3,3))

b = np.array([1, 2, 3, 4], 'float64')
print(b)
# print(np.sctypeDict)
print(np.complex64(b))
c = np.int32(b)
print(c)
print(np.array('Hello'))

mas = np.array([[1,2], [3,4], [5, 6]])
print(mas)
matrix = np.array([[[1, 2], [3,4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(matrix)
print(matrix[0])

# ------------Функции автозаполнения. Создание матриц----------
# empty(shape, ...) - возвращает новый массив заданного размера и типа данных,
# но без определенных значений.
emp = np.empty(10)
print(emp)
print(np.empty(10, 'int32'))
print(np.empty((3, 3), 'int16'))
#
# eye(N, M=None, ...) возвращает массив размером NxM с единичными диагональными элементами
# (остальные элементы равны 0)
print(np.eye(4))
print(np.eye(4, 2))
# idtntity(n, ...) - возвращает квадратный массив размерностью nxn c единичными
# элементами по главной диагонали(остальные равны 0)
print(np.identity(5))
# ones(shape, ...) - возвращает массив заданного размера и типа состоящий из всех единиц.
print(np.ones((5, 5)))
# zeros(shape, ...) - возвращает массив заданного типа состоящий из всех 0.
print(np.zeros((4,4)))
# full(shape, value, ...) Возвращает массив заданного размера и типа со значениями value.
print(np.full((5,5), 10))

