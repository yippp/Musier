# Main program running GA Model to generate an acceptable period
# Containing definitions of evaluation functions
# Version 1.0

from settings import *
from GAModel.period import unit, period
from GAModel.GA import GABase
from GAModel.SA import SA_optimize
from copy import deepcopy
import random

def period_evaluation(p):
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
        if (i == len(note_list) - 1) and (y[1] % 12 == ENDING[MAJOR]):
            score += (len(notes) - y[0]) * 80  # ENDING as the last note
    score -= len(note_list)
    for i in range(p.length):
        if p[i].chordID in  PRIOR_CHORD[MAJOR]:
            score += 14
        if (i >= 1) and ((p[i].chordID - p[i - 1].chordID) % 7 in {1, 3, 5}):
            score += 22
    if p[0].chordID == ENDING_CHORD[MAJOR]:
        score += 100
    if p[p.length - 1].chordID == ENDING_CHORD[MAJOR]:
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


def main_version_1(Tonality, Meter, notions):
    init_generation = []
    period_length = 8
    unit_length = 8
    for i in range(POPULATION):
        p = []
        for j in range(period_length):
            u = []
            for k in range(unit_length):
                ran = random.randint(LOWER_LIMIT, UPPER_LIMIT)
                u.append(ran)
            u = unit(u)
            u.update_chord_4()
            if (j == period_length - 1) or (j == period_length // 2 - 1):  # Ending units
                u = SA_optimize(u, T_ORIGIN, DELTA, ITERATIONS, ending = True)
            else:
                u = SA_optimize(u, T_ORIGIN, DELTA, ITERATIONS)
            p.append(u)
        p = period(p)
        init_generation.append(p)
    model = GABase(0.6, 0.03, init_generation, period_evaluation)
    for k in range(UPDATE_TIME):
        model.update_periods()
    return(model.generation[0])


def main_version_2(Tonality, Meter, notions):
    period_length = 8
    unit_length = 8
    primary = main_version_1(Tonality, Meter, notions)
    # primary = init_period()
    init_generation = []
    for i in range(POPULATION):
        p = deepcopy(primary)
        for j in range(p.length):
            p[j].update_chord_4()
            if (j == period_length - 1) or (j == period_length // 2 - 1):  # Ending units
                p.units[j] = SA_optimize(p.units[j], T_ORIGIN, DELTA, ITERATIONS, vari=False, ending=True)
            else:
                p.units[j] = SA_optimize(p.units[j], T_ORIGIN, DELTA, ITERATIONS, vari=False)
        init_generation.append(p)
    model = GABase(0.6, 0.03, init_generation, period_evaluation)
    # for i in init_generation:
    #     for j in i:
    #         print(j.score, end = ' ')
    #     print('\n')
    # for k in range(UPDATE_TIME):
    #     model.update_periods()
    primary.extend(model.generation[0])
    # for u in primary:
    #     print(u.chordID, u.score)
    return primary


# main_version_1()
# print(main_version_2(0,0,0))