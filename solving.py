import numpy as np
import matplotlib.pyplot as plt

fileOpen = open("myfile.txt", "r")
total=fileOpen.readline().split('|')
fileOpen.close()

b1=total[1].split(',')
b0=total[0].split(';')

a1=b0[0].split(',')
a2=b0[1].split(',')
a3=b0[2].split(',')

a=np.array([[9,2,4],[1,10,4],[2,-4,10]])

a[0][0]=a1[0]
a[0][1]=a1[1]
a[0][2]=a1[2]
a[1][0]=a2[0]
a[1][1]=a2[1]
a[1][2]=a2[2]
a[2][0]=a3[0]
a[2][1]=a3[1]
a[2][2]=a3[2]

print(a)

det_a=((a[0][0]*a[1][1]*a[2][2])+(a[0][1]*a[1][2]*a[2][0])+(a[0][2]*a[1][0]*a[2][1])-
       (a[2][0]*a[1][1]*a[0][2])-(a[2][1]*a[1][2]*a[0][0])-(a[2][2]*a[1][0]*a[0][1]))
print(det_a)

dx=np.array([[20,2,4],[6,10,4],[-15,-4,10]])
dx[0][0]=b1[0]
dx[1][0]=b1[1]
dx[2][0]=b1[2]
print(dx)


det_dx=(dx[0][0]*dx[1][1]*dx[2][2]+dx[0][1]*dx[1][2]*dx[2][0]+dx[0][2]*dx[1][0]*dx[2][1]-
       dx[2][0]*dx[1][1]*dx[0][2]-dx[2][1]*dx[1][2]*dx[0][0]-dx[2][2]*dx[1][0]*dx[0][1])
print(det_dx)
dy=np.array([[9,20,4],[1,6,4],[2,-15,10]])
dy[0][1]=b1[0]
dy[1][1]=b1[1]
dy[2][1]=b1[2]
print(dy)

det_dy=(dy[0][0]*dy[1][1]*dy[2][2]+dy[0][1]*dy[1][2]*dy[2][0]+dy[0][2]*dy[1][0]*dy[2][1]-
       dy[2][0]*dy[1][1]*dy[0][2]-dy[2][1]*dy[1][2]*dy[0][0]-dy[2][2]*dy[1][0]*dy[0][1])
print(det_dy)
dz=np.array([[9,2,20],[1,10,6],[2,-4,-15]])
dz[0][2]=b1[0]
dz[1][2]=b1[1]
dz[2][2]=b1[2]
print(dz)

det_dz=(dz[0][0]*dz[1][1]*dz[2][2]+dz[0][1]*dz[1][2]*dz[2][0]+dz[0][2]*dz[1][0]*dz[2][1]-
       dz[2][0]*dz[1][1]*dz[0][2]-dz[2][1]*dz[1][2]*dz[0][0]-dz[2][2]*dz[1][0]*dz[0][1])
print(det_dz)


x=det_dx/det_a
y=det_dy/det_a
z=det_dz/det_a

print("The roots of the equations:",'X:',x   ,'Y:',y    ,'Z:',z)
w="The roots of the equations:",'X:',x   ,'Y:',y    ,'Z:',z
fileOpen = open("myfile.txt", "a")
fileOpen.writelines(str(w)+'\n')
fileOpen.close()

equation_1=(9*x)+(2*y)+(4*z)
equation_1


equation_2=x+(10*y)+(4*z)
equation_2


equation_3=(2*x)-(4*y)+(10*z)
equation_3



