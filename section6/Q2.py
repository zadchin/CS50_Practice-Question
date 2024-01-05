def match_dna(people_dna, sample_dna):
    # TODO: Compare each DNA sequence with sample_dna and return the matching person's name
    return 0

def contains_strand(dna_sequence, strand):
    # TODO: Check if the strand is a subsequence of the dna_sequence
    return 0

# Dictionary of people and their DNA sequences
people_dna = {
    "Alice": "CTGACTGAACTGACCTGA",
    "Bob": "TCCAGTCCAGTCCAG",
    "Charlie": "AGCTAGCTAGCT",
    "Diana": "CCGACCGACCGA",
    "Ethan": "TTATTATTATTA",
    # Optional: Students can add more complex sequences here
}

# Test the function with example inputs
print(match_dna(people_dna, "CTGACTGAACTGACCTGA"))    # Expected output: "Alice"
print(match_dna(people_dna, "AGCTAGCTAGCT"))          # Expected output: "Charlie"
print(match_dna(people_dna, "ACGTACGT"))               # Expected output: "No match found"


print(contains_strand("CTGACTGAACTGACCTGA", "ACTGA"))   # Expected output: True
print(contains_strand("TCCAGTCCAGTCCAG", "ACTGA"))      # Expected output: False


