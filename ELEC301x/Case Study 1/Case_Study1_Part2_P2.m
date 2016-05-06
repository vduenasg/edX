rng(1);
u = inline('t >=0');
N = 100;
t = 0:(N-1);
x = 0.5*u(t)';

                  
w1 = randn(N,1)*0.02;
w2 = randn(N,1)*0.02;

y1 = x+w1;

figure;
subplot(2,1,1)
plot(t,y1)

y2 = x+w2;                  
subplot(2,1,2)
plot(t,y2) 