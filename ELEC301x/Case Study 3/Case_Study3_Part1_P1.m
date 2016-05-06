clear all;
close all;
a = [1 2 3 4 5 6;  7 8 9 10 11 12];
b = norm(a,2);
c = a/b;
for i=1:6
    d(:,i)=a(:,i)/norm(a(:,i),2);
end
c
d
