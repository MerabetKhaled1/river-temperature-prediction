
mp=09;
[Tw,TEXT]=xlsread('STATION1.xlsx','DATA',  'D2:D10221');   
X1= Tw;
wecg=X1;
[imf,res] = emd(X1,'MaxNumIMF',mp,'Display',1);
 
t=1:length(X1);
Y= [imf]
Y1= [imf, res]
tiledlayout('flow')
subplot(mp+2,1,1)
    t=1:length(X1);
    plot(t,wecg(:,1))
    ylabel(['Ta (°C)'])
    axis tight

for k=2:mp+1
    subplot(mp+2,1,k)
    plot(t,Y1(:,k-1))
    ylabel(['IMF ',num2str(k-1)])
    axis tight
end
    subplot(mp+2,1,mp+2)
    t=1:length(X1);
    plot(t,res(:,1))
    ylabel(['Residual '])
    axis tight

    Y= imf'; 
  Y1= res';
  [Y' Y1'];
xlswrite('STATION1.xlsx',[Y' Y1'] ,'DATA','K2');
