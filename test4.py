import numpy as np

# Dữ liệu huấn luyện (loại bỏ dòng 4 và 6)
X_train = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183])
y_train = np.array([49, 50, 51, 54, 58, 59, 60, 72, 63, 64, 66, 67, 68])

# Thêm cột 1 vào X để tính hệ số tự do (w0)
X_b = np.c_[np.ones((X_train.shape[0], 1)), X_train]

# Tính w theo công thức w = (X^T X)^(-1) X^T y
w = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y_train

print("Tham số w:", w)

# Dự đoán cân nặng cho chiều cao 155 và 160 (dòng 4 và 6)
X_test = np.array([[1, 155], [1, 160]])
y_pred = X_test @ w

print("Dự đoán cân nặng cho chiều cao 155cm:", y_pred[0])
print("Dự đoán cân nặng cho chiều cao 160cm:", y_pred[1])

print("-------------------------------")

print("Sai số cho 155cm:", abs(y_pred[0] - 52))
print("Sai số cho 160cm:", abs(y_pred[1] - 56))