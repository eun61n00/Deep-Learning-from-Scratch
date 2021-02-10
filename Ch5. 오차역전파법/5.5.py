# 5.5.1 ReLU 계층

class Relu:
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        print(out)
        print(out[self.mask])
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx
      
import numpy as np
x = np.array([[1.0, -0.5], [-2.0, 3.0]])

print(x)

mask = (x <= 0)
print(mask)


#5.5.2 sigmoid 계층

class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        
        return out
    
    def backward(self, dout):
        dx = dout * self.out * (1.0 - self.out)
        
        return dx
