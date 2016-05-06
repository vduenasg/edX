load('Week3_CaseStudy_Data.mat');
N = 5;
n = 0:N-1;
h1 = zeros(1,N);
for i = 1:1:N,
    h1(i) = 1/N;
end
h1 = h1'; %SMA Filter
u5 = filter(h1,1,[x; zeros(length(h1)-1,1)]); 

N = 20;
n = 0:N-1;
h1 = zeros(1,N);
for i = 1:1:N,
    h1(i) = 1/N;
end
h1 = h1'; %SMA Filter
u20 = filter(h1,1,[x; zeros(length(h1)-1,1)]);

N = 100;
n = 0:N-1;
h1 = zeros(1,N);
for i = 1:1:N,
    h1(i) = 1/N;
end
h1 = h1'; %SMA Filter
u100 = filter(h1,1,[x; zeros(length(h1)-1,1)]);

subplot(311)
plot(0:length(u5)-1,u5,'-r');
hold on
plot(0:length(x)-1,x,'-b');
subplot(312)
plot(0:length(u20)-1,u20,'-r');
hold on
plot(0:length(x)-1,x,'-b');
subplot(313)
plot(0:length(u100)-1,u100,'-r');
hold on
plot(0:length(x)-1,x,'-b');