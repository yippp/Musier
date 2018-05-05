import os
from Midi import Midi


def period_to_abcjs(seq, numerator, denominator, key, scale):
    dictionary = ["C,", "^C,", "D,", "^D,", "E,", "F,", "^F,", "G,", "^G,", "A,", "^A,", "B,",
                  "C", "^C", "D", "^D", "E", "F", "^F", "G", "^G", "A", "^A", "B",
                  "c", "^c", "d", "^d", "e", "f", "^f", "g", "^g", "a", "^a", "b",
                  "c'", "^c'", "d'", "^d'", "e'", "f'", "^F'", "g'", "^g'", "a'", "^a'", "b'"]
    count = 1
    note_count = 0
    period_count = -1
    long_note = False
    generated_notions = '''X: 1\nM: %d/%d\nL: 1/%d\nK: %s\n''' % (numerator, denominator, scale, key)
    for i in range(len(seq)):
        if seq[i] is None:
            count += 1
            long_note = True
        else:
            if long_note is True:
                generated_notions += str(count)
                count = 1
                long_note = False
            if ((note_count) % (scale // denominator * numerator)) == 0:
                period_count += 1
                generated_notions += "|"
                if ((period_count % 4) == 0) and (period_count != 0):
                    generated_notions += "\n"
            generated_notions += dictionary[12 + seq[i]]
        note_count += 1
    if seq[-1] is None:
        generated_notions += str(count)
    return generated_notions


direction = 'Pop'
files = os.listdir(direction)
SCALE = 16
for file in files:
    path = direction + '/' + file
    if os.path.isfile(path):
        midi = Midi(path)
        note_list = midi.output_as_note_list(normalize=True)
        try:
            p = midi.output_as_period(scale=SCALE, base=60)
            file_out = 'periods/' + direction + '/' + file[:-4] + '.txt'
            f = open(file_out, 'w')
            f.write(str(p))
            f.close()
            abcjs = period_to_abcjs(p.get_notes(), midi.numerator, midi.denominator, midi.key, SCALE)
            file_out = 'abcjs/' + direction + '/' + file[:-4] + '.txt'
            f = open(file_out, 'w')
            f.write(abcjs)
            f.close()
        except:
            print("Error occurred when converting", file, "to abcjs.")
