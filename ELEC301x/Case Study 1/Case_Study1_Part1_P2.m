clear all;
% Write code to implement a 0.8-sec long sine wave of length 1000 and 
% frequency 440 Hz

% To plot your signal, you can use either: plot(t,x) or stem(t,x)
N = 1000;
t = linspace(0, (N-1)/1250, 1000);
x = sin(2*pi*440*t);
x = x'
stem(t,x)
y = 50*x;
stem(t,y)