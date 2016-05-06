%%%
N = 120;
n = 0:N-1;
x0 = [zeros(10,1); ones(100,1); zeros(10,1)];
x0 = x0/norm(x0);
x1 = [zeros(10,1); ones(50,1); -ones(50,1); zeros(10,1)];
x1 = x1/norm(x1);
signals=[x0,x1];
subplot(311)
stem(n,x0,'b','Marker','none','LineWidth',1)
title('Signal x0 - Transmit to send a digital 0','fontsize',18)
subplot(312)
stem(n,x1,'r','Marker','none','LineWidth',1)
title('Signal x1 - Transmit to send a digital 1','fontsize',18)

% received signal is either x0 or x1 with additive noise
y = signals(:,round(rand(1,1))+1) + 0.2*randn(size(x1));

subplot(313)
stem(n,y,'k','Marker','none','LineWidth',1)
title('Received signal - Was it a 0 or 1?','fontsize',18)

% computes the inner products between y and both x0 and x1:
innerproduct0 = abs( y' * x0 )
innerproduct1 = abs( y' * x1 )

 
%%%%
%%%% Write code below that stores a 0 or 1 into RECEIVEDBIT
%%%% based upon whether x0 or x1 was the more likely transmission
%%%% (hint: it should only take one or two lines of code)
if innerproduct0>innerproduct1
    RECEIVEDBIT=0
else
    RECEIVEDBIT=1
end
 