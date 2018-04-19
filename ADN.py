

import os


acido_nucleico = input("Enter D to convertir to DNA or R to convert to RNA")

if acido_nucleico.lower()=="r":
    dna = []
    data = input("Press Enter to add a DNA nucleobase  Enter  EXIT to exit ")
    while data == "":
        nucleobase = input("Enter  A for Adenine, C for Cytosine, G for Guanine, or T for Thymine")
        dna.append(nucleobase.upper())
        data = input("Press Enter to add another DNA nucleobase Enter EXIT if you are finished")
    rna = dna[:]
    while "T" in rna:
        rna[rna.index("T")] = "U"

if acido_nucleico.lower() == "d":
    rna =[]
    data = input("Press ENTER to add an RNA nucleobase. enter EXIT to exti")
    while data == "":
        nucleobase = input("Enter A for Adenine, C for Cytosine, G for Guanine, or U for Uracil.")
        data = input("Press ENTER to add another RNA nucleobase. Enter EXIT if you are finished")
        rna.append(nucleobase.upper())
        data = input("Press ENTER to add another RNA nucleobase. ENTER exit if you are finished")
    dna = rna[:]
    while "U" in dna:
        dna[dna.index("U")] = "T"

os.system('cls')
print("Here is your bioimformatical report:")
print()
print("Your DNA sequence")
print(rna)