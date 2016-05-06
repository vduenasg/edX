close all;
clear all;
load('Week3_CaseStudy_Data.mat');
lambda = 0.2;
N = 20;

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
full=length(x);
FORE = 252;
x2013 = zeros(252,1);
a = 0;
for i = 1:1:FORE,
    if i<N+2
        x1 = [x(full-N+i:end);x2013(1:i-1)];
    else
        x1 = x2013(i-N:i-1);
    end
    for e = 1:1:N-1
        a = a + (h3(e)*x1(N-e));
    end
    x2013(i) = a;
    a = 0;
end
plot(0:length(x2013)-1,x2013,'r')
hold on
plot(0:length(price2013)-1,price2013)