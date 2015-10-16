import matplotlib.pyplot as plt
import numpy as np

print 'Write the four-digit NACA type you want to plot:'
Naca = raw_input()
dgt = [int(i) for i in str(Naca)]
if len(dgt) > 4 or len(dgt)< 4:
    print 'NACA number needs to be a 4-digit number!'
else:
    md = float(dgt[0])
    pd = float(dgt[1])
    lst_digits = float(str(dgt[2])+str(dgt[3]))

    print 'Write desired chord length:'
    c = float(raw_input())

    #symetric NACA airfoil
    def yt(lst_digits,c,x):
        t = lst_digits/100.
        return 5*t*c*(0.2969*np.sqrt(x/c)+ (-0.1260)*(x/c) + \
           (-0.3516)*(x/c)**2 + \
           0.2843*(x/c)**3 + (-0.1015)*(x/c)**4)

    #Mean camber line    
    def yc(md,pd, c, x):
        m = md/100.
        p = pd/10.
        if x >= 0 and x <= p*c:
            return m* x/p**2 *(2*p - x/c)
        else:
            return m * (c-x)/(1-p)**2 * (1 + x/c-2*p)
            
    #cambered airfoil           
    def xyUL(x, md, pd, lst_digits, c):
        xU = np.zeros(len(x))
        xL = np.zeros(len(x))
        yU = np.zeros(len(x))
        yL = np.zeros(len(x))
        def theta(x, md, pd, c):
            m = md/100.
            p = pd/10.
        
            if x >= 0 and x<= p*c:
                return np.arctan(2* m / p**2 * (p-x/c))
            else: 
                return np.arctan(2*m/(1-p)**2 * (p-x/c))
                
        for i in range(len(x)):
            xU[i] = x[i] - yt(lst_digits, c, x[i]) * np.sin(theta(x[i],md,pd,c))
            xL[i] = x[i] + yt(lst_digits, c, x[i]) * np.sin(theta(x[i],md,pd,c))
            yU[i] = yc(md,pd,c,x[i]) + yt(lst_digits, c, x[i])*np.cos(theta(x[i],md,pd,c))
            yL[i] = yc(md,pd,c,x[i]) - yt(lst_digits, c, x[i])*np.cos(theta(x[i],md,pd,c))
        return xU, xL, yU, yL

    x = np.linspace(0,c,1001)
    if md > 0.2 and pd > 0.2:
        xu, xl, yu, yl = xyUL(x,md,pd,lst_digits, c)
        plt.plot(xu,yu, 'b')
        plt.plot(xl,yl, 'b')
        plt.title('NACA'+Naca)
        plt.xlabel('x')
        plt.ylabel('y')
    else:
        plt.plot(x,yt(lst_digits, c, x),'b') 
        plt.plot(x,-yt(lst_digits, c, x),'b')
        plt.title('NACA'+Naca)
        plt.xlabel('x')
        plt.ylabel('y')


    plt.axis('equal')
    plt.savefig(Naca+'.png')
    plt.show()



