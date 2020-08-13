clear all; close all; startup;

%-------
coord = load('ensomerge_atm_djf_fortaylor_2ndrun.txt','-ascii');
% x = a cos(alpha)
x = coord(:,1).*coord(:,2);
% y = sqrt(a^2-x^2)
y = sqrt(coord(:,1).^2-x.^2);
%
scrsz = get(0,'ScreenSize');
%[left, bottom, width, height]
figure('Position',[1 scrsz(4)/2 scrsz(3)/2.8 scrsz(4)/2.2]);
figure(1),clf
%plot(x,y,'ko','LineWidth',4)
plot(x,y,'k.','MarkerSize',12)
set(gca,'box','off')
hold on;
plot(x(end),y(end),'ko','MarkerSize',12,'MarkerFaceColor',[0/255,0/255,0/255])
%
ang=0:0.01:pi; 
r = 1.0;
xp=r*cos(ang);
yp=r*sin(ang);
plot(xp,yp,'-','color',[0,0,0]+0.6)
axis([-1 2.5 0 2.5]);
set(gca,'Xtick',[-1,-0.5,0,0.5,1,1.5,2,2.5]);
ax = gca;
ax.YAxisLocation = 'origin';
set(gca,'YTickLabel',[]);
ax.TickLength = [0.02, 0.02]; % Make tick marks longer.

% calculate and plot 5th and 95th percentiles for cosalpha
prc=prctile(coord(1:end-1,2),95);
prc95=prc;
x=[0 4.*prc];
y=[0 sqrt(4.^2-(4.*prc).^2)];
plot(x,y,'-','color',[205/255,92/255,92/255])
x=2.*prc;
y=sqrt(2.^2-(2.*prc).^2);
textd=sprintf('%.2f',prc);
text(x+0.02,y-0.1,textd,'FontSize',38,'color',[205/255,92/255,92/255]);
%
prc=prctile(coord(1:end-1,2),5);
prc5=prc;
x=[0 4.*prc];
y=[0 sqrt(4.^2-(4.*prc).^2)];
plot(x,y,'-','color',[70/255,130/255,180/255])
x=2.2*prc;
y=sqrt(2.2^2-(2.2*prc).^2);
textd=sprintf('%.2f',prc);
text(x+0.02,y-0.08,textd,'FontSize',38,'color',[70/255,130/255,180/255]);
% plot thicker arc spanning 5th and 95th percentiles for cosalpha
ang=acos(prc95):0.01:acos(prc5); 
r = 1.0;
xp=r*cos(ang);
yp=r*sin(ang);
plot(xp,yp,'-','color',[0,0,0]+0.6,'LineWidth',14)
% calculate and plot median for cosalpha
med=median(coord(1:end-1,2));
x=[0 4.*med];
y=[0 sqrt(4.^2-(4.*med).^2)];
plot(x,y,'-','color',[34/255,139/255,34/255])
x=2.2*med;
y=sqrt(2.2^2-(2.2*med).^2);
textd=sprintf('%.2f',med);
text(x+0.02,y-0.1,textd,'FontSize',38,'color',[34/255,139/255,34/255]);

% calculate and plot 5th and 95th percentiles for r
prc=prctile(coord(1:end-1,1),95);
ang=0:0.01:pi; 
r = prc;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[205/255,92/255,92/255])
x=r*cos(pi*2.6/4);
y=r*sin(pi*2.6/4);
textd=sprintf('%.2f',prc);
text(x+0.02,y-0.08,textd,'FontSize',38,'color',[205/255,92/255,92/255]);
%
prc=prctile(coord(1:end-1,1),5);
ang=0:0.01:pi; 
r = prc;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[70/255,130/255,180/255])
x=r*cos(pi*3/4);
y=r*sin(pi*3/4);
textd=sprintf('%.2f',prc);
text(x-0.05,y-0.12,textd,'FontSize',38,'color',[70/255,130/255,180/255]);
% calculate and plot median for r
med=median(coord(1:end-1,1));
ang=0:0.01:pi; 
r = med;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[34/255,139/255,34/255])
x=r*cos(pi*2.8/4);
y=r*sin(pi*2.8/4);
textd=sprintf('%.2f',med);
text(x-0.05,y-0.12,textd,'FontSize',38,'color',[34/255,139/255,34/255]);
hold off;

%-------
coord = load('ensomerge_atm_djf_fortaylor_perm_long.txt','-ascii');
% x = a cos(alpha)
x = coord(:,1).*coord(:,2);
% y = sqrt(a^2-x^2)
y = sqrt(coord(:,1).^2-x.^2);
%
scrsz = get(0,'ScreenSize');
%[left, bottom, width, height]
figure('Position',[1 scrsz(4)/2 scrsz(3)/2.8 scrsz(4)/2.2]);
figure(2),clf
%plot(x,y,'ko','LineWidth',4)
plot(x,y,'k.','MarkerSize',12)
set(gca,'box','off')
hold on;
plot(x(end),y(end),'ko','MarkerSize',12,'MarkerFaceColor',[0/255,0/255,0/255])

%
ang=0:0.01:pi; 
r = 1.0;
xp=r*cos(ang);
yp=r*sin(ang);
plot(xp,yp,'-','color',[0,0,0]+0.6)
%axis([-1 2.5 0 2.5]);
%set(gca,'Xtick',[-1,-0.5,0,0.5,1,1.5,2,2.5]);
axis([-1.5 2. 0 2.5]);
set(gca,'Xtick',[-1.5,-1.0,-0.5,0,0.5,1,1.5,2.0]);
ax = gca;
ax.YAxisLocation = 'origin';
set(gca,'YTickLabel',[]);
ax.TickLength = [0.02, 0.02]; % Make tick marks longer.
% plot thicker arc spanning 5th and 95th percentiles for cosalpha
ang=acos(prc95):0.01:acos(prc5); 
r = 1.0;
xp=r*cos(ang);
yp=r*sin(ang);
plot(xp,yp,'-','color',[0,0,0]+0.6,'LineWidth',14)
%calculate and plot 5th and 95th percentiles for cosalpha
prc=prctile(coord(1:end-1,2),95);
x=[0 4*prc];
y=[0 sqrt(4^2-(4*prc).^2)];
plot(x,y,'-','color',[205/255,92/255,92/255])
x=1.7*prc;
y=sqrt(1.7^2-(1.7*prc).^2);
textd=sprintf('%.2f',prc);
text(x+0.04,y-0.1,textd,'FontSize',38,'color',[205/255,92/255,92/255]);
%
prc=prctile(coord(1:end-1,2),5);
x=[0 4*prc];
y=[0 sqrt(4^2-(4*prc).^2)];
plot(x,y,'-','color',[70/255,130/255,180/255])
x=1.8*prc;
y=sqrt(1.8^2-(1.8*prc).^2);
textd=sprintf('%.2f',prc);
text(x+0.04,y-0.0,textd,'FontSize',38,'color',[70/255,130/255,180/255]);
% calculate and plot median for cosalpha
med=median(coord(1:end-1,2));
x=[0 4.*med];
y=[0 sqrt(4.^2-(4.*med).^2)];
plot(x,y,'-','color',[34/255,139/255,34/255])
x=1.9*med;
y=sqrt(1.9^2-(1.9*med).^2);
textd=sprintf('%.2f',med);
text(x+0.0,y-0.1,textd,'FontSize',38,'color',[34/255,139/255,34/255]);

% here something else
%
% x = a cos(alpha)
x = coord(:,1).*coord(:,2);
% y = sqrt(a^2-x^2)
y = sqrt(coord(:,1).^2-x.^2);
%
%i=find(coord(1:end-1,1)>1. & coord(1:end-1,2)>=0.67);
%xsel=x(i); ysel=y(i);
%plot(xsel,ysel,'ro','LineWidth',4,'MarkerFaceColor','r')
k=find(coord(1:end-1,1)>=1.);
xsel=x(k); ysel=y(k);
plot(xsel,ysel,'ro','LineWidth',4,'MarkerFaceColor','r')

% calculate and plot 5th and 95th percentiles for r
prc=prctile(coord(1:end-1,1),95);
ang=0:0.01:pi; 
r = prc;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[205/255,92/255,92/255])
x=r*cos(pi*2.6/4);
y=r*sin(pi*2.6/4);
textd=sprintf('%.2f',prc);
text(x+0.08,y-0.04,textd,'FontSize',38,'color',[205/255,92/255,92/255]);
%
prc=prctile(coord(1:end-1,1),5);
ang=0:0.01:pi; 
r = prc;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[70/255,130/255,180/255])
x=r*cos(pi*3.0/4);
y=r*sin(pi*3.0/4);
textd=sprintf('%.2f',prc);
text(x-0.02,y-0.1,textd,'FontSize',38,'color',[70/255,130/255,180/255]);
% calculate and plot median for r
med=median(coord(1:end-1,1));
ang=0:0.01:pi; 
r = med;
x=r*cos(ang);
y=r*sin(ang);
plot(x,y,'-','color',[34/255,139/255,34/255])
x=r*cos(pi*2.5/4);
y=r*sin(pi*2.5/4);
textd=sprintf('%.2f',med);
text(x-0.02,y-0.1,textd,'FontSize',38,'color',[34/255,139/255,34/255]);

hold off;

