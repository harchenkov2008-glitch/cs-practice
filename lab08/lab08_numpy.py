import numpy as np

#1. создание векторов и матриц

print("=" * 60)
print('1.создание векторов и матриц')
print('=' * 60)

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype = int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print('hours', hours)
print('hours.shape', hours.shape)
print('hours.ndim', hours.ndim)
print('hours.size', hours.size)
print('hours.dtype', hours.dtype)
print('line', line)
print('zeros', zeros)
print('unknown_table:\n', unknown_table)
print('identity:\n', identity)

#2

print()
print("=" * 60)
print('2')
print('=' * 60)

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])


#3

print()
print("=" * 60)
print('3')
print('=' * 60)

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])

central = temperatures[:2, 1:3]
print(central)
print(central.shape)

#4

print()
print("=" * 60)
print('4')
print('=' * 60)

matrix = np.arange(1, 26).reshape(5, 5)
print(matrix)

first_three = matrix[:3]
print(first_three, first_three.shape)

last_two = matrix[-2:]
print(last_two, last_two.shape)

first_two_cols = matrix[:, :2]
print(first_two_cols, first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print(fragment, fragment.shape)

corner = matrix[-2:, -2:]
print(corner, corner.shape)


#5
print()
print("=" * 60)
print('5')
print('=' * 60)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print(vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print(small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix)
print(matrix)

#6
print()
print("=" * 60)
print('5')
print('=' * 60)

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T


print(numbers.shape)
print(table.shape)
print(transposed.shape)
