import sys
from collections import Counter


def monogram_counter(file):
    words_count = Counter()
    for line in open(file).readlines():
        words_count += Counter(line.strip().split(','))

    with open('{}.csv'.format(file), 'w') as f:
        for word, count in words_count.items():
            f.write('{},{}\n'.format(word, count))


if __name__ == "__main__":
    monogram_counter(sys.argv[1])
