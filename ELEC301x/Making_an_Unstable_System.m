clear all;
clc;
x=[0 -1 2 3 0 1 -2 1 1 0 0 0 0];
a=1.1;
y=zeros(1,13);
%%% Update y so that y[n]=x[n]+a.*y[n-1].
%%% When computing the first value of y,
%%% assume that it was previously at rest, i.e. 0
%%% Your code here:
y1 = 0;
for i=1:length(x);
    y(i) = x(i)+(a*y1);
    y1 = y(i);
end       
        
%%%
subplot(1,2,1),stem(0:12,x),title('x')
subplot(1,2,2),stem(0:12,y),title('y')