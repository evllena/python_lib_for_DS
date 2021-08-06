import numpy as np

print('TASK 1:')
a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]]).T
print(a)

mean_a = a.mean(axis=0)
print(mean_a)

print('TASK 2:')

a_centered = np.subtract(a, mean_a)
print(a_centered)

print('TASK 3:')

column_1 = a_centered[:, 0]
column_2 = a_centered[:, 1]
a_centered_sp = column_1.dot(column_2)
print(a_centered_sp, a_centered_sp/(len(column_1)-1))

print('TASK 4:')
matrix = np.cov(a.transpose())
cov = matrix[0, 1]
print(cov)
