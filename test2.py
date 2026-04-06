import numpy as np

# Dữ liệu huấn luyện
X_train = np.array([
    [60, 2, 10],
    [40, 2, 5],
    [100, 3, 7]
])
y_train = np.array([10, 12, 20])

# Tính tham số w theo công thức w = (X^T X)^(-1) X^T y
X = X_train
y = y_train.reshape(-1, 1)
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Dự đoán giá cho căn nhà x = (50, 2, 8)
x_new = np.array([50, 2, 8])
y_pred = x_new @ w
print("X^T X:\n", X.T @ X)
print("Nghịch đảo (X^T X):\n", np.linalg.inv(X.T @ X))
print("X^T y:\n", X.T @ y)
print("w:\n", w)

print("------------------------------")
print("Tham số w:", w.flatten())
print("Dự đoán giá nhà:", y_pred.item())