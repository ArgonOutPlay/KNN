#generátor dvojic slov ze souboru jednotlivých slov
import random

number_pairs = 2000
input_file ="random_words.txt"
output_file = "word_pairs.txt"

#načtení slov ze soubotu
with open(input_file, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]
#vytvoření náhodných dvojic s náhodnou úpravou a velikostí písmen
pairs = []
for _ in range(number_pairs):
    word_first = random.choice(words)
    word_second = random.choice(words)
    
    #náhodné nastavení některých slov na malé písmenka
    if random.random() < 0.5:
        word_first = word_first.lower()
    if random.random() < 0.5:
        word_second = word_second.lower()

    #přidání slova
    pairs.append(f"{word_first} {word_second}")

#uložení do souboru
with open(output_file, "w", encoding="utf-8") as f:
    for pair in pairs:
        f.write(pair + "\n")
