clear all;
% Write code to amplify (50x) and clip a sine wave 
% at amplitude 0.5 and -0.5
N = 1000;
t = linspace(0, (N-1)/1250, 1000);
x = sin(2*pi*440*t);
x = x';
y = 50*x;
y(y < -0.5) = -0.5;
y(y > 0.5) = 0.5;
s = y;
stem(t,s)