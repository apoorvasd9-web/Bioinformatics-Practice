# Using a lambda function to calculate GC percentage.
# Formula: ((G + C) / Total Bases) * 100

calculate_gc_lambda = lambda g, c, total: round(((g + c) / total) * 100, 2) if total > 0 else 0

def validate_dna(sequence):
    """
    Validates if the sequence contains only A, T, G, and C.
    
    Uses PHASES: Collections (set), Control Flow (if/else).
    """
    # Convert sequence to uppercase to handle lowercase inputs safely
    seq_upper = sequence.upper()

    # Using a SET to extract unique characters from the sequence
    unique_bases = set(seq_upper)

    # Valid DNA characters allowed
    valid_bases = {'A', 'T', 'G', 'C'}

    # Check if the unique bases in our sequence fit within the valid bases set
    if unique_bases.issubset(valid_bases) and len(seq_upper) > 0:
        return True
    else:
        return False

def analyze_dna_sequence(sequence):
    """
    Performs core bioinformatics operations on a valid DNA sequence.
    Uses PHASES: Collections (dict, tuple, list), Loops, Functions.
    
    """
    seq_upper = sequence.upper()
    dna_length = len(seq_upper)

    # 1. Base Counting using a DICTIONARY
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in seq_upper:
        if base in counts:
            counts[base] += 1

    # 2. GC Content Calculation via our Lambda Function
    gc_percent = calculate_gc_lambda(counts['G'], counts['C'], dna_length)

    # 3. Generating Reverse Sequence using string slicing
    reversed_seq = seq_upper[::-1]

    # 4. Generating Complement Sequence using a DICTIONARY map
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement_list = []
    for base in seq_upper:
        complement_list.append(complement_map[base])
    complement_seq = "".join(complement_list)

    # 5. Reverse Complement
    reverse_complement_seq = complement_seq[::-1]

    # 6. DNA to RNA Transcription (Replacing T with U)
    rna_seq = seq_upper.replace('T', 'U')

    # 7. Start and Stop Codon Detection (Scanning in groups of 3)
    start_codons = []
    stop_codons = []

    # Loop through the sequence by increments of 3 (Codons)
    for i in range(0, dna_length - 2, 3):
        codon = seq_upper[i:i+3]
        if codon == "ATG":
            start_codons.append(f"ATG at position {i+1}")
        elif codon in ["TAA", "TAG", "TGA"]:
            stop_codons.append(f"{codon} at position {i+1}")

    # Package results inside a DICTIONARY to return multiple structured values
    results = {
       'length': dna_length,
       'counts': counts,
       'gc_content': gc_percent,
       'reverse': reversed_seq,
       'complement': complement_seq,
       'rev_complement': reverse_complement_seq,
       'rna': rna_seq,
       'start_codons': start_codons,
       'stop_codons': stop_codons
    }

    return results

# --- PHASE 6: FILE HANDLING & EXCEPTION HANDLING ---
def save_report_to_file(sequence, results, filename="dna_report.txt"):
    """
    Saves the analysis results to a text file using 'with open' and Exception Handling.
    """
    try:
        # Open file in APPEND mode ('a') so we don't overwrite older reports
        with open(filename, "a") as file:
            file.write("=" * 50 + "\n")
            file.write("          BIOINFORMATICS DNA REPORT\n")
            file.write("=" * 50 + "\n")
            file.write(f"Original Sequence: {sequence.upper()}\n")
            file.write(f"Sequence Length:   {results['length']} bases\n")
            file.write(f"Base Counts:       A:{results['counts']['A']}, T:{results['counts']['T']}, G:{results['counts']['G']}, C:{results['counts']['C']}\n")
            file.write(f"GC Content:        {results['gc_content']}%\n")
            file.write(f"RNA Transcript:    {results['rna']}\n")
            file.write(f"Reverse Seq:       {results['reverse']}\n")
            file.write(f"Complement Seq:    {results['complement']}\n")
            file.write(f"Rev-Complement:    {results['rev_complement']}\n")
            file.write(f"Start Codons Found: {results['start_codons']}\n")
            file.write(f"Stop Codons Found:  {results['stop_codons']}\n")
            file.write("=" * 50 + "\n\n")

            
    except IOError as e:
        print(f"\n[ERROR] Could not write report to file: {e}")
    else:
        # Runs ONLY if no exceptions occurred in the try block
        print(f"\n[SUCCESS] Analysis successfully appended to '{filename}'!")
    finally:
        # Always runs no matter what
        print("File operation process finished.")

def read_previous_reports(filename="dna_report.txt"):
   """
   Reads and displays all saved reports from the text file.
   """
   print("\n--- FETCHING SAVED DNA REPORTS ---")
   try:
      # Open file in READ mode ('r')
      with open(filename, "r") as file:
         content = file.read()
         if content.strip() == "":
            print("The report file is empty.")
         else:
            print(content)
   except FileNotFoundError:
      print(f"[NOTICE] No previous report file found named '{filename}'. Run an analysis first!")
   except IOError as e:
      print(f"[ERROR] An error occurred while reading the file: {e}")


# --- MAIN INTERFACE (Menu Driven) ---
def main_menu():
   """
   Controls the program flow using loops and user choices.
   """
   # An infinite loop that keeps the menu alive until the user decides to break out
   while True:
       print("\n" + "="*40)
       print("    BIOMEDICAL DNA ANALYZER")
       print("="*40)
       print("1. Analyze a New DNA Sequence")
       print("2. View Saved Analysis Reports")
       print("3. Exit Program")
       print("="*40)

       choice = input("Enter your choice (1-3): ").strip()

       
       # --- PHASE 1: CONTROL FLOW ---
       if choice == '1':
           dna_input = input("\nEnter your DNA sequence (e.g., ATGCATGAATGA): ").strip()

           # Sequence Validation
           if validate_dna(dna_input):
               print("\n[Validating] Sequence verified. Analyzing metrics...")


               # Perform analysis
               analysis_results = analyze_dna_sequence(dna_input)

               # Print clean, formatted output to screen
               print("\n" + "-"*30)
               print("        ANALYSIS RESULTS")
               print("-"*30)
               print(f"Length:         {analysis_results['length']} bp")
               print(f"GC Content:     {analysis_results['gc_content']}%")
               print(f"RNA Form:       {analysis_results['rna']}")
               print(f"Rev-Complement: {analysis_results['rev_complement']}")
               print(f"Start Codons:   {analysis_results['start_codons']}")
               print(f"Stop Codons:    {analysis_results['stop_codons']}")
               print("-"*30)

            # Save results to disk
               save_report_to_file(dna_input, analysis_results)
        else:
           print("\n[INVALID INPUT] DNA sequence must contain ONLY A, T, G, and C letters. Try again.")
    elif choice == '2':
        read_previous_reports()

    elif choice == '3':
         print("\nThank you for using DNA Analyzer Pro. Exiting program now...")
         break # Breaks out of the while loop to terminate execution


    else:
         print("\n[INVALID CHOICE] Please enter a number between 1 and 3.")


# This conditional block ensures the program runs smoothly when executed directly
if _name_ == "_main_":
main_menu()
         


 

 








 




 
      
 
   

         

   
 
 


 



 
 
        


    


   
 














            




















       
            

    












    




















    
















