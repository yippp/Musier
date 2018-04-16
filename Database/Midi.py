import mido


class Midi:

    def __init__(self, file):
        midi = mido.MidiFile(file)
        self.ticks_per_beat= midi.ticks_per_beat
        self.notes = []
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
        beat = 0
        for msg in midi.tracks[1]:
            beat += msg.time / self.ticks_per_beat
            print(msg.type)
            if (msg.type == 'note_on') or (msg.type == 'note_off'):
                self.notes.append([beat, msg.note, msg.velocity, msg.type])