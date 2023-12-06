import numpy as np
x = np.array([[1,2,3],[4,5,6]])
print('x.shape:', x.shape)
print('x.shape[0]:',x.shape[0])

y = np.array([[11,22,33],[44,55,66]])
print(y)
print(np.append(x,y,axis=0))
print(np.append(x,y,axis=1).shape)
