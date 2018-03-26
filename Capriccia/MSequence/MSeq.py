from settings import *


class MSeq:
    def __init__(self):
        """
        TODO initialization way need to be design
        """
        self.LUT = {1: (1, 3, 5), 2: (3, 5, 8), 3: (1)}  # key is int, each value representing a combination of notes
        self.seq = [1, 0, 0, 0, 2, 0, -1, 0, 1, 1, 2, 3]  # elements are keys of LUT. 0 is lasting for previous notes, -1 is mute
        self.quantization_unit = 4  # number of elements in self.seq in each bar, default better be 16 (as same as Orange's)
        self.bpm = 120
        self.time_signature = '4/4'  # TODO numerical representation need
        self.scale_type = 0  # 0 Major scale, 1 Minor scale
        self.key_signature = 'C4'  # TODO numerical representation need

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
