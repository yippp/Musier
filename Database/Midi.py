import mido


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

    def output_as_note_list(self):
        note_list = []
        notes_on = {}
        for msg in self.messages:
            start = notes_on.get(msg[1])
            if start is None:
                notes_on[msg[1]] = msg[0]
            else:
                note_list.append((msg[1], start, msg[0] - start))
                notes_on.pop(msg[1])
        note_list.sort(key=lambda note: (note[1], note[2]))
        return note_list
