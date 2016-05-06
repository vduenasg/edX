load('Week3_CaseStudy_Data.mat');
N = 10;
n = 0:N-1;
h1 = zeros(1,N);
for i = 1:1:N,
    h1(i) = 1/N;
end
h1 = h1'; %SMA Filter

y1 = conv(h1,x);

s1 = filter(h1,1,[x; zeros(length(h1)-1,1)]); 
%zero padding because the length of its output equals the length of its input
t = 0:length(y1)-1;
plot(t,y1,'-r');
hold on
plot(t,s1,'-b');
d = norm(y1,2)-norm(s1,2);