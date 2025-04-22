#generátor obrázků dle slov
from trdg.generators import GeneratorFromStrings
from PIL import Image
import re
import os

#nastavení generování
# input_path ='czech_words.txt'
# output_path ="czech_dataset"
input_path ='word_pairs.txt'
output_path ="word_pairs_dataset"
image_count = 200

#čištění nevalidních znaků v názvu
def clean_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
    filename = filename.replace("\n", "").replace("\r", "")
    return filename.strip()

#vytvoření složky, pokud neexistuje
os.makedirs(output_path, exist_ok=True)

#načtení slov
with open(input_path, 'r', encoding='utf-8') as file:
    words = file.readlines()

#generátor
generator = GeneratorFromStrings(
    words, 
    count=image_count, 
    alignment='center',
    language='cz', 
    margins=(10, 10, 10, 10),
    blur=1,
    size=70,
    fit=True,
    random_blur=True
)

#uložení a zapsání
with open(output_path + "/labels.txt", "w", encoding="utf-8") as label_file:
    for i, (image, label) in enumerate(generator):
        if image is None:
            print(f"ERROR: Obrázek {i} se nepodařilo vygenerovat.")
            continue
        cleaned_label = clean_filename(label)
        #uložení obrázku
        filename = f"{i}_{cleaned_label}.png"
        image_path = os.path.join(output_path, filename)
        image.save(image_path)
        #uložení labelů
        label_file.write(f"{image_path} {label.strip()}\n")
