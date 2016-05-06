%Create the row vector u
%Create the column vector v
%Create the Matrix A
%Find the column vector x
u = [2 5 0 4];
t = [5.1 5.2 4.2 1.3];
t = t';
v = u' + t;
A = [2 4 7 2; 4 5 10 4; 9 4 1 1; 0 1 6 7];
x = inv(A)*v