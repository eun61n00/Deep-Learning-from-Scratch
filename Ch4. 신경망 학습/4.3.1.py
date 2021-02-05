# 수치 미분의 나쁜 구현
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h)-f(x)) / h
  
#개선
def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)
