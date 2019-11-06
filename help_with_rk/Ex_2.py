import numpy as np


class OLS():
	def __init__(self, v1=np.random.randn(100,3), v2 = np.random.randn(100,3)):
		self.X = v1
		self.y = v2

	def beta(self):
		b = np.dot(np.dot(np.linalg.inv(np.dot(self.X.T, self.X)), self.X.T), self.y)
		return b

	def V(self):
		b = self.beta()
		n = len(self.X)
		k = len(self.X[0])
		q = 1/(n-k)*np.dot((self.y - np.dot(self.X,b)).T, (self.y - np.dot(self.X,b)))
		v = np.dot(q, np.linalg.inv(np.dot(self.X.T, self.X)))
		return v

	def predict(self, xm = np.array([1,0,1])):
		b = self.beta()
		n = len(self.X)
		k = len(self.X[0])
		q = 1/(n-k)*np.dot((self.y - np.dot(self.X,b)).T, (self.y - np.dot(self.X,b)))
		y2 = np.dot(xm.T,b)
		vy = np.dot(q,1 + np.dot(np.dot(xm.T, np.linalg.inv(np.dot(self.X.T, self.X))), xm))
		return y2,vy






X = np.random.randn(100,3)
y = X.dot(np.array([1,2,3])) + np.random.randn(100)


test = OLS(X,y)

print('Run beta:')
print(test.beta())

print('Run V:')
print(test.V())

print('Run predict:')
print(test.predict(np.array([1,0,1])))
