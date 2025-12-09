def load_sequences(file_path="sequences.txt"):

    sequences = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split('\t')
                if len(parts) < 3:
                    parts = line.split(maxsplit=2)

                if len(parts) >= 3:
                    protein_name = parts[0].strip()
                    sequence = parts[2].strip()
                    sequences[protein_name] = sequence
        return sequences
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}


def calculate_diff(protein1, protein2, sequences):

    missing = []
    if protein1 not in sequences:
        missing.append(protein1)
    if protein2 not in sequences:
        missing.append(protein2)

    if missing:
        return f"MISSING: {', '.join(missing)}"


    seq1 = sequences[protein1]
    seq2 = sequences[protein2]


    min_len = min(len(seq1), len(seq2))


    differences = 0
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            differences += 1

    return str(differences)


def process_diff_queries():

    sequences = load_sequences()

    if not sequences:
        print("Error: No sequences loaded. Check the file 'sequences.txt'")
        return


    diff_queries = [
        ("6.8 kDa mitochondrial proteolipid", "Alcohol dehydrogenase"),
        ("RNA-dependent RNA polymerase [Fragment]", "Alcohol dehydrogenase"),
        ("Cecropin", "Pre-T/NK cell associated protein 6H9A")
    ]


    results = []
    for protein1, protein2 in diff_queries:
        result = calculate_diff(protein1, protein2, sequences)
        results.append(f"amino-acids difference: {result}")


    print("diff\t6.8 kDa mitochondrial proteolipid\tAlcohol dehydrogenase")
    print(results[0])
    print()
    print("diff\tRNA-dependent RNA polymerase [Fragment]\tAlcohol dehydrogenase")
    print(results[1])
    print()
    print("diff\tCecropin\tPre-T/NK cell associated protein 6H9A")
    print(results[2])


def main():

    process_diff_queries()


 
    main()
