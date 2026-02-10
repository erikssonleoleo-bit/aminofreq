def codons_extract(dna,n):
    segment = []
    for i in range(0,len(dna),3):
        segment.append(dna[n+i:n+i+3])
    Codon = [k for k in segment if len(k) >= 3]
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
        if Finns_Stop:
            plats_stop = hela_listan.index(i) + 1
            break
    return plats_start , plats_stop








def protein_extract(hela_listan,start,stop):
    lista = [helper(hela_listan,start,stop)]
    print("test 3", lista)
    plats_1_tuple = lista[0]
    plats_2_tuple = lista[-1]
    plats_1 = plats_1_tuple[0]
    plats_2 = plats_2_tuple[-1]
    print("test 2", plats_1, plats_2)
    if "A" == plats_1 or "A" == plats_2:
        ny_lista = []
    else:
        ny_lista = hela_listan[plats_1 : plats_2]
    return ny_lista










     
        



def a_count(start_slut,dic):
    gen = start_slut
    for i in dic:
        print (dic[i])
print("Test:",protein_extract(['TAG', 'ATG', 'TAG'], ['ATG'], ['TAA', 'TAG']))



