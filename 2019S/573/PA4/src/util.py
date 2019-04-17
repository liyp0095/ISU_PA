def read_csv_file(filename):
    with open(filename) as fp:
        for line in fp.readlines():
            a_line = line.strip(" ").strip("\n").split(",")
            yield a_line

