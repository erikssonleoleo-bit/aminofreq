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
    plats_1_tuple = lista[0]
    plats_2_tuple = lista[-1]
    plats_1 = plats_1_tuple[0]
    plats_2 = plats_2_tuple[-1]
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








def read_dna(string_name, filename):
    Svar = ""
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
            Svar += rad
    if not Hittad:
        Svar = ""
    Svar = Svar.upper()
    Svar = Svar.replace("\n","")
    return Svar
    

def composition(string_name, filename,genetic_code , start, stop):

    for n in range(3):
        Hela_DNA_sequence = read_dna(string_name, filename)
        Uppdelat_DNA = codons_extract(Hela_DNA_sequence, n)
        DNA_sequence = protein_extract(Uppdelat_DNA, start, stop)
        Dict_med_antal = aa_count(DNA_sequence, genetic_code)
        if Hela_DNA_sequence == '':
            print('Error: the sequence is not in the file')
            break
        elif len(DNA_sequence) == 0:
            print(f"Frame {n}: no valid protein")
        else:
            print(f"Frame {n}:\nprotein: {DNA_sequence}\namino acid count: {Dict_med_antal}")













        





    



