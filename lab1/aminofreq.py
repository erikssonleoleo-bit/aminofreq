def codons_extract(dna,n):
    segment = []
    for i in range(0,len(dna),3):
        segment.append(dna[n+i:n+i+3])
    Codon = [k for k in segment if len(k) >= 3]
    return Codon





def helper(hela_listan,start,stop):
    plats_start = "A"
    plats_stop = "A"
    Finns_Start = False
    Finns_Stop = False
    for i in range(len(hela_listan)):
        if hela_listan[i] in start:
            Finns_Start = True
            plats_start=i
            break
    if not Finns_Start:
        return plats_start , plats_stop
                
    for j in range(plats_start +1, len(hela_listan)):
            if hela_listan[j] in stop:
                Finns_Stop = True
                plats_stop = j
                break
    if not Finns_Stop:
        return "A", "A"
    return plats_start, plats_stop
    



def protein_extract(hela_listan,start,stop):
    lista = [helper(hela_listan,start,stop)]
        # print("test 3", lista)
    plats_1_tuple = lista[0]
    plats_2_tuple = lista[-1]
    plats_1 = plats_1_tuple[0]
    plats_2 = plats_2_tuple[-1]
        # print("test 2", plats_1, plats_2)
    if "A" == plats_1 or "A" == plats_2:
        ny_lista = []
    else:
        ny_lista = hela_listan[plats_1 : plats_2+1]
    return ny_lista


def aa_count(codons, genetic_code):
    counts={}
    for c in codons:
        if c in genetic_code:
            aa=genetic_code[c]
            if aa in counts:
                counts[aa]=counts[aa]+1
            else:
                counts[aa]=1
    return counts





#rader = file.readlines()


#def read_dna1(string_name, filename):
    Ihop = ""
    Hittad = False
    with open(filename, 'r') as file:
        rader = file.readlines()
        print("Rader: ", rader)
        for rad in file:
        #for k in rader:
            rad = rad.strip()
            #print("Rad: ", rad)
            if '>' + string_name +'\n' in rader:
                Hittad = True
                rad = next(file)
                print("Hittad = True")
            if Hittad:
                if rad.startswith('>'):
                    print("Breakar_första")
                    break
                else:            
                    Ihop += rad
                    if rad.startswith('>'):
                        print("Breakar_andra")
                        break
            if not Hittad:
                print("If not Hittad", "'  '")
    #print("Ihop_1: ", Ihop)
    Stora = Ihop.upper()
    print("Svar: ", Stora)


def read_dna(string_name, filename):
    Ihop = ""
    Hittad = False
    identifier = '>'+ string_name
    with open(filename, 'r') as file:
        rader = file.readlines()
        for i, rad in enumerate(rader):
            if rad.startswith(identifier):
                Hittad = True
            if Hittad:
                if i+1 >= len(rader):
                    break
                rad = rader[i+1]
                rad.strip()
                if rad.startswith('>'):
                    break
                Ihop += rad
        if not Hittad:
                print("''")
    Stora = Ihop.upper()
    Svar = Stora.replace("\n","")
    print("Svar", Svar)
    return Svar
    


 





        





    



read_dna('sequence2','examples/example1.fna')