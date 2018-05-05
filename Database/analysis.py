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
    direction = 'Children'
    files = os.listdir(direction)
    pattern_dict = {}
    for file in files:
        path = direction + '/' + file
        if os.path.isfile(path):
            midi = Midi(path)
            note_list = midi.output_as_note_list(normalize=True, clean=True)
            note_list = delete_repetition(note_list)
            for i in range(1, len(note_list)):
                # Define your pattern here, remember to modify the iterator's range.
                # pattern = note_list[i][0] - note_list[i - 1][0]
                # pattern = note_list[i][0] + note_list[i - 2][0] - note_list[i - 1][0] * 2
                # pattern = (note_list[i - 1][0] - note_list[i - 2][0], note_list[i][0] - note_list[i - 1][0])
                pattern = (note_list[i - 1][2] * 4, note_list[i][2] * 4)
                if pattern_dict.get(pattern) is not None:
                    pattern_dict[pattern] += 1
                else:
                    pattern_dict[pattern] = 1
    pattern_list = list(pattern_dict.items())
    pattern_list.sort(key=lambda item: -item[1])
    file_out = 'results/' + direction + '/' + file_out
    f = open(file_out, 'w')
    for i in range(len(pattern_list)):
        f.write("%d %d %d\n" % (pattern_list[i][0][0], pattern_list[i][0][1], pattern_list[i][1]))
        # f.write("%d %d\n" % (pattern_list[i][0], pattern_list[i][1]))
    f.close()
    return pattern_list


def plot(xlabel, ylabel, file_in, file_out, num = None):
    direction = 'Children'
    file_in = 'results/' + direction + '/' + file_in
    f = open(file_in, 'r')
    x = []
    y = []
    label = []
    i = 0
    for line in f.readlines():
        x.append(i)
        # v1, v2 = tuple(map(int, line.split()))
        v1, v2, v3 = tuple(map(int, line.split()))
        # y.append(v2)
        # label.append(v1)
        y.append(v3)
        label.append((v1, v2))
        i += 1
    f.close()
    x = x[:num]
    y = y[:num]
    label = label[:num]
    plt.figure(figsize=(20, 4))
    plt.title('Frequency of Length Tuple in %s Set' % direction)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(x, label)
    plt.bar(x, y, 0.5, align='center')
    file_out = 'results/' + direction + '/' + file_out
    plt.savefig(file_out)
    plt.show()


get_pattern('length_tuple.txt')
plot('Length Tuple', 'Frequency', 'length_tuple.txt', 'length_tuple.jpg', 32)
# get_pattern('difference_tuple.txt')
# plot('Difference Tuple', 'Frequency', 'difference_tuple.txt', 'difference_tuple.jpg', 32)
# get_pattern('2nddiff-freq.txt')
# plot('Second Difference', 'Frequency', '2nddiff-freq.txt', '2nddiff-freq.jpg', 32)
# get_pattern('2nddiff-freq(without repetition).txt')
# plot('Second Difference', 'Frequency', '2nddiff-freq(without repetition).txt', '2nddiff-freq(without repetition).jpg', 32)
# get_pattern('diff-freq(without repetition).txt')
# plot('Difference', 'Frequency', 'diff-freq(without repetition).txt', 'diff-freq(without repetition).jpg', 32)
# get_pattern('diff-freq.txt')
# plot('Difference', 'Frequency', 'diff-freq.txt', 'diff-freq.jpg', 32)