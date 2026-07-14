#DNA sequence
dna = "ATGCGTAACG"
print("DNA Sequence:", dna)

#Find DNA length
length = len(dna)

print("DNA Length:", length)

#DNA Indexing
first_base = dna[0]
last_base = dna[-1]

print("First Base:", first_base)
print("Last Base:", last_base)

#DNA Slicing
part = dna[0:5]
print("First 5 Bases:", part)

#Count Bases
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("A Count:", a_count)
print("T Count:", t_count)
print("G Count:", g_count)
print("C Count:", c_count)

#Dictionary Report

report = {
    "sequence": dna,
    "length": length,
    "A": a_count,
    "T": t_count,
    "G": g_count,
    "C": c_count,
}
print(report)


#Print Report

for key, value in report.items():
    print(key, ":", value)

#DNA to RNA

rna = dna.replace("T", "U")
print("RNA Sequence:", rna)

#Final Output
print("DNA Analysis Completed")

#DNA as list

base_list = list(dna)
print("DNA List:", base_list)

#Print each base
for base in base_list:
    print(base)

#Tuple Information
gene_info = ("BRCA1", "HUMAN", 17)
print("Gene Info:", gene_info)

#Tuple Indexing
print("Gene Name:", gene_info[0])
print("Organism:", gene_info[1])

#Unique Bases
unique_bases = set(dna)
print("Unique Bases:", unique_bases)

#Final
print("DNA Analysis Completed Successfully")


    

     
