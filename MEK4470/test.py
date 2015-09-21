import numpy as np

D = 3
F = 2
a = np.zeros((5,5))
a[0][0] = 3*D+F/2.
for i in range(1,4):
    a[i][i] = 2*D
    
for j in range(0,4):    
    a[j+1][j] = D+F/2.
    a[j][j+1] = D-F/2.
        
a[-1][-1] = 3*D-F/2.
    
print a

b = np.zeros((5,1))
c = np.zeros((1,5))

b[2][0] = 3
c[0][2] = 2

Su = np.zeros((1,5))
Su[0][0] = 2*D+F
    #theta = zeros((1,nodes))
theta = np.linalg.inv(a)*Su
print theta
