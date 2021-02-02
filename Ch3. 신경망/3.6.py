import sys, os
sys.path.append(os.pardir)    #부모 디렉터리의 파일을 가져올 수 있도록 설정
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize = False)

#각 데이터의 형상 출력
print(x_train.shape)    #(60000, 784)
print(t_train.shape)    #(60000,)
print(x_test.shape)    #(10000, 784)
print(x_test.shape)    #(10000,)

import numpy as np
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize = False)

img = x_train[0]
lable = t_train[0]
print(lable)    #5

print(img.shape)    #(784,)
img = img.reshape(28, 28)    #원래 이미지의 모양으로 변형
print(img.shape)    #(28, 28)

img_show(img)

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize = True, flatten = True, one_hot_label = False)
    return x_test, t_test
  
def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
        
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y
  
x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len()):
    y = predict(network, x[i])
    p = np.argmax(y)    # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i]:
        accuracy_cnt += 
print("Accuracy: " + str(float(accuracy_cnt) / len(x)))
