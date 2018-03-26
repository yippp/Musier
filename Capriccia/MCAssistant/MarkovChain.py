from MSequence.MSeq import MSeq


class MarkovChain:
    def __init__(self, m_seq, t_matrix):
        self.m_seq = m_seq
        self.t_matrix = t_matrix

    def extented_MSeq(self):
        """
        :return:
        """
        self.m_seq = MSeq()
        for i in range(self.m_seq.num_notes_needed()):
            self.m_seq.seq.append(self.get_next_note())
        return self.m_seq

    def get_next_note(self):
        """
        :return:
        """
        seq = self.m_seq.single_note_seq()
        # TODO multiply the t_matrix
        new_note = 1
        return new_note


    def train_t_matrix(self):
        """
        TODO get t_matrix
        :return:
        """
        pass