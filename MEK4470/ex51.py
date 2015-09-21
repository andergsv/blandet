from numpy import exp, linspace, zeros, linalg
import matplotlib.pyplot as plt

def exact(rho, u, x, gamma, the0, theend, L):
    return ( theend - the0 ) * ( exp( ( rho * u * x ) / float( gamma ) ) - 1 ) \
    / float( exp( ( rho * u * L ) / gamma ) - 1 ) + the0
L = 1
rho =1
gamma = 0.1
u= 0.25

xe = linspace( 0, L, 1001 )

def numerical(nodes, gamma, rho, u, L, thetaA, thetaB):
    dx = L / float( nodes )
    x = linspace( dx / 2., L - dx/2., L / float( dx ) )
    D = gamma / float( dx )
    F = rho * u
    a = zeros( (nodes,nodes) )
    a[0][0] = 3 * D + F / 2.
    for i in range( 1, nodes - 1 ):
        a[i][i] = 2 * D
        
    for j in range( 0, nodes - 1 ):    
        a[j+1][j] = -(D + F / 2.)
        a[j][j+1] = -(D - F / 2.)
        
    a[-1][-1] = 3 * D - F / 2.
    Su = zeros( (1, nodes) )
    Su[0][0] = (2 * D + F) * thetaA
    Su[-1][-1] = (2 * D - F) * thetaB
    theta = linalg.inv( a ) * Su
    th = zeros( nodes )
    for i in range( nodes ):
        th[i] = sum( theta[i, :] )
    return th, x
    
theta, x = numerical( 5, gamma, rho, u, L, 1, 0 )
print x
plt.plot( xe, exact( rho, u, xe, gamma, 1, 0, L ), 'b',
         x, theta, 'r--o')
plt.show()

