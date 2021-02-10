#5.4.1 곱셈계층

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
        
    def forward(self, x, y):
        self.x = x
        self.y = y
        
        out = x*y
        
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x #x와 y를 바꾼다
        
        return dx, dy
        
apple = 100
apple_num = 2
tax = 1.1

#계층들
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price) #220

