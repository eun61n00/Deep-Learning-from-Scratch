def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_X
    
    for i in range(step_num):
        grad = numerical_grdient(f, x)
        x -= lr * grad
        return x
