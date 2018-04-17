from Midi import Midi
import os
import matplotlib.pyplot as plt


def delete_repetition(note_list):
    new_list = [note_list[0]]
    for i in range(1, len(note_list)):
        if note_list[i - 1][0] != note_list[i][0]:
            new_list.append(note_list[i])
    return new_list


def get_pattern(file_out):
    direction = 'Pop'
    files = os.listdir(direction)
    pattern_dict = {}
    for file in files:
        path = direction + '/' + file
        if os.path.isfile(path):
            midi = Midi(path)
            note_list = midi.output_as_note_list()
            # note_list = delete_repetition(note_list)
            for i in range(1, len(note_list)):
                pattern = note_list[i][0] - note_list[i - 1][0]
                # pattern = note_list[i][0] + note_list[i - 2][0] - note_list[i - 1][0] * 2  # Define your pattern here
                if pattern_dict.get(pattern) is not None:
                    pattern_dict[pattern] += 1
                else:
                    pattern_dict[pattern] = 1
    pattern_list = list(pattern_dict.items())
    pattern_list.sort(key=lambda item: -item[1])
    f = open(file_out, 'w')
    for i in range(len(pattern_list)):
        f.write("%d %d\n" % (pattern_list[i][0], pattern_list[i][1]))
    f.close()
    return pattern_list


def plot(xlabel, ylabel, file_in, file_out, num = None):
    f = open(file_in, 'r')
    x = []
    y = []
    label = []
    i = 0
    for line in f.readlines():
        x.append(i)
        v1, v2 = tuple(map(int, line.split()))
        y.append(v2)
        label.append(v1)
        i += 1
    f.close()
    x = x[:num]
    y = y[:num]
    label = label[:num]
    plt.figure(figsize=(10, 4))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x, label)
    plt.bar(x, y, 0.5, align='center')
    plt.savefig(file_out)
    plt.show()


get_pattern('diff-freq.txt')
plot('Difference', 'Frequency', 'diff-freq.txt', 'diff-freq.jpg', 24)
