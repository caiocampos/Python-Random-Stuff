def to_rna(dna_strand):
    rna = []
    for nuc in dna_strand:
        if nuc == 'G':
            rna.append('C')
        elif nuc == 'C':
            rna.append('G')
        elif nuc == 'T':
            rna.append('A')
        elif nuc == 'A':
            rna.append('U')
    return "".join(rna)
