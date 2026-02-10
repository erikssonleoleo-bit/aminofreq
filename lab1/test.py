import io
import sys
import importlib.util

genetic_code = {
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'AAT': 'N', 'AAC': 'N',
    'GAT': 'D', 'GAC': 'D',
    'TGT': 'C', 'TGC': 'C',
    'CAA': 'Q', 'CAG': 'Q',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'CAT': 'H', 'CAC': 'H',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'TTA': 'L', 'TTG': 'L',
    'AAA': 'K', 'AAG': 'K',
    'ATG': 'M',
    'TTT': 'F', 'TTC': 'F',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'TGG': 'W',
    'TAT': 'Y', 'TAC': 'Y',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
}

start_codons = ["ATG", "TTG", "GTG", "CTG"]

stop_codons = ["TAA", "TGA", "TAG"]

def test(fun,x,y):
    global pass_tests, fail_tests
    if type(x) == tuple:
        z = fun(*x)
    else:
        z = fun(x)
    if y == z:
        pass_tests = pass_tests + 1
    else:
        if type(x) == tuple:
            s = repr(x)
        else:
            s = "("+repr(x)+")"
        print("Condition failed:")
        print("   "+fun.__name__+s+" == "+repr(y))
        print(fun.__name__+" returned/printed:")
        print(str(z))
        fail_tests = fail_tests + 1

def run(src_path=None):
    global pass_tests, fail_tests

    if src_path is None:
        import aminofreq
    else:
        spec_path = src_path + "/aminofreq.py"
        spec = importlib.util.spec_from_file_location("aminofreq", spec_path)
        assert spec is not None, f"failed to load spec from {spec_path}"
        aminofreq = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(aminofreq)

    pass_tests = 0
    fail_tests = 0
    fun_count  = 0

    def composition(identifier,fasta,gencode,startcn,stopcn):
        saved = sys.stdout
        sys.stdout = io.StringIO()
        aminofreq.composition(identifier,fasta,gencode,startcn,stopcn)
        out = sys.stdout.getvalue()
        sys.stdout = saved
        return out

    if hasattr(aminofreq, "codons_extract"):
        fun_count = fun_count + 1
        test(aminofreq.codons_extract, ('GAATGGTGGTCATGAATTAGA',2), ['ATG','GTG','GTC','ATG','AAT','TAG'])
        test(aminofreq.codons_extract, ('ATTATGGCACTGTAA',0), ['ATT', 'ATG', 'GCA', 'CTG', 'TAA'])
        test(aminofreq.codons_extract, ('ATTATGGCACTGTAAG',0), ['ATT', 'ATG', 'GCA', 'CTG', 'TAA'])
        test(aminofreq.codons_extract, ('ATTATGGCACTGTAAGT',0), ['ATT', 'ATG', 'GCA', 'CTG', 'TAA'])
        test(aminofreq.codons_extract, ('ATGGTTGCCTTAGCAGTGA',1), ['TGG', 'TTG', 'CCT', 'TAG', 'CAG', 'TGA'])
        test(aminofreq.codons_extract, ('ATGGTTGCCTTAGCAGTGAG',1), ['TGG', 'TTG', 'CCT', 'TAG', 'CAG', 'TGA'])
        test(aminofreq.codons_extract, ('ATGGTTGCCTTAGCAGTGAGG',1), ['TGG', 'TTG', 'CCT', 'TAG', 'CAG', 'TGA'])
        test(aminofreq.codons_extract, ('ATGGTTGCCTTAGCAGTGAGGT',6), ['GCC', 'TTA', 'GCA', 'GTG', 'AGG'])
        test(aminofreq.codons_extract, ('ATGGTTGCCTTAGCAGTGAGGT',30), [])
        test(aminofreq.codons_extract, ('',9), [])
        test(aminofreq.codons_extract, ('AA',0), [])
    else:
        print("codons_extract is not implemented yet!")

    if hasattr(aminofreq, "protein_extract"):
        fun_count = fun_count + 1
        test(aminofreq.protein_extract, (['ATT','ATG','GCA','CTG','TAA','CTA'],['ATG'],['TAA','TAG']),['ATG','GCA','CTG','TAA'])
        test(aminofreq.protein_extract, (['TGG','TTG','CCT','TAG','CAG','TGA'],['ATG','TTG'],['TAA','TAG','TGA']), ['TTG','CCT','TAG'])
        test(aminofreq.protein_extract, (['CTA','ATG','GTG','GTC','ATG','AAT','TAG','GGT'],['GTG','ATG'],['TAG','TGA']),['ATG','GTG','GTC','ATG','AAT','TAG'])
        test(aminofreq.protein_extract, (['GTG','GCC','TAG','TTG','ATG','TTA','TAG','CCT'],['ATG','GTG'],['TAA','TAG','TGA']), ['GTG','GCC','TAG'])
        test(aminofreq.protein_extract, (['GTT','ATG','TCC','GTA','ACT'],['ATG'],['TAA','TAG','TGA']), [])
        test(aminofreq.protein_extract, (['TGC','CAT','TGA','ATT'],['GTG'],['TAA','TAG','TGA']), [])
        test(aminofreq.protein_extract, (['TAA', 'CTT', 'ATG', 'GCT', 'GTG'],['GTG',],['TAA','TAG','TGA']), [])
        test(aminofreq.protein_extract, (['CCC','CCC','CCC','CCC','ATG', 'GCC', 'TTG', 'TGA','CCC','CCC','CCC','CCC'],['TTG','ATG'],['TAA','TGA']), ['ATG', 'GCC', 'TTG', 'TGA'])
        test(aminofreq.protein_extract, (['TAG', 'ATG', 'ATG'], ['ATG'], ['TAA', 'TAG']), [])
        test(aminofreq.protein_extract, (['TAG', 'ATG', 'TAG'], ['ATG'], ['TAA', 'TAG']), ['ATG', 'TAG'])
        test(aminofreq.protein_extract, (['TAG', 'ATG', 'ATG', 'TAA'], ['ATG'], ['TAA', 'TAG']), ['ATG', 'ATG', 'TAA'])
        test(aminofreq.protein_extract, (['CCC', 'TTG', 'CCC', 'CCC', 'TAA', 'CCC', 'TGA', 'CCC'],[],['TGA','TAA']), [])
        test(aminofreq.protein_extract, (['CCC', 'TTG', 'CCC', 'CCC', 'TAA', 'CCC', 'TGA', 'CCC'],['ATG'],[]), [])
        test(aminofreq.protein_extract, (['CCC', 'TTG', 'CCC', 'CCC', 'TAA', 'CCC', 'TGA', 'CCC'],['ATG','TTG'],[]), [])
        test(aminofreq.protein_extract, (['CCC', 'TTG', 'CCC', 'CCC', 'TAA', 'CCC', 'TGA', 'CCC'],[],[]), [])
        test(aminofreq.protein_extract, ([],['ATG'],['TGA']), [])
        test(aminofreq.protein_extract, (['ATG'],['ATG'],['TGA']), [])
        test(aminofreq.protein_extract, (['TGA'],['ATG'],['TGA']), [])
    else:
        print("protein_extract is not implemented yet!")

    if hasattr(aminofreq, "aa_count"):
        fun_count = fun_count + 1
        test(aminofreq.aa_count, (['ATG','GTG','GTC','ATG','AAT','TAG'], {'ATG': 'M', 'TTT': 'F', 'TTC': 'F', 'GTC': 'V', 'GTG': 'V', 'AAT': 'N', 'AAC': 'N','TAT': 'Y'}), {'M': 2, 'V': 2, 'N': 1})
        test(aminofreq.aa_count, (['ATG','GTG','GTC','ATG','AAT','TAG'], {'ATG': 'M', 'TTT': 'F', 'TTC': 'F', 'GTG': 'V', 'AAT': 'N', 'AAC': 'N','TAT': 'Y'}), {'M': 2, 'V': 1, 'N': 1})
        test(aminofreq.aa_count, (['ATG','TAG','GTC','TTT','TAG'], {'ATG': 'M', 'TTT': 'F', 'TTC': 'F', 'GTC': 'V', 'AAT': 'N', 'AAC': 'N','TAT': 'Y'}), {'M': 1, 'V': 1, 'F': 1})
        test(aminofreq.aa_count, (['ATG','TAG','GTC','TTT','TAG'], {'TTC': 'F', 'GTG': 'V', 'AAT': 'N', 'AAC': 'N','TAT': 'Y'}), {})
        test(aminofreq.aa_count, (['ATG','GTG','GTC','ATG','AAT','TAG'],{}), {})
        test(aminofreq.aa_count, (['ATG','TAG'],{}),{})
        test(aminofreq.aa_count, (['TAG'],{}), {})
        test(aminofreq.aa_count, ([],{}), {})
    else:
        print("aa_count is not implemented yet!")

    if hasattr(aminofreq, "read_dna"):
        fun_count = fun_count + 1
        test(aminofreq.read_dna,('sequence1','examples/example1.fna'), "ATGACATAGAGTGAATGGGATTGAATAACGTTA")
        test(aminofreq.read_dna,('sequence2','examples/example1.fna'), "ATGCCCATTAGTGAATGCATA")
        test(aminofreq.read_dna,('sequence3','examples/example1.fna'), "")
        test(aminofreq.read_dna,('SEQUENCE_1','examples/example2.fna'), "CCGGAAGCCCGTCGACTGGGGTGCAGCTTGGAGTGATGATACAGATGCGGCCAAACGCTGGCTGGCCTTGTCCATCATGGAGCAGTTCCAC")
        test(aminofreq.read_dna,('SEQUENCE_1','examples/example3.fna'), "CCGGAAGCCCGTCGACTGGGGTGCAGCTTGGAGTGATGATACAGATGCGGCCAAACGCTGGCTGGCCTTGTCCATCATGGAGCAGTTCCAC")
        test(aminofreq.read_dna,('SEQUENCE_2','examples/example2.fna'), "CGACCGCCTCAGCTCCTGCAGGGCTGTTCACCTGTCTAGTGGAGGCCAGT")
        test(aminofreq.read_dna,('SEQUENCE_2','examples/example3.fna'), "CGACCGCCTCAGCTCCTGCAGGGCTGTTCACCTGTCTAGTGGAGGCCAGT")
        test(aminofreq.read_dna,('SEQUENCE_3','examples/example3.fna'), "TGCACCAAACATGTAACCAACAAAAACTTTCAAGGCACCTGGCTGTGTATGAAAGGCCCAATTTTGCTGGCCCGGGGCGAGTATAT")
        test(aminofreq.read_dna,('seq','examples/gibberish.fna'), "")
    else:
        print("read_dna is not implemented yet!")

    if hasattr(aminofreq, "composition"):
        fun_count = fun_count + 1
        test(composition, ('SEQUENCE_4','examples/example4.fna',genetic_code,start_codons,stop_codons), 'Error: the sequence is not in the file\n')
        test(composition, ('SEQUENCE_1','examples/example4.fna',genetic_code,start_codons,stop_codons), 'Frame 0:\nprotein: [\'CTG\', \'GGG\', \'TGC\', \'AGC\', \'TTG\', \'GAG\', \'TGA\']\namino acid count: {\'L\': 2, \'G\': 1, \'C\': 1, \'S\': 1, \'E\': 1}\nFrame 1: no valid protein\nFrame 2: no valid protein\n')
        test(composition, ('SEQUENCE_2','examples/example4.fna',genetic_code,start_codons,stop_codons), 'Frame 0: no valid protein\nFrame 1:\nprotein: [\'CTG\', \'CAG\', \'GGC\', \'TGT\', \'TCA\', \'CCT\', \'GTC\', \'TAG\']\namino acid count: {\'L\': 1, \'Q\': 1, \'G\': 1, \'C\': 1, \'S\': 1, \'P\': 1, \'V\': 1}\nFrame 2: no valid protein\n')
        test(composition, ('SEQUENCE_3','examples/example4.fna',genetic_code,start_codons,stop_codons), 'Frame 0: no valid protein\nFrame 1: no valid protein\nFrame 2:\nprotein: [\'ATG\', \'TAA\']\namino acid count: {\'M\': 1}\n')
    else:
        print("composition is not implemented yet!")

    print(str(pass_tests)+" out of "+str(pass_tests+fail_tests)+" passed.")

    return (fun_count == 3 and fail_tests == 0)

if __name__ == "__main__":
    dirname = sys.argv[1] if len(sys.argv) > 1 else None
    run(dirname)
