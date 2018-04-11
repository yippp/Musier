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
        if (i == len(note_list) - 1) and (y[1] % 12 == 9):
            score += (len(notes) - y[0]) * 80  # La as the last note
    score -= len(note_list)
    for i in range(p.length):
        if p[i].chord_score >= 19:
            score += 8
        if p[i].chordID in {2, 4, 6}:
            score += 6
        if (i >= 1) and ((p[i].chordID - p[i - 1].chordID) % 7 in {1, 3, 5}):
            score += 6
    if p[p.length - 1].chordID == 6:
        score += 150
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
    population = 35
    period_length = 8
    unit_length = 8
    update_time = 110
    for i in range(population):
        p = []
        for j in range(period_length):
            u = []
            for k in range(unit_length):
                ran = random.randint(-3, 12)
                u.append(ran)
            u = unit(u)
            u.update_chord_4()
            if (j == period_length - 1) or (j == period_length // 2 - 1):  # Ending units
                u = SA_optimize(u, 800, 0.95, 400, ending = True)
            else:
                u = SA_optimize(u, 800, 0.95, 400)
            p.append(u)
        p = period(p)
        init_generation.append(p)
    model = GABase(0.6, 0.03, init_generation, period_evaluation)
    for k in range(update_time):
        model.update_periods()
    return(model.generation[0])


def main_version_2(Tonality, Meter, notions):
    population = 35
    update_time = 160
    primary = init_period()
    init_generation = []
    for j in range(population):
        p = deepcopy(primary)
        for i in range(p.length):
            p[i].update_chord_4()
            p.units[i] = SA_optimize(p.units[i], 800, 0.95, 400, vari=False)
        init_generation.append(p)
    model = GABase(0.6, 0.03, init_generation, period_evaluation)
    for k in range(update_time):
        model.update_periods()
    return(model.generation[0])


# main_version_1()
main_version_2()
