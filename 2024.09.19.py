konyvtar=[]
with open('konyvtar.txt','r',encoding='utf-8') as forras, \
    open('konyvtar_adat.txt','w',encoding='utf-8') as cel:
    fejletc=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        konyv={'szezo': adat[0], 'cm':adat[1], 'kiadas':adat[2], \
                'IBSN':adat[3],'alapot':adat[4]}
        konyvtar.append(konyv)
        print(konyvtar,file=cel)
    print(f'{konyvtar}')