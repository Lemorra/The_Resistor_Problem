from numpy import *
from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3

N_x=25
N_y=25
rad=8.75
Niter=1500

phi=zeros((N_y,N_x))
Jx=zeros((N_y,N_x))
Jy=zeros((N_y,N_x))

x=linspace(-12,13,25)
y=linspace(-12,13,25)

Y,X=meshgrid(y,x)

ii=where(((X*X)+(Y*Y))<=(8.75*8.75))

#print(ii)
#print()
#print(X)

phi[ii]=1.0

fig1=plt.figure(1)
a1x=fig1.add_subplot(111)
a2x=fig1.add_subplot(111)

c=a1x.contour(phi)
plt.clabel(c)
a2x.plot(ii[0],ii[1],'ro')


errors=zeros(1500)
Ni_x=linspace(1,1500,1500)

for k in range(Niter):
	oldphi=phi.copy()
	phi[1:-1,1:-1]=0.25*(phi[1:-1,0:-2]+phi[1:-1,2:]+phi[0:-2,1:-1]+phi[2:,1:-1])
	phi[1:-1,0]=phi[1:-1,1]
	phi[1:-1,-1]=phi[1:-1,-2]
	phi[0,1:-1]=phi[1,1:-1]
	phi[ii]=1.0
	errors[k]=(abs(phi-oldphi)).max()

fig2=plt.figure(2)
b1x=fig2.add_subplot(111)
b2x=fig2.add_subplot(111)
b3x=fig2.add_subplot(111)
b1x.semilogy(Ni_x,errors,'r-',label='error curve')
#b2x.loglog(Ni_x,errors,'g-')
b3x.plot(Ni_x[::50],errors[::50],'bo',label='every 50th iteration')
plt.xlabel('No of iteration')
plt.ylabel('Error')
plt.title('Error v/s No of iteration')

fig4=figure(4)
ax=p3.Axes3D(fig4)
title('The 3D surface plot of the potential')
surf=ax.plot_surface(Y,X,phi.T,rstride=1,cstride=1,cmap=cm.jet)

fig5=figure(5)
bx=p3.Axes3D(fig5)
title('The 3D contour plot of the potential')
bx.contour(Y,X,phi.T)

Jx[1:-1,1:-1]=0.5*(phi[1:-1,0:-2]-phi[1:-1,2:])
Jy[1:-1,1:-1]=0.5*(phi[0:-2,1:-1]-phi[2:,1:-1])

fig6=figure(6)
cx1=fig6.add_subplot(111)
cx2=fig6.add_subplot(111)
cx2.plot(ii[0],ii[1],'ro')
cx1.quiver(Jx[:,:],Jy[:,:])

#print(phi)

plt.show()
