import numpy as np
import random as rand
np.zeros((2, 3))
x = np.ones((2, 3, 4)) * 128
#print(x)
np.arange(1, 10, 2)
x1 = np.linspace(0, 10, 5)

fileName = "out2.npy"
#with open(fileName, "wb") as fp:
#    np.save(fp, x1)
print("-----------我是分隔線---------")
with open(fileName, "rb") as fp:
    x2 = np.load(fp)
    print(x2)

np.full((3, 2), 8)     # 建立一個3*2全為8的陣容

print("-----------我是分隔線---------")
np.random.seed(1723)
y = np.random.randint(2, 135, (2, 3))
print(y)
z = y.reshape(1, 6)
print(z)
r = np.random.shuffle(z)
print(r)

data = list("This is a book")
print(data)
rand.seed(1723)
rand.shuffle(data)
print("".join(data))

a = np.array([1, 2, 3, 4])      #一維陣列建立
# print(a)
b = np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype=float)   #二維陣列建立
# print(b)
c = np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [             #三維陣列建立
             (2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype=float)
# print(c)