# 1-gramモデルを学習

import sys

counts = dict()
total_count = 0
TRAINING_FILE = open(sys.argv[1], 'r')

for line in TRAINING_FILE:
    words = line.strip().split()
    words.append('</s>')
    for word in words:
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1
        total_count += 1

with open('./01-model.txt', 'w') as f:
    for word, count in counts.items():
        probability = counts[word]/total_count
        f.writelines(word + '\t' + str(probability) + '\n')
