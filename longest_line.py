def max_line_length(file_name):
    max_length = 0
    with open(file_name) as f:
        for line in f.readlines():
            line_length = len(line.strip())
            if line_length > max_length:
                max_length = line_length
    # return max_length
    print("{} max line length is {}".format(file_name, max_length))


max_line_length('datasets/en_US/en_US.blogs.txt')
max_line_length('datasets/en_US/en_US.news.txt')
