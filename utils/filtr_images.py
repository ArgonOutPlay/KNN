#Vyextrahování pouze obrázků ke kterým jsou dostupné labely
import os
import shutil

input_folder = 'part2'
output_folder = 'hdata'
label_path = 'fl.txt'    #vygenerovatelné z filtr_labels.py

#povolené koncovky - bylo to potřeba, protože jinak to tvořilo nějaké divné obrázky.
valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

#vytvoření složky, pokud neexistuje
os.makedirs(output_folder, exist_ok=True)

#načtení obrázků co jsou uvedeny v label
image_filenames = []
with open(label_path, 'r', encoding='utf-8') as label_file:
    for line in label_file:
        #získání cesty
        stripped = line.strip().split()
        if not stripped:
            continue
        filename = stripped[0]
        #přidání do pole ocest
        if os.path.splitext(filename)[1].lower() in valid_extensions:
            image_filenames.append(filename)
        else:
            print(f"ERROR: Invalid filename: {filename}")

#nakopírování obrázků
for filename in image_filenames:
    #otevření
    source_path = os.path.join(input_folder, filename)
    save_path = os.path.join(output_folder, filename)
    
    #nakopírování
    if os.path.isfile(source_path):
        shutil.copy2(source_path, save_path)
    else:
        print(f"ERROR: File was not found: {filename}")
