import os


def count_lines(file_path):
    with open(file_path, 'r') as f:
        return len(f.readlines())


for root, dirs, files in os.walk('.'):
    for filename in files:
        try:
            LOC = count_lines(os.path.join(root, filename))
            print('{0};{1}'.format(filename, LOC))
        except UnicodeDecodeError:
            # print('Could not count lines of file <<{0}>>'.format(filename))
            pass
