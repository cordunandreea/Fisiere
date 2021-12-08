with open('c:/Users/user/Desktop/Lista clasei 11C.txt', 'r', encoding="utf-8") as f:
    x=f.read()
fr=0
en=0
note_fr=0
note_en=0
for i in x.split('\n'):
    o=i.split()
    if str(o[3])=='franceza':
        note_fr.append(o[2]), fr.append(o)
    with open('c:/Users/user/Desktop/11C franceza.txt', 'w', encoding="utf-8") as f:
            for d in range(0, len(str(fr))):
                for g in range(0, len(str(fr))):
                    f.write(str(fr)+str(' '))
                    f.write()
            f.write('media:',sum(note_fr)/len(note_fr))
    if str(o[3])=='engleza':
        note_en.append(o[2]), en.append(o)
    with open('c:/Users/user/Desktop/11C engleza.txt', 'w', encoding="utf-8") as f:
            for p in range(0, len(str(en))):
                for w in range(0, len(str(en))):
                    f.write(str(en)+str(' '))
                    f.write()
            f.write('media:',sum(note_en)/len(note_en))