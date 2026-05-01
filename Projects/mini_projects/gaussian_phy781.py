import numpy as np

def gauss_jordan (A):
    n = len(A)
    aug = np.hstack ([A, np.eye(n)]) #Build augumented matrix [A | I]
    
    for i in range (n):
        max_row = np.argmax(abs (aug [i:, i])) + i
        aug [[i, max_row ]] = aug [[ max_row , i]]
        
        aug [i] = aug[i] / aug[i,i]
        for j in range (n):
                if j != i:
                    aug [j] -= aug[j,i] * aug[i]
    return aug [:, n:]

#QUICK TEST
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

A_inv = gauss_jordan(A)
print(np.round(A_inv, 4))

# Verify: A @ A_inv should give Identity

print(np.round(A @ A_inv, 6))
