
[Tw,TEXT]=xlsread('STATION1.xlsx','DATA',  'D2:D10221');  
X1= Tw;
Nstd = 0.2;
NR = 100;
MaxIter = 500;
[modes]= eemd(X1,Nstd,NR,MaxIter);
modes
t=1:length(X1);
[a b]=size(modes)

Y= modes'; 

xlswrite('STATION1.xlsx',[Y] ,'DATA','I2');

figure;
subplot(a+1,2,1);
plot(t,X1);% the ECG signal is in the first row of the subplot
ylabel('Ta(°C)')
set(gca,'xtick',[])
axis tight;

for i=2:a
    subplot(a+1,2,i);
    plot(t,modes(i-1,:));
    ylabel (['IMF ' num2str(i-1)]);
    set(gca,'xtick',[])
    xlim([1 length(X1)])
end;

    t=1:length(X1);
    plot(t,res(:,1))
    ylabel(['Residual '])
    axis tightsubplot(mp+2,1,mp+2)
  
