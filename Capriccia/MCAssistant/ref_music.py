from MSequence.MSeq import MSeq
little_star_list = [1, 1, 5, 5, 6, 6, 5, 0,
               4, 4, 3, 3, 2, 2, 1, 0,
               5, 5, 4, 4, 3, 3, 2, 0,
               5, 5, 4, 4, 3, 3, 2, 0,
               1, 1, 5, 5, 6, 6, 5, 0,
               4, 4, 3, 3, 2, 2, 1, 0,
               ]

little_star = MSeq(LUT=None,seq=little_star_list,quant_unit=4,bpm=80, time_sig=4, scale_type=0,key_sig='C4')
