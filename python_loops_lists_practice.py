#List Creation
samples = ["DNA1", "DNA2", "DNA3", "DNA4", "DNA5"]
print("My DNA Samples:")
print(samples)

#Indexing
print("\nIndexing:")
print("First sample:", samples[0])
print("Third sample:", samples[2])

#Negative Indexing
print("\nNegative Indexing:")
print("Last sample:", samples[-1])
print("Second last sample:", samples[-2])

#Slicing + Step + Reverse Slicing
#Slicing
print("\nSlicing:")
print("First three sample:", samples[0:3])
print("From second sample:", samples[1:])

#Slicing with Step
print("\nSlicing with Step:")
print("Every second sample:", samples[::2])

#Reverse Slicing
print("\nReverse Slicing:")
print("Reverse sample:", samples[::-1])

#List Methods

#append()
print("\nAppend Method:")

genes = ["BRCA1", "TP53"]
print("Before:", genes)

genes.append("EGFR")
print("After append:", genes)

#insert()
print("\nInsert Method:")

genes.insert(1, "MYC")
print("After insert:", genes)

#extend()
print("\nExtend Method:")

genes.extend(["KRAS", "BRAF"])
print("After extend:", genes)

#remove()
print("\nRemove Method:")

genes.remove("MYC")
print("After remove:", genes)

#pop()
print("\npop Method:")

removed_gene = genes.pop(2)

print("Removed:", removed_gene)
print("After pop:", genes)

#sort()
print("\nSort Method:")

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)

#reverse()
print("\nReverse Method:")

samples = ["DNA1" "DNA2", "DNA3"]

samples.reverse()

print("Reverse:", samples)

#clear()
print("\nClear Method:")
temp = ["A", "B", "C"]
temp.clear()
print("After clear:", temp)

#Nested list
genes_group = [
    ["BRCA1", "TP53"],
    ["EGFR", "KRAS"]
]
print("\nNested List:")
print(genes_group)
print("First group:", genes_group[0])
print("TP53:", genes_group[0][1])
print("KRAS:", genes_group[1][1])

#Nested list change + add
genes_group[0][1] = "MYC"
print("\nAfter Cgange:")
print(genes_group)

#add item
genes_group[1].append("BRAF")
print("\nAfter Add:")
print(genes_group)

#list with loop
print("\nLoop Practice:")
samples = ["DNA1", "DNA2", "DNA3"]
for sample in samples:
    print(sample)

#list + loop + if
lengths = [100, 250, 50, 300]
for length in lengths:
    if length >= 200:
        print(length, "High quality")
    else:
        print(length, "Low quality")





