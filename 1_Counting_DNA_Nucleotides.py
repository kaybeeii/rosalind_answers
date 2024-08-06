#Given DNA string up to 1000 bp
#Return number of times 'A', 'C', 'G', 'T' occur

DNA = ('CTGAATTGAGTTTTAGCACCAAATCGGGCCCCGGGTTGGTTCGCTTTGTTAGGTCTCTGCTGTAACGTGTTTCCCTAGTTGAATCACGCCACACTCCGCGGGTAGGGTGGCGATGACACCGGAGGTACCGACCTAGAGGTTGCCTGCCAACTGGCGCTGAGTCGAGAGGTTTCGAACAGAAAGACATCCGACAATGGACTCGGGCACCTCGGGTCCATCCTGACACCGAATGAGGACTAATTATCTTGCTGATGACATTTTTCAGTCAGAAACCGGCCTTACCAGTGGATGATCTGTTTCCGGTTTAAAACGACTCTGGGCCGCATCTCGTACTCTACCACAATAGTGCACCGCTATGCTCGCCAAACGTACGAGACCTTTCATCGGGGCCCGATACAAGACTGCGTACAAAATTCAACGGCATATCGATAGTACGAGTCAACGTGCTTTCCTGGCGAGTTTCGGTTCCAGCGTGTGCGGTGCCGGCTGAGTAGGGGTTGTCAAAGCCCACTCTGTCTACAACAGCGCTTCCTCGCGCCATTTAGCAGTCCATCCAGGATTCTACCCGGATAAGGACTTCTTACCTATCTGTTGGTTTTGCCCGGGTGCCTGGCTGTTGATTCGTACACGTAAAGACTCCCGCCCACTTGCGTCTTGCTTGTTGATCTACGAACCGCTGTAGTCTATCATAGATTTGACAGCTTGTATTGGGGGGCTCCCGTCACGCTTTGACGAGCGATCTTGGACCCACTCATCGTGTATCAGGCAGGACACGCACTAGAGGAGGGCTGTTAAGGGCCGTTGAACGAAAATCTGGAATTCACACTGGTGACACAAGTCTCAATTCAGCACTCTCCCGAAAATGGGCCCGCTGACCAACTCTTCGCCTGGCACCCCTAGCAAAACTATTTTAACGTCGAGACGTTCACGACCAGCTTAGTT')
print(DNA.count('A'), DNA.count('C'), DNA.count('G'), DNA.count('T'))

#Output: 210 257 237 238