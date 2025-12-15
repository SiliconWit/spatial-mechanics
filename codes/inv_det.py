import numpy as np

# -------------------------
# 4x4 Homogeneous Matrix
# -------------------------
H2 = np.array([
    [1,  0,  0, -5],
    [0, -1,  0, 10],
    [0,  0, -1,  8],
    [0,  0,  0,  1]
], dtype=float)

H2_inv = np.linalg.inv(H2)
det_H2 = np.linalg.det(H2)

print("4x4 Matrix H2:\n", H2)
print("\nInverse of 4x4 H2:\n", H2_inv)
print("\nDeterminant of 4x4 H2:", det_H2)

# -------------------------
# 3x3 Rotation from H2
# -------------------------
R = H2[:3, :3]

R_inv = np.linalg.inv(R)
det_R = np.linalg.det(R)

print("\n3x3 Rotation Matrix from H2:\n", R)
print("\nInverse of 3x3 R:\n", R_inv)
print("\nDeterminant of 3x3 R:", det_R)

# -------------------------
# Additional 3x3 Matrix
# -------------------------
R_new = np.array([
    [ 0, -1,  0],
    [-1,  0,  0],
    [ 0,  0,  1]
], dtype=float)

det_R_new = np.linalg.det(R_new)
R_new_inv = np.linalg.inv(R_new)

print("\nAdditional 3x3 Matrix R_new:\n", R_new)
print("\nInverse of R_new:\n", R_new_inv)
print("\nDeterminant of R_new:", det_R_new)

