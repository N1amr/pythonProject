import matplotlib.pyplot as p

p.plot(range(20), range(20))
p.show()

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
x = [
	[1, 1],
	[-1, -1]
]
y = [1, 2]
nb.fit(x, y)

test = -2
print nb.predict(test)
