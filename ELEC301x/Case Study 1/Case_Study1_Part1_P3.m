% Write code to implement 0.8-sec long square wave
% and triangle wave of length 1000,frequency 440Hz.
N = 1000;
t = linspace(0, (N-1)/1250, 1000);
x = sin(2*pi*440*t);
y = square(2*pi*440*t);
z = sawtooth(2*pi*440*t,0.5);
subplot(311)
plot(t,x)
subplot(312)
plot(t,y)
subplot(313)
plot(t,z)