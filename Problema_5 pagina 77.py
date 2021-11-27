f=open(r'C:\Users\user\Desktop\CARACTERE.txt','w')
intrare=str(input('introduceti un sir de caractere aleatoriu de la tastatura:'))
f.write(intrare)
f.close()

f=open(r'C:\Users\user\Desktop\CARACTERE.txt','r')
x=f.read()
f.close()
print(x)

vocal=0
for i in range(0, len(x)):
    if x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='u' or x[i]=='o':
        vocal=vocal+1

f=open(r'C:\Users\user\Desktop\VOCALE.txt', 'w')
f.write(str(vocal))
f.close