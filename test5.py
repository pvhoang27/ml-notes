import numpy as np

def grad(x):
    return 2*x + 5*np.cos(x)

def cost(x):
    return x**2 + 5*np.sin(x)

def myGD1(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) < 1e-3:  # just a small number
            break
        x.append(x_new)
    return (x, it)

x_list, num_iter = myGD1(2, 0.1)
print("Các giá trị x qua từng vòng lặp:", x_list)
print("Số vòng lặp:", num_iter)
print("Giá trị nhỏ nhất tìm được:", x_list[-1])
print("Giá trị hàm cost tại điểm nhỏ nhất:", cost(x_list[-1]))