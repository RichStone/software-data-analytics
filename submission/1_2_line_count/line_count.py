import os


def count_lines(file_path):
    with open(file_path, 'r', encoding='utf8', errors='replace') as f:
        return len(f.readlines())


# traverse dir
for root, dirs, files in os.walk('.'):
    for filename in files:
        path = os.path.join(root, filename)
        print('{0};{1}'.format(filename, count_lines(path)))
