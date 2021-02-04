# 교차 엔트로피 오차 CCE, cross entropy error

import numpy as np

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]     #'2'일 확률이 가장 높다고 추정함
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]     #'7'일 확률이 가장 높다고 추정함
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]      #정답은 '2'

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))       #정답인 원소를 모델이 정답이라고 예측한 확률에 자연로그 취함
  
cross_entropy_error(np.array(y1), np.array(t))
cross_entropy_error(np.array(y2), np.array(t))
