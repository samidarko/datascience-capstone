import sys
from collections import Counter
from datetime import datetime
from glob import glob


def counter_aggregator(output_file, input_files):
    files = glob(input_files)
    words_count = Counter()
    for file in files:
        total_lines = len(open(file).readlines())
        with open(file) as input_file:
            line_number = 0
            previous_percentage = 0
            for line in input_file.readlines():
                line_number += 1
                current_percentage = int(line_number/total_lines*100)
                if current_percentage > previous_percentage:
                    previous_percentage = current_percentage
                    print('[{}] File {} {}% processed'.format(datetime.now(), file, current_percentage))
                word, count = line.strip().split(',')
                words_count += Counter({word: int(count)})

    with open(output_file, 'w') as f:
        for word, count in words_count.most_common():
            f.write('{},{}\n'.format(word, count))


if __name__ == "__main__":
    counter_aggregator(sys.argv[1], sys.argv[2])
