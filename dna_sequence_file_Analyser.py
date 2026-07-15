#DNA SEQUENCE FILE ANALYSER

#Function using def
def show_sequence(sequence):
    print("DNA Sequence:", sequence)

#Function with argument and return
def get_length(sequence):
    return len(sequence)

#Another function with argument and return
def count_a(sequence):
    return sequence.count("A")

#Lamda function
count_g = lambda sequence: sequence.count("G")

#Function calls
dna = "ATGCGTAA"

show_sequence(dna)

length = get_length(dna)
print("DNA Length:", length)

a_count = count_a(dna)
print("A Count:", a_count)

print("G Count:", count_g(dna))


#FILE HANDLING

#Write mode
with open("dna.txt", "w") as file:
    file.write(dna)
print("DNA written to file")

#Append mode
with open("dna.txt", "a") as file:
    file.write("\nGCTA")
print("New DNA sequence appended")

#Read full file using read()
with open("dna.txt", "r") as file:
    data = file.read()
print("\nFull File Content:")
print(data)

#Read one line using readline()
with open("dna.txt", "r") as file:
    first_line = file.readline()
print("\nFirst Line:")
print(first_line)

#Read all lines as a list using readlines()
with open("dna.txt", "r") as file:
    all_lines = file.readlines()
print("All Lines as List:")
print(all_lines)

#File with loop
print("\nSequences One by One:")

with open("dna.txt", "r") as file:
    for sequence in file:
        print(sequence.strip())

#Normal open() and close()
file = open("dna.txt", "r")
final_data = file.read()
file.close()

print("/nFinal Data:")
print(final_data)

print("\n=== ANALYSIS COMPLETED ===")
