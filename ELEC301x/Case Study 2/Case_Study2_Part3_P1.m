clear all
close all
rng(1);
lambda = 0.2;
N = 20;
FORE = 20
v = ones(N,1);

v = v+randn(N,1)*0.05;

q = zeros(FORE,1);

w2 = 0;
for i = 1:1:N,
    w2 = w2+exp(-lambda*(i-1));
end
h3 = zeros(1,N);
for i = 1:1:N,
    h3(i) = (exp(-lambda*(i-1)))/(w2);
end
h3 = h3'; %EMA Filter
h3 = fliplr(h3);
a = 0;
for i = 1:1:FORE,
    v = [v(i:FORE);q(1:i-1)];
    for e = 1:1:N-1
        a = a + (h3(e)*v(N-e));
    end
    q(i) = a;
    a = 0;
end
plot(0:length(q)-1,q)

