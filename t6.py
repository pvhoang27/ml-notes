import numpy as np
from sklearn.linear_model import LogisticRegression

# Dữ liệu từ ảnh
X = np.array([
    [0.5], [0.75], [1], [1.25], [1.5], [1.75], [1.75], [2], [2.25], [2.5],
    [2.75], [3], [3.25], [3.5], [4], [4.25], [4.5], [4.75], [5], [5.5]
])
y = np.array([
    0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 1, 1, 1, 1, 1
])

# Huấn luyện mô hình Logistic Regression
model = LogisticRegression()
model.fit(X, y)

# Dự đoán xác suất đậu khi học 1.5 giờ và 3 giờ
hours_test = np.array([[1.5], [3]])
probs = model.predict_proba(hours_test)

print("Xác suất đậu khi học 1.5 giờ:", probs[0][1])
print("Xác suất đậu khi học 3 giờ:", probs[1][1])

# Dự đoán nhãn
print("Dự đoán pass/fail cho 1.5 giờ:", model.predict([[1.5]]))
print("Dự đoán pass/fail cho 3 giờ:", model.predict([[3]]))