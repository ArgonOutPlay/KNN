import matplotlib.pyplot as plt
from collections import Counter

file_path = 'train_labels.txt'
word_lengths = []
letter_counts = Counter()

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 2:
            continue 
        word = parts[1]
        word_lengths.append(len(word))
        letter_counts.update(word)

plt.figure(figsize=(12, 10))
# delka slov
plt.subplot(2, 1, 1)
plt.hist(word_lengths, bins=range(1, max(word_lengths)+2), edgecolor='black', alpha=0.75)
plt.xlabel('Délka slova')
plt.ylabel('Počet výskytů')
plt.title('Histogram délek slov')

# frekvence znaku
plt.subplot(2, 1, 2)
letters, counts = zip(*sorted(letter_counts.items()))
plt.bar(letters, counts, color='skyblue', edgecolor='black')
plt.xlabel('Písmeno')
plt.ylabel('Počet výskytů')
plt.title('Frekvence jednotlivých znaků')

plt.tight_layout()
plt.show()