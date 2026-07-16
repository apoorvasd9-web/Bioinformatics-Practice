Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============================= RESTART: C:/Users/NI/AppData/Local/Programs/Python/Python313/BIOINFORMATICS_DNA_Analyser_miniProject.py =============================

========================================
    BIOMEDICAL DNA ANALYZER PRO v1.0
========================================
1. Analyze a New DNA Sequence
2. View Saved Analysis Reports
3. Exit Program
========================================
Enter your choice (1-3): 1

Enter your DNA sequence (e.g., ATGCATGAATGA): ATGCATGAATGA

[Validating] Sequence verified. Analyzing metrics...

------------------------------
        ANALYSIS RESULTS
------------------------------
Length:         12 bp
GC Content:     33.33%
RNA Form:       AUGCAUGAAUGA
Rev-Complement: TCATTCATGCAT
Start Codons:   ['ATG at position 1']
Stop Codons:    ['TGA at position 10']
------------------------------

[SUCCESS] Analysis successfully appended to 'dna_report.txt'!
File operation process finished.

========================================
    BIOMEDICAL DNA ANALYZER PRO v1.0
========================================
1. Analyze a New DNA Sequence
2. View Saved Analysis Reports
3. Exit Program
========================================
Enter your choice (1-3): 2

--- FETCHING SAVED DNA REPORTS ---
DNA Sequence: ATGCGTAA
Length: 8
A Count: 3
T Count: 2
G Count: 2
C Count: 1
GC Content: 37.50 %==================================================
          BIOINFORMATICS DNA REPORT
==================================================
Original Sequence: ATGCATGAATGA
Sequence Length:   12 bases
Base Counts:       A:5, T:3, G:3, C:1
GC Content:        33.33%
RNA Transcript:    AUGCAUGAAUGA
Reverse Seq:       AGTAAGTACGTA
Complement Seq:    TACGTACTTACT
Rev-Complement:    TCATTCATGCAT
Start Codons Found: ['ATG at position 1']
Stop Codons Found:  ['TGA at position 10']
==================================================



========================================
    BIOMEDICAL DNA ANALYZER PRO v1.0
========================================
1. Analyze a New DNA Sequence
2. View Saved Analysis Reports
3. Exit Program
========================================
Enter your choice (1-3): 3

Thank you for using DNA Analyzer Pro. Exiting program now...
