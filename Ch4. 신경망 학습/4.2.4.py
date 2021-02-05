import numpy as np

#정답 레이블이 one-hot-incoding 일때 (one_hot_label = True)
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0] #???
    return -np.sum(t * np.log(y + 1e-7)) / batch_size
 
#정답 레이블이 one-hot-incoding 이 아닐때 (one_hot_label = False)
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_Size
