N = 8;
n = 0:N-1;

for k = n;
    
    x = exp( 1j* (2*pi/N) * k * n);
    subplot(8,2,2*k+1)
    stem(n,real(x),'b','fill','LineWidth',2); hold on
    str = sprintf('k=%d',k); ylabel(str,'interpreter','Latex','fontsize',14);
    aa = axis; axis([0,7,-1,1]);
    
    subplot(8,2,2*k+2)
    stem(n,imag(x),'r','fill','LineWidth',2); hold off
    aa = axis; axis([0,7,-1,1]);
    
end

subplot(821)
title('${ Re}(e^{j \frac{2\pi}{8}}) = \cos({\frac{2\pi}{8}})$','interpreter','Latex','fontsize',18);

subplot(822)
title('${ Im}(e^{j \frac{2\pi}{8}}) = \sin({\frac{2\pi}{8}})$','interpreter','Latex','fontsize',18);