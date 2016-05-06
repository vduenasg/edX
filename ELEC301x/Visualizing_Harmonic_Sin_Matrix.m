N = 8;
n = 0:N-1;

for k = n;
    D(:,k+1) = exp( 1j*(2*pi/N) * k * n).';
    
end

clf
subplot(121)
imagesc(n,n,real(D)); axis('square')
xlabel('$k$','interpreter','Latex','fontsize',18);
ylabel('$n$','interpreter','Latex','fontsize',18);
title('${ Re}(e^{j \frac{2\pi}{8}}) = \cos({\frac{2\pi}{8}})$','interpreter','Latex','fontsize',18);
colorbar

subplot(122)
imagesc(n,n,imag(D)); axis('square')
xlabel('$k$','interpreter','Latex','fontsize',18);
ylabel('$n$','interpreter','Latex','fontsize',18);
title('${Im}(e^{j \frac{2\pi}{N}}) = \sin({\frac{2\pi}{N}})$','interpreter','Latex','fontsize',18);
colorbar