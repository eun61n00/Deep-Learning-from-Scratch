# 6.1.2 확률적 경사 하강법 SGD
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
        
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]
            
#SGD class를 사용한 신겸망 매개변수의 진행
#다음은 의사코드
#network = TwoLayerNet(...)
#optimizer = SGD()

#for i in range(1000):
#    ...
#    x_batch, t_batch = get_mini_batch(...) #미니배치
#    grads = network.gradient(x_batch, t_batch)
#    params = network.params
#    optimizer.update(params, grads)
#    ...

# 6.1.4 모멘텀momentum
class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None
        
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

#6.1.5 AdaGrad
class AdaGrad:
    def __init__(self, lr = 0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
