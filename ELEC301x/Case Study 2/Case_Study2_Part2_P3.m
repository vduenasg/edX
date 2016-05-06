load('Week3_CaseStudy_Data.mat');
lambda = 0.2;
N = 20;
n = 0:N-1;
w1 = 0;
for i = 1:1:N,
    w1 = w1+N-(i-1);
end
h2 = zeros(1,N);
for i = 1:1:N,
    h2(i) = (N-(i-1))/(w1);
end
h2 = h2'; %WMA Filter

y2 = filter(h2,1,[x; zeros(length(h2)-1,1)]);

w2 = 0;
for i = 1:1:N,
    w2 = w2+exp(-lambda*(i-1));
end
h3 = zeros(1,N);
for i = 1:1:N,
    h3(i) = (exp(-lambda*(i-1)))/(w2);
end
h3 = h3'; %EMA Filter

y3 = filter(h3,1,[x; zeros(length(h3)-1,1)]);

subplot(211)
plot(0:length(y2)-1,y2,'-r');
hold on
plot(0:length(x)-1,x,'-b');
subplot(212)
plot(0:length(y3)-1,y3,'-r');
hold on
plot(0:length(x)-1,x,'-b');