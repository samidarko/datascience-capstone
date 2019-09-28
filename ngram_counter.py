import sys
from collections import Counter
from nltk import ngrams


def ngram_counter(n, file):
    words_count = Counter()
    for line in open(file).readlines():
        words = line.strip().split(',')
        words_count += Counter([' '.join(ngram) for ngram in ngrams(words, n)])

    with open('{}.csv'.format(file), 'w') as f:
        for word, count in words_count.items():
            f.write('{},{}\n'.format(word, count))


if __name__ == "__main__":
    ngram_counter(int(sys.argv[1]), sys.argv[2])
