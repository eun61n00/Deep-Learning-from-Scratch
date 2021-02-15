#6.2.2 은닉층의 활성화값 분포
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.random.randn(1000, 100) #1000개의 데이터
node_num = 100 #각 은닉층의 노드(뉴런) 수
hidden_layer_size = 5 #은닉층이 5개
activation = {} #이곳에 활성화 결과(활성화값)를 저장

for i in range(hidden_layer_size):
    if i != 0:
        x = activation[i-1]
        
    w = np.random.randn(node_num, node_num) *1
    a = np.dot(x, w)
    z = sigmoid(a)
    activation[i] = z
    
#히스토그램 그리기
for i, a in activation.items():
    plt.subplot(1, len(activation), i+1)
    plt.title(str(i+1)+"-layer")
    plt.hist(a.flatten(), 30, range(0,1))
plt.show()

#가중치를 표준편차를 0.01로 한 정규분포로 초기화
#w = np.random.randn(node_num, node_num) * 0.01

#가중치를 Xavier 초기값으로 초기화
#node_num = 100
#w = np.random.randn(node_num, node_num) / np.sqrt(node_num)
