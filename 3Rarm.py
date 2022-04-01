import py_compile
import matplotlib.pyplot as plt
from matplotlib import style
import math

phideg=float(input("Enter the angle: "))
x=float(input("Enter the x coordinate: "))
y=float(input("Enter the y coordinate: "))
pi=3.141592653589793238462643383279502884
phi=phideg*pi/180
a1=1
a2=1
a3=1
wx=x-a3*math.cos(phi)
wy=y-a3*math.sin(phi)
#c2=(wx*wx+wy*wy-a1*a1-a2*a2)/(2*a1*a2)
#if c2<=1:   
''' s2_1=math.sqrt(1-c2*c2)
    s2_2=-(math.sqrt(1-c2*c2))
    theta2_1=math.atan2(s2_1,c2)
    theta2_2=math.atan2(s2_2,c2)
    denom_1=a1*a1+a2*a2+2*a1*a2*math.cos(theta2_1);
    denom_2=a1*a1+a2*a2+2*a1*a2*math.cos(theta2_2);
    s1_1=(wy*(a1+a2*math.cos(theta2_1))-a2*math.sin(theta2_1)*wx)/denom_1
    s1_2=(wy*(a1+a2*math.cos(theta2_2))-a2*math.sin(theta2_2)*wx)/denom_2
    c1_1=(wx*(a1+a2*math.cos(theta2_1))-a2*math.sin(theta2_1)*wy)/denom_1
    c1_2=(wx*(a1+a2*math.cos(theta2_2))-a2*math.sin(theta2_2)*wy)/denom_2
    theta1_1=math.atan2(s1_1,c1_1)
    theta1_2=math.atan2(s1_2,c1_2)
    theta3_1=phi-theta1_1-theta2_1
    theta3_2=phi-theta1_2-theta2_2 '''
if 1 :    
    alpha=math.atan(wy/wx)
    theta2_1=theta2_2=pi-math.acos((a1*a1+a2*a2-wx*wx-wy*wy)/(2*a1*a2))
    theta1_1=alpha-math.acos((wx*wx+wy*wy+a1*a1-a2*a2)/(2*a1*math.sqrt(wx*wx+wy*wy)))
    theta1_2=alpha+math.acos((wx*wx+wy*wy+a1*a1-a2*a2)/(2*a1*math.sqrt(wx*wx+wy*wy)))
    #print("%f %f \n%f %f \n%f %f"%(theta1_1*180/pi,theta1_2*180/pi,theta2_1*180/pi,theta2_2*180/pi,theta3_1*180/pi,theta3_2*180/pi))

    ax_1=a1*math.cos(theta1_1)
    ax_2=a1*math.cos(theta1_2)
    ay_1=a1*math.sin(theta1_1)
    ay_2=a1*math.sin(theta1_2)
    #bx_1=ax_1+a2*math.cos(theta1_1+theta2_1)
    #by_1=ay_1+a2*math.sin(theta1_1+theta2_1)
    #bx_2=ax_2+a2*math.cos(theta1_2+theta2_2)
    #by_2=ay_2+a2*math.sin(theta1_2+theta2_2)
    #bx=ax_1+a2*math.cos(theta1_1+theta2_1)
    #by=ay_1+a2*math.sin(theta1_1+theta2_1)
    bx=wx
    by=wy
    cx=x
    cy=y
    style.use('ggplot')
    #sol1_x=[0,ax_1,bx_1,cx]
    #sol1_y=[0,ay_1,by_1,cy]
    #sol2_x=[0,ax_2,bx_2,cx]
    #sol2_y=[0,ay_2,by_2,cy]
    sol1_x=[0,ax_1,bx,cx]
    sol1_y=[0,ay_1,by,cy]
    sol2_x=[0,ax_2,bx,cx]
    sol2_y=[0,ay_2,by,cy]
    plt.plot(range(5))
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.draw()
    plt.plot(sol1_x,sol1_y,'g',label='line one', linewidth=3)
    plt.plot(sol2_x,sol2_y,'c',label='line two',linewidth=3, linestyle='dashed')
    print(sol1_x ,sol1_y, sol2_x, sol2_y)
    plt.title('arm diagram')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.legend()
    plt.grid(True,color='k')
    plt.show()

else:
    print("Invalid Input")  
    


