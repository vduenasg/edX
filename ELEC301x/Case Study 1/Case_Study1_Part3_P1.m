clear all;
N = 1000;   %Muestras
F0 = 440;   %Hz
tf = 0.8/1000; %Time Factor
F = zeros(N,20);
for c=1:20
    for r=1:N
        F(r,c) = sin(2*pi*(c-1)*F0*(tf*(r-1)));
    end
end