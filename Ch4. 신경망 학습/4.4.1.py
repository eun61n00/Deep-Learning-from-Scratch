def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_X
    
    for i in range(step_num):
        grad = numerical_grdient(f, x)
        x -= lr * grad
        return x
    
#문제: 경사법으로  f((x0), (x1)) = (x0)^2 + (x1)^2의 최솟값을 구하라.
def function_2(x):
    return x[0]**2 + x[1]**2

init_x = np.array([-3.0, 4.0])
gradient_descent(function_2, init_x = init_x, lr=0.1, step_num=100)
