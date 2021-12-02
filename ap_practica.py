f=open('c:/Users/Statie-7-C100/Desktop/Lista clasei 11C.txt','r', encoding="utf-8")
lista=list(f)
print('\tNume', 'Prenume', 'Nota', 'Limba Straina', sep='\t')
#for l in lista:    col=l.split()    print(col[0],col[1],col[2],col[3],sep='\t')
print(f.read())
f.close()
for i, linie in enumerate(lista):
    print(i+1, ':', linie, end='')