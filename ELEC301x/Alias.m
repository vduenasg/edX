w=9*pi/4;  % <-- enter a different value of w which produces the same plot as the above plot

%%%%%%%%%%%%%%%%% DO NOT MODIFY THE FOLLOWING CODE %%%%%%%%%%%%%%%%%

% Generate a vector with discrete time values
n=0:1:7;
  
% Generate a vector with signal values
x=sin(w.*n);
  
% Plot and annotate the signal
stem(x);
xlabel('n');
title('x[n] with \omega value provided by you');
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%