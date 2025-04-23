#Soubor pro vyextrahování pouze vyplněných řádků souboru a změnění cesty k obrázkům.
import os

input_file = "labels_his_part2.txt"
output_file = "filtered_labels.txt"
filename = "hdata"

def filter_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input, \
         open(output_file, 'w', encoding='utf-8') as output:
        
        for line in input:
            #rozdělení
            stripped = line.strip().split(maxsplit=1)
            if len(stripped) < 2:
                continue
            
            second_part = stripped[1].strip()
            #výpis jenom anotovaných řádků
            if not (second_part.startswith('---') or second_part.startswith('---*')):
                #úprava cesty k souboru
                filepath = os.path.basename(stripped[0].strip())
                output.write(filename + "/" + filepath + " " + second_part + "\n")

filter_line(input_file, output_file)
