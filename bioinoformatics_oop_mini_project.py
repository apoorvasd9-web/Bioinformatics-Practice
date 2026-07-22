# ============================================
# Bioinformatics Mini Project
# Created by: Apoorva
# ============================================

class BioSample:

    # Class Variable
    lab = "Genome Research Lab"

    def __init__(self, sample_id, sequence):
        # Instance Variables
        self.sample_id = sample_id
        self.sequence = sequence

    # Instance Method
    def show_details(self):
        print("\n------ Sample Details ------")
        print("Lab       :", BioSample.lab)
        print("Sample ID :", self.sample_id)
        print("Sequence  :", self.sequence)

    # Instance Method
    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        percent = (gc / len(self.sequence)) * 100
        print("GC Content: {:.2f}%".format(percent))

    # Class Method
    @classmethod
    def change_lab(cls, new_lab):
        cls.lab = new_lab

    # Static Method
    @staticmethod
    def dna_length(sequence):
        return len(sequence)


# -------------------------
# Object Creation
# -------------------------

s1 = BioSample("S101", "ATGCGCGTAA")
s2 = BioSample("S102", "ATATGGCCAA")

# Instance Methods
s1.show_details()
s1.gc_content()

s2.show_details()
s2.gc_content()

# Static Method
print("\nDNA Length of S1:",
      BioSample.dna_length(s1.sequence))

# Class Method
BioSample.change_lab("Bioinformatics Research Center")

print("\nAfter Changing Lab Name")

s1.show_details()
s2.show_details()

# Object Identity
print("\nObject ID S1:", id(s1))
print("Object ID S2:", id(s2))
