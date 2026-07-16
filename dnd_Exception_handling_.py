# DNA EXCEPTION HANDLING PROJECT

try:
    with open("dna.txt", "r") as file:
         sequence = file.read()

    #DNA ANALYSIS
    print("DNA Sequence:", sequence)
    print("DNA Length:", len(sequence))
    print("A Count:", sequence.count("A"))

    #USER INPUT
    number = int(input("Enter a number:"))
    result = 10 / number

except FileNotFoundError:
    print("Error: DNA file not found.")
except ValueError:
    print("Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except TypeError:
    print("Error: Invalid data type.")

else:
    print("Division Result:", result)
    print("No Errors. Analysis Successful.")

finally:
    print("Program Finishied.")
    
