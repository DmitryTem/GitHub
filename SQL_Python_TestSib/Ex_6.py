

class BadInt():
	def __init__(self, num):
		self.data = num
	def __add__(self, other):
		return self.data * other.data
	def __mul__(self, other):
		return self.data + other.data





a = BadInt(5)
b = BadInt(6)


assert a+b == 30, 'Sum check'
assert a*b == 11, 'Multiply check'



