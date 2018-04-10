from MSequence.MSeq import MSeq

little_star_MSeq = MSeq(LUT=None,
                        seq=[40, 40, 47, 47, 49, 49, 47, 0,
                             45, 45, 44, 44, 42, 42, 40, 0,
                             47, 47, 45, 45, 44, 44, 42, 0,
                             47, 47, 45, 45, 44, 44, 42, 0,
                             40, 40, 47, 47, 49, 49, 47, 0,
                             45, 45, 44, 44, 42, 42, 40, 0,],
                        quant_unit=4,bpm=80, time_sig=4, scale_type=0,key_sig=40)

# TODO delete following test
# from MCAssistant.MarkovChain import MarkovChain
#
# test_seq = [45, 45, 44, 44, 42, 42, 40, 0]
#     #[40, 40, 47, 47, 49, 49, 47, 47, 45, 45, 45, 44, 42, 42, 42, 0]
#
# uncompleted_little_star = MSeq(LUT=None, seq=test_seq,
#                                quant_unit=4, bpm=80, time_sig=4, scale_type=0, key_sig=40)
#
# mc = MarkovChain(uncompleted_little_star)
# mc.train_t_matrix(little_star)
# for i in range(2):
#     mc.extended_MSeq()
# print(mc.m_seq.seq)
