#오차제곱합 SSE, sum of squares for error

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]     #'2'일 확률이 가장 높다고 추정함
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]     #'7'일 확률이 가장 높다고 추정함
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]      #정답은 '2'

def sum_squares_error(y, t):
    return 0.5*np.sum((y-t)**2)
  
print(sum_squares_error(np.array(y1), np.array(t)))
print(sum_squares_error(np.array(y2), np.array(t)))
