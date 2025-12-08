import fileinput

with open('sequences.0.txt', 'rt') as hert:
    results = []


    for line in hert:
        line = line.strip()
        if not line:  # Пропускаем пустые строки
            continue


        parts = line.split('\t')
        if len(parts) < 3:
            parts = line.split(maxsplit=2)


        if len(parts) >= 3:
            protein_name = parts[0].strip()
            organism = parts[1].strip()
            sequence = parts[2].strip()


            if 'SIIK' in sequence and 'PLML' in sequence and 'FK3I' in sequence:

                results.append(f"{organism} - {protein_name}")


with open('genedata.0.txt', 'w') as output_file:
    if results:
        for result in results:
            output_file.write(result + '\n')
    else:
        output_file.write('NOT FOUND')
result={}