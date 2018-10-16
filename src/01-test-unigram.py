# 1-gramモデルを読み込み、エントロピーとカバレージを計算
# python 01-test-unigram.py TEST_FILE
import sys
import math

MODEL_FILE = open('./01-model.txt', 'r')
TEST_FILE = open(sys.argv[1], 'r')
probabilities = dict()

# parameter
lambda_1 = 0.95
lambda_unk = 1 - lambda_1
V = 1000000
W, H, unk = 0, 0, 0

# モデルの読み込み
for line in MODEL_FILE:
    w, P = line.strip().split()[0], line.strip().split()[1]
    probabilities[w] = P

# 評価と結果表示
for line in TEST_FILE:
    words = line.strip().split()
    words.append('</s>')
    for word in words:
        W += 1
        P = lambda_unk / V
        try:
            P += lambda_1 * float(probabilities[word])
            #print('P({}) = {}'.format(word, P))
        except KeyError:
            unk += 1
        H += -math.log2(P)
        #print('H({}) = {}'.format(word, -math.log2(P)))

print("entropy = {}".format(H / W))
print("coverage = {}".format((W - unk) / W))
