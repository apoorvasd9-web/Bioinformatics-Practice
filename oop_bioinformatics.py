from abc import ABC, abstractmethod

# -------------------------
# Abstract Class
# -------------------------
class BioSequence(ABC):

    lab_name = "Genome Research Lab"

    def __init__(self, sample_id, sequence):
        self.sample_id = sample_id
        self._sequence = sequence
        self.__status = "Pending"

    @abstractmethod
    def analyze(self):
        pass

    def show_info(self):
        print("\nSample ID :", self.sample_id)
        print("Sequence :", self._sequence)

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    @classmethod
    def lab(cls):
        print("\nLab Name :", cls.lab_name)

    @staticmethod
    def sequence_type():
        print("\nDNA contains A, T, G and C bases.")


# -------------------------
# Child Class
# -------------------------
class DNASequence(BioSequence):

    def __init__(self, sample_id, sequence):
        super().__init__(sample_id, sequence)

    def analyze(self):
        super().show_info()

        gc = (
            self._sequence.count("G")
            + self._sequence.count("C")
        )

        length = len(self._sequence)

        gc_percent = (gc / length) * 100

        print("GC Content :", round(gc_percent, 2), "%")


# -------------------------
# Another Child Class
# -------------------------
class RNASequence(BioSequence):

    def analyze(self):
        super().show_info()
        print("RNA Analysis Completed")


# -------------------------
# Duck Typing
# -------------------------
def process(sequence):
    sequence.analyze()


# -------------------------
# Objects
# -------------------------
dna = DNASequence("DNA001", "ATGCGCGTA")

rna = RNASequence("RNA001", "AUGCGCUAA")

# -------------------------
# Class Method
# -------------------------
BioSequence.lab()

# -------------------------
# Static Method
# -------------------------
BioSequence.sequence_type()

# -------------------------
# Polymorphism + Duck Typing
# -------------------------
process(dna)

process(rna)

# -------------------------
# Encapsulation
# -------------------------
print("\nStatus :", dna.get_status())

dna.set_status("Completed")

print("Updated Status :", dna.get_status())
