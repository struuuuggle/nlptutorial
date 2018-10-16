# ファイルの中の単語の頻度を数えるプログラム
#
# TEST_FILE: ../../test/00-input.txt
# ANSWER_FILE: ../../test/00-answer.txt

import sys

TARGET_FILE = open(sys.argv[1], "r")

def count_freq(FILE):
    d = dict()
    for line in FILE:
        for word in line.strip().split():
            if not word in d.keys():
                d[word] = 1
            else:
                d[word] += 1

    for item in d.items():
        print(item[0], item[1], sep='\t')
    return d

if __name__ == '__main__':
    count_freq(TARGET_FILE)
