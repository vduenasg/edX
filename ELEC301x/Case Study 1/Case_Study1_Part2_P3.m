rng(1);
s1 = 0.2;
s2 = 0.8;
N = 1000;
t = 0:(N-1);
y = (sin(t/50)+cos(t/200)-sin(t/100))';

                  
w1 = randn(N,1)*s1;
w2 = randn(N,1)*s2;

figure;
subplot(1,3,1)
plot(t,y)

y1 = y+w1;                  
subplot(1,3,2)
plot(t,y1)

y2 = y+w2;                  
subplot(1,3,3)
plot(t,y2) 