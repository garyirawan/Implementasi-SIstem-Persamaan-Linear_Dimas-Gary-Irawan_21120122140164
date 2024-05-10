import numpy as np

A = np.array([[3, 2, -1],
              [2, -4, 2],
              [1, 3, 2]])

B = np.array([10000, 8000, 15000])

A_inv = np.linalg.inv(A)

X = np.dot(A_inv, B)

print("Jumlah optimal kontribusi dari setiap divisi:")
print(f"Produksi (P): {X[0]}")
print(f"Pemasaran (M): {X[1]}")
print(f"Keuangan (K): {X[2]}")
