# Přepis ozdobných nápisů
### Baseline
  - knn.ipynb - Načtení a otestování přesnosti [ParSEQ](https://github.com/baudm/parseq) modelu.
### Analýza datové sady
  - dataStat.py - Analýza délky slov a výskytu znaků podle labels.
  - imageRes.py - Analýza velikosti obrázků dle obrázků.
### Generování syntetické datové sady
#### Textové soubory využitelné pro generování syntetických obrázků:
  - random_words.txt - Vytvořené generátorem náhodných slov.
  - word_pairs.txt - Vytvořené z random_words.txt s využitím generátoru dvojic (pairs_gen.py)
  - czech_words.txt - Smysluplnější slova až trojice slov vytvořené s využitím chatGPT.
#### Scripty pro generování syntetických obrázků
  - pairs_gen.py - Generátor dvojic slov ze seznamu slov.
  - image_gen.py - Generátor obrázků z textového dokumentu slov. Využívá [trdg](https://github.com/Belval/TextRecognitionDataGenerator/tree/master).
