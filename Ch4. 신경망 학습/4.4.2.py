import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) #정규분포로 초기화
        
    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        
        return loss
      
net = simpleNet()
print(net.W) #가중치 매개변수 초기화

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

print(np.argmax(p))

t = np.array([0, 0, 1]) #정답레이블

print(net.loss(x, t))


def f(W): #인수 W는 dummy로 만든 것
    return net.loss(x, t)
#파이썬에서 람다lamda기법을 써서 정의하면, 
#f = lambda w: net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)

