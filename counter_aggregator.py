import sys
from collections import Counter
from glob import glob


def monogram_counter_aggregator(pathname):
    files = glob(pathname)
    words_count = Counter()
    for file in files:
        print('processing file {}'.format(file))
        for line in open(file).readlines():
            word, count = line.strip().split(',')
            words_count += Counter({word: int(count)})

    # TODO filename in parameter
    # with open('datasets/monogram_frequencies.txt', 'w') as f:
    #     for word, count in words_count.most_common():
    #         f.write('{},{}\n'.format(word, count))


if __name__ == "__main__":
    monogram_counter_aggregator(sys.argv[1])
