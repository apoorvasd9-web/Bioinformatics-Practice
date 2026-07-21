print("====================================")
print("   Bioinformatics Mini Project")
print("      Created by Apoorva")
print("====================================")


# Parent Class
class Sequence:

    lab = "Genome Research Lab"      # Class Variable

    def __init__(self, seq_id, sequence):

        self.seq_id = seq_id         # Public Attribute
        self._sequence = sequence    # Protected Attribute
        self.__length = len(sequence) # Private Attribute

        print("Sequence Object Created")

    def show_details(self):

        print("\nSequence ID :", self.seq_id)
        print("Sequence :", self._sequence)
        print("Length :", self.__length)
        print("Lab :", Sequence.lab)

    def analyze(self):

        print("Analyzing General Sequence...")


# Child Class 1
class DNASequence(Sequence):

    def analyze(self):

        super().analyze()

        print("DNA Analysis Started")
        print("ATGC Count =", len(self._sequence))


# Parent Class 2
class Report:

    def report(self):

        print("Generating Bioinformatics Report...")


# Multiple Inheritance
class FinalReport(DNASequence, Report):

    def final_output(self):

        print("\n===== Final Report =====")

        self.show_details()

        self.analyze()

        self.report()

        print("Analysis Completed Successfully")


print("\nBefore Object Creation")

sample1 = FinalReport(
    "SEQ001",
    "ATGCGTAA"
)

print("\nAfter Object Creation")

sample1.final_output()

print("\nProgram Finished")
