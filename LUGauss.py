import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[3, 2, -1],
              [2, -4, 2],
              [1, 3, 2]])

B = np.array([10000, 8000, 15000])

LU, piv = lu_factor(A)

X = lu_solve((LU, piv), B)

print("Jumlah optimal kontribusi dari setiap divisi:")
print(f"Produksi (P): {X[0]}")
print(f"Pemasaran (M): {X[1]}")
print(f"Keuangan (K): {X[2]}")
