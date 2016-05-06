u = inline('t >=0');
N = 100;
t = 0:(N-1);
x = 0.5*u(t)';
stem(t,x)