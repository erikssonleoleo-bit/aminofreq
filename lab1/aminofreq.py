def codons_extract(dna,n):
    segment = []
    for i in range(0,len(dna),3):
        segment.append(dna[n+i:n+i+3])
    Codon = [k for k in segment if len(k) >= 3]
    print("Codons:",Codon)
    return Codon





def helper(hela_listan,start,stop):
    plats_start = "A"
    plats_stop = "A"
    for i in hela_listan:
        Finns_Start = False
        Finns_Stop = False
        if i in start:
            Finns_Start = True
        if i in stop:
            Finns_Stop = True
        if Finns_Start:
            plats_start = hela_listan.index(i)
            print("Plats start:" , plats_start) 
        if Finns_Stop:
            plats_stop = hela_listan.index(i) + 1
            print("PLats stop:" , plats_stop)
    return plats_start , plats_stop








def protein_extract(hela_listan,start,stop):
    lista = [helper(hela_listan,start,stop)]
    print("Lista" , lista)
    plats_1_tuple = lista[0]
    plats_2_tuple = lista[-1]
    plats_1 = plats_1_tuple[0]
    plats_2 = plats_2_tuple[-1]
    print("PLats 1 och 2 Tuple:" , plats_1_tuple , plats_2_tuple)
    print("PLats 1 och 2 :" , plats_1 , plats_2)
    if "A" == plats_1 or "A" == plats_2:
        ny_lista = []
        print("Tom lista" , ny_lista)
        return ny_lista
    else:
        ny_lista = hela_listan[plats_1 : plats_2]
        print("plats_1 :", plats_1 , " plats_2", plats_2 , "ny_lista", ny_lista)








protein_extract(['TGG','TTG','CCT','TAG','CAG','TGA'],['ATG','TTG'],['TAA','TAG','TGA'])


def aa_count(start_slut,dictionary):
    dictionary = {'ATG':'M','TTT':'F','TTC':'F','GTC':'V','GTG':'V','AAC':'N','TAT':'Y'}
    gen = start_slut
    ny_gen = [dictionary.get(i,i) for i in gen]
    print(ny_gen)
    antal_M = ny_gen.count("M")
    antal_V = ny_gen.count("V")
    antal_F = ny_gen.count("F")
    antal_N = ny_gen.count("N")
    antal_Y = ny_gen.count("Y")
    print("M:",antal_M,"V:",antal_V,"F:",antal_F,"N:",antal_N,"Y:",antal_Y)
        
     
        



def a_count(start_slut,dic):
    gen = start_slut
    for i in dic:
        print (dic[i])


