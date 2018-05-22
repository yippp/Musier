# Main program running GA Model to generate an acceptable period
# Containing definitions of evaluation functions
# Version 1.0

from settings import *
from GAModel.period import unit, period
from GAModel.GA import GABase
from GAModel.SA import SA_optimize
from copy import deepcopy
import random


def period_evaluation(p, major):
    notes = p.get_notes()
    note_list = []
    for i in range(len(notes)):
        if notes[i] is not None:
            note_list.append((i, notes[i]))
    if len(note_list) == 0:
        return 0
    score = 0
    for i in range(1, len(note_list)):
        x = note_list[i - 1]
        y = note_list[i]
        t_diff = y[0] - x[0]  # length
        p_diff = abs(y[1] - x[1])  # pitch difference
        if t_diff == 1:
            if p_diff > 4:
                score -= p_diff
        elif t_diff == 2:
            if p_diff > 8:
                score -= (p_diff - 4)
        else:
            if p_diff > 12:
                score -= (p_diff - 8)
        if p_diff in {5, 7}:
            score += 5
        if p_diff in {2, 3, 4, 8, 9, 10, 12}:
            score += 3
        if (y[1] % 12) not in {0, 2, 4, 5, 7, 9, 11}:
            score -= 1
        if (i == len(note_list) - 1) and (y[1] % 12 == ENDING[major]):
            score += (len(notes) - y[0]) * 80  # ENDING as the last note
    score -= len(note_list)
    for i in range(p.length):
        if p[i].chordID in PRIOR_CHORD[major]:
            score += 10
        if (i >= 1) and ((p[i].chordID - p[i - 1].chordID) % 7 in {1, 3, 5}):
            score += 15
    if p[0].chordID == ENDING_CHORD[major]:
        score += 100
    if p[p.length - 1].chordID == ENDING_CHORD[major]:
        score += 100
    if score < 0:
        score = 0
    return score


def init_period():
    p = period()
    p.append(unit([4, None, 4, None, 2, None, 4, None]))
    p.append(unit([2, 0, None, 2, -3, None, None, None]))
    p.append(unit([7, None, 7, None, 7, 2, None, 0]))
    p.append(unit([7, 4, None, None, None, None, None, None]))
    p.append(unit([9, None, 9, None, 7, 9, None, 4]))
    p.append(unit([7, 4, None, 2, 4, None, None, None]))
    p.append(unit([2, None, 0, 2, 4, None, 2, None]))
    p.append(unit([-1, None, None, None, None, None, None, None]))
    return p


def main_version_1(meter, major, user_input=None):
    # Meter: {3, 4}
    # Major: {0, 1}
    init_generation = []
    period_length = 8
    unit_length = meter * 2
    if user_input is None:
        user_input = []
    j = 0
    fixed_units = []
    while j <= len(user_input) - 1:
        fixed_units.append(user_input[j:j+unit_length])
        j += unit_length
    if (len(fixed_units) > 0) and (len(fixed_units[-1]) < unit_length):
        fixed_units[-1].extend([None] * (unit_length - len(fixed_units[-1])))
    fixed_length = len(fixed_units)
    for j in range(fixed_length):
        fixed_units[j] = unit(fixed_units[j], mutable=False)
        fixed_units[j].update_chord(meter)
    for i in range(POPULATION):
        p = deepcopy(fixed_units)
        for j in range(fixed_length, period_length):
            if fixed_length == 0:
                u = []
                for k in range(unit_length):
                    ran = random.randint(LOWER_LIMIT, UPPER_LIMIT)
                    u.append(ran)
                u = unit(u, mutable=True)
                u.update_chord(meter)
            elif fixed_length == 2:
                u = deepcopy(p[-2])
                u.chordID = random.randint(1, len(CHORD) - 1)
                u.mutable = True
            else:
                u = deepcopy(p[-1])
                u.chordID = random.randint(1, len(CHORD) - 1)
                u.mutable = True
            if j == period_length - 1:
                u.chordID = ENDING_CHORD[major]
                u.fix_chord = True
            if (j == period_length - 1) or (j == period_length // 2 - 1):  # Ending units
                u = SA_optimize(u, T_ORIGIN, DELTA, ITERATIONS, ending = True)
            else:
                u = SA_optimize(u, T_ORIGIN, DELTA, ITERATIONS)
            p.append(u)
        p = period(p)
        init_generation.append(p)
    model = GABase(1.0, 0.03, init_generation, period_evaluation, major)
    for k in range(UPDATE_TIME):
        model.update_periods()
        print(model.least, model.generation[0].score)
    return model.generation[0]


def main_version_2(meter, major, user_input=None):
    period_length = 8
    unit_length = meter * 2
    primary = main_version_1(meter, major, user_input)
    # primary = init_period()
    init_generation = []
    for i in range(POPULATION):
        p = deepcopy(primary)
        for j in range(p.length):
            if not p[j].fix_chord:
                p[j].update_chord(meter)
            if (j == period_length - 1) or (j == period_length // 2 - 1):  # Ending units
                p.units[j] = SA_optimize(p.units[j], T_ORIGIN, DELTA, ITERATIONS, vari=False, ending=True)
            else:
                p.units[j] = SA_optimize(p.units[j], T_ORIGIN, DELTA, ITERATIONS, vari=False)
        init_generation.append(p)
    model = GABase(1.0, 0.03, init_generation, period_evaluation, major)
    # for i in init_generation:
    #     for j in i:
    #         print(j.score, end = ' ')
    #     print('\n')
    for k in range(UPDATE_TIME):
       model.update_periods()
    primary.extend(model.generation[0])
    # for u in primary:
    #     print(u.chordID, u.score)
    chord_track = period()
    for i in range(primary.length):
        u = primary[i]
        chord_note = []
        if i != primary.length - 1:
            for j in range(meter):
                chord_note.extend([CHORD_NOTE[meter][u.chordID][j] - 12, None])
        else:
            chord_note.append(CHORD_NOTE[meter][u.chordID][0] - 12)
            chord_note.extend([None] * (meter * 2 - 1))
        chord_track.append(unit(chord_note))
    return primary, chord_track


# print(main_version_2(3,0,[0, None, 2, None, 4, None, 0, None, 7, None, None, None])[0].get_notes())