import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)

def plotData(x,y , y_hat=None):
	plt.scatter(x,y, marker='.')
	if y_hat is not None :
				plt.scatter(x,y_hat,  marker='v')
	plt.title('Data')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

def getData(n):
	x = np.random.randn(n,1)
	y = 2*x + 1 + np.random.randn(n,1)	# Adding random noise
	return x,y

n = 100	
X_ori , y = getData(n)
#plotData(X_ori,y)

ones = np.ones((n,1))

#design matrix
X = np.append(X_ori,ones,axis=1)

#closed form solution
w = np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,y))
#print(w)


#make prediction
y_hat = np.dot(X,w)
plotData(X_ori,y,y_hat)
