import numpy as np
from numpy import pi
a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.ndim)
# print(a.dtype.name)
# print(a.size)
# print(type(a))
b = np.array([6.5, 7.4, 8])
# print(b.dtype.name)
c=np.array([[1, 2], [3, 7]], dtype=complex)
# print(c)
d=np.empty((2,2,2,2,2))
# print(d)
# print(d.size)
e=np.arange(2,20,1.9)
# print(e)
f=np.linspace(0,10,4)
# print(f)
g=np.linspace(0, pi, 4)
# print(g)
# print(np.sin(g))
# print(np.random.rand(3,2))
#N(mu,sigma^2) = sigma * np.random.randn(...) + mu
h = np.random.randn(2,3)
print(h)
print(2. * h)
print(2. * h  + 3)
