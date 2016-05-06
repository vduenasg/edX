close all;
clear all;
load('Week3_CaseStudy_Data.mat');
lambda = 0.2;
h3 = exp(-lambda*(0:19));
h3 = h3';
h3 = h3/sum(h3);

l = length(x);
x2013 = zeros(252,1);
x2013(1) = fliplr(h3')*x(l-19:l);
for i = 2:20
    x2013(i) = fliplr(h3')*[x(l-20+i:l);x2013(1:i-1)];
end

for i = 21:252
    x2013(i) = fliplr(h3')*x2013(i-20:i-1);
end

figure;
plot(x2013);
hold on;
plot(price2013,'r');
title('Predicted and Real Oil Prices in 2013')
ylabel('Dollar per Barrel')
legend('Predicted Oil Price in 2013','Real Oil Price in 2013');