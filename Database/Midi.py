import mido
from GAModel.period import unit, period


class Midi:
    def __init__(self, file):
        midi = mido.MidiFile(file)
        self.file_name = file
        self.ticks_per_beat= midi.ticks_per_beat
        self.messages = []
        self.numerator = None
        self.denominator = None
        self.key = None
        self.tempo = None
        for msg in midi.tracks[0]:
            if msg.type == 'time_signature':
                self.numerator = msg.numerator
                self.denominator = msg.denominator
            if msg.type == 'key_signature':
                self.key = msg.key
            if msg.type == 'set_tempo':
                self.tempo = msg.tempo
        tick = 0
        for msg in midi.tracks[1]:
            tick += msg.time
            beat = tick / self.ticks_per_beat
            if (msg.type == 'note_on') or (msg.type == 'note_off'):
                self.messages.append((beat, msg.note, msg.velocity, msg.type))

    def output_as_note_list(self, normalize=False):
        note_list = []
        notes_on = {}
        for msg in self.messages:
            start = notes_on.get(msg[1])
            if start is None:
                notes_on[msg[1]] = msg[0]
            else:
                end = msg[0]
                if normalize:
                    start = round(start * 4) / 4
                    end = round(end * 4) / 4
                note_list.append((msg[1], start, end - start))
                notes_on.pop(msg[1])
        note_list.sort(key=lambda note: (note[1], note[2]))
        return note_list

    def output_as_period(self, scale=16, base=72):
        calibration = self.denominator / scale
        note_list = self.output_as_note_list(normalize=True)
        index = 1
        while index < len(note_list):  # Clean overlapped notes
            if note_list[index][1] < note_list[index - 1][1] + calibration:
                del note_list[index]
            else:
                index += 1
        bias = (note_list[0][1] // self.numerator) * self.numerator
        index = 0
        p = period()
        while True:
            last = bias
            u = []
            while (index < len(note_list)) and (note_list[index][1] < bias + self.numerator):
                u.extend([None] * int((note_list[index][1] - last) // calibration))
                u.append(note_list[index][0] - base)
                last = note_list[index][1] + calibration
                index += 1
            u.extend([None] * int((bias + self.numerator - last) // calibration))
            if len(u) != self.numerator // calibration:
                return bias
            p.append(unit(u))
            if index == len(note_list):
                return p
            bias += self.numerator
