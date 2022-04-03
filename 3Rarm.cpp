#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<math.h>
void polarxy(int link,float angle);
float link_x,link_y;

int main()
{   float phideg,x,y;
    link_x=0,link_y=0;
    std::cout<<"Enter the angle and x,y coordinates: \n";
    std::cin>>phideg>>x>>y;
    float const pi=3.141592653589793238462643383279502884;
    float phi=phideg*pi/180;
    int a1=1,a2=1,a3=1;
    float wx=x-a3*cos(phi);
    float wy=y-a3*sin(phi);
    float alpha=atan(wy/wx);
    float theta2_1=(pi-acos((a1*a1+a2*a2-wx*wx-wy*wy)/(2*a1*a2)));
    float theta2_2=(pi-acos((a1*a1+a2*a2-wx*wx-wy*wy)/(2*a1*a2)));
    float theta1_1=alpha-acos((wx*wx+wy*wy+a1*a1-a2*a2)/(2*a1*sqrt(wx*wx+wy*wy)));
    float theta1_2=alpha+acos((wx*wx+wy*wy+a1*a1-a2*a2)/(2*a1*sqrt(wx*wx+wy*wy)));
    //float theta2_1=alpha-theta1_1;
    //float theta2_2=alpha+theta1_2;
    if(sqrt(x*x+y*y)>(a1+a2+a3)|| ((a1*a1+a2*a2-wx*wx-wy*wy)/(2*a1*a2))>1)
    {
        theta1_1=atan(y/x);
        theta1_2=atan(y/x);
        theta2_1=atan(y/x);
        phi=atan(y/x);
    }
    std::cout<<theta1_1*180/pi<<"\t"<<theta2_1*180/pi<<"\t"<<phi*180/pi<<"\t";
    std::cout<<"\n The coordinates for link 1 is:\n";
    polarxy(a1,theta1_1);
    std::cout<<"\n The coordinates for link 2 is:\n";
    polarxy(a2,theta2_1);
    std::cout<<"\n The coordinates for link 3 is:\n";
    polarxy(a3,phi);
    

    return 0;
}

void polarxy(int link,float angle)
{
  link_x=link_x+link*cos(angle);
  link_y=link_y+link*sin(angle);
  std::cout<<link_x<<"\t"<<link_y<<"\t";

}