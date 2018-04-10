from MSequence.MSeq import MSeq


class MarkovChain:
    def __init__(self, m_seq):
        """
        Markov chain class help to generate music for inputting MSeq
        after create an instance using input MSeq
        use train_t_matrix(...) to train the MC, MarkovChain.ref_music.little_star_MSeq can be used as input
        then use extended_MSeq() to get the extended_MSeq

        # TODO using_LUT MSeq support
        :param m_seq: input MSeq, currently only support single track MSeq whose using_LUT is false
        """
        self.m_seq = m_seq
        self.t_matrix = [[0 for i in range(90)] for j in range(90)]  # 0, 1, ..., 88, 89 where 89 represent -1

    def extended_MSeq(self):
        """
        :return:
        """
        note_needs = self.m_seq.num_notes_needed()
        note_needs = self.m_seq.time_sinature if not note_needs else note_needs
        for i in range(note_needs):
            self.m_seq.seq.append(self.get_next_note())
            print('last note: %d, new note: %d' % (self.m_seq.seq[-2],self.m_seq.seq[-1]))
        return self.m_seq

    def get_next_note(self):
        """
        :return:
        """
        seq = self.m_seq.single_note_seq()
        from random import choices
        new_note = choices(range(90), self.t_matrix[seq[-1]])
        return new_note[0] if new_note[0] != 89 else -1

    def train_t_matrix(self, train_Mseq):
        """
        TODO train t_matrix
        TODO pre trained t_matrix
        :param train_MSeq: the reference MSeq
        :return:
        """
        for i in range(len(train_Mseq.seq)-1):
            row_index = train_Mseq.seq[i] if train_Mseq.seq[i] != -1 else 89
            col_index = train_Mseq.seq[i+1] if train_Mseq.seq[i+1] != -1 else 89
            self.t_matrix[row_index][col_index] += 1
        # TODO multiple inputs' training and normalization