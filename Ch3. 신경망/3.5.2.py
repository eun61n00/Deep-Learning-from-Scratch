#interpreter--------------------------------

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a)))   #제대로 계산되지 않는다. -> array([nan, nan, nan])

c = np.max(a)
print(a-c)    #array([0, -10, -20])

print(np.exp(a-c) / np.sum(np.exp(a-c)))
#arrya([])

#script-------------------------------

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)    #오버플로 해결
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
