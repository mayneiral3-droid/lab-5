with open('sequences.0.txt', 'r', encoding='utf-8') as f:
    seqs = {}
    for line in f:
        if line.strip():
            parts = line.strip().split('\t')
            if len(parts) < 3:
                parts = line.strip().split(maxsplit=2)
            if len(parts) >= 3:
                seqs[parts[0].strip()] = parts[2].strip()

print("mode\tCecropin")
if "Cecropin" in seqs:
    s = seqs["Cecropin"]
    f = {}
    for c in s:
        f[c] = f.get(c, 0) + 1
    m = max(f.values())
    r = sorted([c for c, cnt in f.items() if cnt == m])[0]
    print(f"most common amino acid: {r}")
else:
    print("most common amino acid: MISSING: Cecropin")

print()

print("mode\tAlcohol dehydrogenase")
if "Alcohol dehydrogenase" in seqs:
    s = seqs["Alcohol dehydrogenase"]
    f = {}
    for c in s:
        f[c] = f.get(c, 0) + 1
    m = max(f.values())
    r = sorted([c for c, cnt in f.items() if cnt == m])[0]
    print(f"most common amino acid: {r}")
else:
    print("most common amino acid: MISSING: Alcohol dehydrogenase")