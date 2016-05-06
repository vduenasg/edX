clear all;
N = 1000;   %Muestras
F0 = 440;   %Hz
tf = 0.8/1000; %Time Factor
t = linspace(0,(N-1)/(1000/0.8),1000);
F = zeros(N,20);
for c=1:20
    for r=1:N
        F(r,c) = sin(2*pi*(c-1)*F0*(tf*(r-1)));
    end
end
v=[0 1 0 0.75 0 0.5 0 0.14 0 0.5 0 0.12 0 0.17 0 0 0 0 0 0 ];
s = F*v';

subplot(211)
stem(t,F)
subplot(212)
stem(t,s)