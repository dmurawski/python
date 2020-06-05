import numpy as np 
import matplotlib.pyplot as plt

#3
# a = np.arange(25)
# a=a.reshape(5,5)
# np.fill_diagonal(a, 0)
# print(a)

# 1
# x = np.arange(-10,10,1)
# y = x**2*np.pi
# plt.plot(x,y)
# plt.show()

# 2

# x=np.arange(0,6,0.01)
# y=np.cos(x)
# y1=np.sin(x)
# y2=-np.cos(x)
# y3=-np.sin(x)
# plt.plot(x,y,color="lightblue",label="f(x)=cos(x)")
# plt.plot(x,y1,'--',color="orange",label="f(x)=sin(x)")
# plt.plot(x,y2,'.',color="green",label="f(x)=-cos(x)")
# plt.plot(x,y3,'-.',color="red",label="f(x)=-sin(x)")
# plt.legend(loc=4)
# plt.show()


# Zad 4 
np.random.seed(1)
matrix1=np.random.randint(1,11,25).reshape(5,5)
matrix2=np.random.randint(1,11,25).reshape(5,5)
print(matrix1,'\n\n',matrix2)
matrix1=matrix1*2
matrix2=matrix2*2
print(matrix1,'\n\n',matrix2)
matrix3 = np.concatenate((matrix1,matrix2),axis=0)
print('\n',matrix3)
wektor = []
wektor = matrix3[:,1:3]
wektor = wektor.flatten()
print(wektor)
matrix = np.arange(1,101,1).reshape(10,10)
print(matrix)
wektor=[]
wektor2=[]
wektor = matrix[::2]
wektor2 = matrix[1::2]
print('\n',wektor)

print('\n',wektor2)
wektordiag=np.diag(matrix)

print('\n',wektordiag)