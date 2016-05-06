lambda = 0.4;
N = 10;
n = 0:N-1;
h1 = zeros(1,N);
for i = 1:1:N,
    h1(i) = 1/N;
end
h1 = h1'; %SMA Filter
w1 = 0;
for i = 1:1:N,
    w1 = w1+N-(i-1);
end
h2 = zeros(1,N);
for i = 1:1:N,
    h2(i) = (N-(i-1))/(w1);
end
h2 = h2'; %WMA Filter
w2 = 0;
for i = 1:1:N,
    w2 = w2+exp(-lambda*(i-1));
end
h3 = zeros(1,N);
for i = 1:1:N,
    h3(i) = (exp(-lambda*(i-1)))/(w2);
end
h3 = h3'; %EMA Filter
subplot(311)
stem(n,h1);
subplot(312)
stem(n,h2);
subplot(313)
stem(n,h3);