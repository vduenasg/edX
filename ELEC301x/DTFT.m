% Please write the Matlab to calculate the DTFT of x[n] and store the DTFT to vector X.
% The plotting code provided below will help you plot DTFT.
signal = [1 1 1 1 1 1 1 1];
n = 0:7; %these are the time indices for the signal vector above
omega = linspace(-pi,pi,1000);

% write your own code here
temp = omega'*n;
temp = -1i*temp;
e = exp(temp);

X = e*signal';

subplot(311)
stem(n,signal);
 
subplot(312)
plot(omega,abs(X),'b');
title('DTFT X[$\omega$]','interpreter','LaTeX','fontsize',14);
xlabel('$\omega$','interpreter','LaTeX','fontsize',14);
ylabel('magnitude of DTFT','fontsize',14);
xlim([-pi pi]);


subplot(313)
plot(omega,angle(X),'g');
grid on;
xlabel('$\omega$','interpreter','LaTeX','fontsize',14);
ylabel('phase of DTFT','fontsize',14);
xlim([-pi pi]);