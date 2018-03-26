from settings import *


class MSeq:
    def __init__(self, LUT, seq, quant_unit, bpm, time_sig, scale_type, key_sig):
        """
        TODO initialization way need to be design
        """
        self.LUT = LUT
        # {1: (1, 5, 8), 2: (5, 8, 10), 3: (1)}  # key is int, each value representing a combination of notes,
        # elements in value are absolute pitch, C4 = 0, C4# = 1, B4 = -1
        # C1 Major: do, do#, re, re#, mi, fa, fa#, so, so#, la, la#, ti, do
        #           1,   2,  3,  4,   5,  6,   7,  8,   9,  10,  11, 12, 13

        self.multi_notes = bool(LUT)
        # when multi_notes, using LUT, otherwise elements in seq are absolute pitch

        self.seq = seq
        #[1, 0, 0, 0, 2, 0, -1, 0, 1, 1, 2, 3]  # elements are keys of LUT. 0 is lasting for previous notes, -1 is mute

        self.quantization_unit = quant_unit
        # number of elements in self.seq in each bar, default better be 16 (as same as Orange's)

        self.bpm = bpm
        self.time_signature = time_sig  # TODO numerical representation need
        self.scale_type = scale_type  # 0 Major scale, 1 Minor scale
        self.key_signature = key_sig  # TODO numerical representation need

    def import_from_midi(self, midi_file):
        """
        TODO from midi file construct MSeq
        :param midi_file:
        :return:
        """
        pass

    def export_to_midi(self, midi_file):
        """
        TODO export this MSeq to a midi file
        :param midi_file:
        :return:
        """
        pass

    def re_quantify(self, quant_unit):
        """
        TODO change the quantization unit and change the seq and LUT
        :param quant_unit:
        :return:
        """
        pass

    def build_init_LUT(self):
        """
        TODO construct single note LUT same as seq
        :return:
        """
        pass

    def num_notes_needed(self):
        """
        TODO return number of note needed to fulfill the last bar
        :return:
        """
        pass

    def single_note_seq(self):
        """
        TODO return the single_note_version, where if multiple note exists, using the highest note
        :return:
        """
        if not self.multi_notes:
            return self.seq
        seq = []
        for i in self.seq:
            if i != -1 and i != 0:
                seq.append(max(self.LUT[i]))
            else:
                seq.append(i)
        return seq
