#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;
//La ecuación diferencial es: d2y/dt2 = -w2y, con y(0)=1 y v(0)=0. Se va a integrar de 0 hasta 30.

void explicit_Euler(float h);
void rk4(float h);
void lf(float h);
float w=1.0;
float Y=1.0;
float T=10000.0;

int main(){
    explicit_Euler(0.5);
    rk4(0.5);
    lf(0.5);
    return 0;
}

void explicit_Euler(float h){
    ofstream outfile;

    outfile.open("explicito.txt");

    float yn, yn1;
    float vn,vn1;
    int N=T/h;
    yn=Y;
    vn=0;
    outfile<<0<<' '<<yn<<' '<<vn<<endl;
    for(int i=1;i<=N;i++){
        yn1=yn+h*vn;
        vn1=vn-h*w*w*yn;
        yn=yn1;
        vn=vn1;
        outfile<<i*h<<' '<<yn<<' '<<vn<<endl;        
    }
    
    outfile.close();
}
void rk4(float h){
    ofstream outfile;

    outfile.open("rk4.txt");

    float yn, yn1;
    float vn,vn1;
    int N=T/h;
    float k11,k12,k13,k14;
    float k21,k22,k23,k24;
    yn=Y;
    vn=0;
    outfile<<0<<' '<<yn<<' '<<vn<<endl;
    for(int i=1;i<=N;i++){
        k11=h*(vn);
        k21=h*(-w*w*yn);
            
        k12=h*(vn+k21/2);
        k22=h*(-w*w*(yn+k11/2));
            
        k13=h*(vn+k22/2);
        k23=h*(-w*w*(yn+k12/2));
        
        k14=h*(vn+k23);
        k24=h*(-w*w*(yn+k13));
        
        yn1=yn+(k11+2*k12+2*k13+k14)/6;
        vn1=vn+(k21+2*k22+2*k23+k24)/6;
        yn=yn1;
        vn=vn1;
        outfile<<i*h<<' '<<yn<<' '<<vn<<endl;        
    }
    
    outfile.close();
}
void lf(float h){
    ofstream outfile;

    outfile.open("lf.txt");

    float yn, yn1;
    float vn,vn1;
    float vn12;
    int N=T/h;
    yn=Y;
    vn=0;
    outfile<<0<<' '<<yn<<' '<<vn<<endl;
    for(int i=1;i<=N;i++){
        vn12=vn + h/2*(-w*w*yn);
        yn1=yn+vn12*h;
        vn1=vn12 + h/2*(-w*w*yn1);
        yn=yn1;
        vn=vn1;
        outfile<<i*h<<' '<<yn<<' '<<vn<<endl;        
    }
    
    outfile.close();
}



