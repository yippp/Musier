NULL_SCORE = -1
CHORD = [{}, {0, 4, 7}, {2, 5, 9}, {4, 7, 11}, {5, 9, 0}, {7, 11, 2}, {9, 0, 4}, {11, 2, 5}]
CHORD_NOTE = {4: [[None, None, None, None], [0, 7, 4, 7], [-3, 5, 2, 5], [-1, 7, 4, 7], [0, 9, 5, 9], [-1, 7, 2, 7], [-3, 4, 0, 4], [-1, 5, 2, 5]],
              3: [[None, None, None], [0, 4, 7], [-3, 2, 5], [-1, 4, 7], [0, 5, 9], [-1, 2, 7], [-3, 0, 4], [-1, 2, 5]]}
DOWNBEAT = {8: {2:1, 4:2, 6:1}, 6: {2:1, 4:1}}
PRIOR_CHORD = {0: {2, 3, 6}, 1: {1, 4, 5}}
ENDING = {0: 9, 1: 0}
ENDING_CHORD = {0: 6, 1: 1}
UPPER_LIMIT = 20
LOWER_LIMIT = 0
MID_PITCH = 10
T_ORIGIN = 800
DELTA = 0.97
ITERATIONS = 300
POPULATION = 36
UPDATE_TIME = 100