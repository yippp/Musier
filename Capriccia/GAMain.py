# Main program running GA Model to generate an acceptable period
# Containing definitions of evaluation functions
# Version 1.0

from settings import *
from GAModel.period import unit, period
from GAModel.GA import GABase
import random


def unit_evaluation(u):
    note_list = []
    for i in range(u.length):
        if u[i] is not None:
            note_list.append((i, u[i]))
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
            score += 4
        if p_diff in {1, 2, 3, 4, 8, 9, 10, 12}:
            score += 2
    score -= len(note_list)
    score += u.chord_score
    return score


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
            score += 4
        if p_diff in {1, 2, 3, 4, 8, 9, 10, 12}:
            score += 2
    score -= len(note_list)
    for u in p.units:
        if u.chord_score >= 19:
            score += 8
        if u.chordID in {2, 4, 6}:
            score += 6
    if p[p.length - 1].chordID == 6:
        score += 10
    if score < 0:
        score = 0
    return score


def period_evaluation_single(p):
    """
    Only works when every unit contains a single note.
    :param p:
    :return:
    """
    score = 0
    if (p[0][0] % 12) in {0, 4, 9}:
        score += 18
    if (p[p.length - 1][0] % 12) in {9}:
        score += 18
    for i in range(1, p.length):
        if (p[i][0] % 12) in {0, 2, 4, 5, 7, 9, 11}:
            score += 4
        if (i%8 == 4) and ((p[i][0] % 12) in {2, 5, 9}):
            score += 8
        if (i%8 == 0) and ((p[i][0] % 12) in {0, 4, 9}):
            score += 8
        diff = abs(p[i][0] - p[i-1][0])
        if diff > 9:
            score -= 20
        if diff in {5, 7}:
            score += 5
        elif diff in {4, 8}:
            score += 4
        elif diff in {3, 9}:
            score += 3
        elif diff in {2, 1}:
            score += 2
        elif diff in {0}:
            score += 1
    if score < 0:
        score = 0
    return score


def main_version_1():
    init_generation = []
    population = 45
    period_length = 8
    unit_length = 8
    update_time = 75
    for i in range(population):
        p = []
        for j in range(period_length):
            u = []
            for k in range(unit_length):
                ran = random.randint(-3, 12)
                u.append(ran)
            u = unit(u)
            u.update_chord_4()
            p.append(u)
        p = period(p)
        init_generation.append(p)
    model = GABase(0.6, 0.04, 0, 0, init_generation, unit_evaluation, period_evaluation)
    for k in range(update_time):
        model.update_periods_with_SA()
    print(model.generation[0])
    print(model.generation[0].score)

def main_verion_single():
    init_generation = []
    population = 35
    period_length = 25
    update_time = 60
    for i in range(population):
        p = []
        for j in range(period_length):
            ran = random.randint(-3, 12)
            p.append(unit([ran]))
        p = period(p)
        init_generation.append(p)
    model = GABase(0.6, 0.04, 0, 0, init_generation, unit_evaluation, period_evaluation_single)
    for k in range(update_time):
        model.update_periods()
    print('NoteList = ',end = '')
    for i in range(period_length):
        print(model.generation[0][i][0], end=',')
    print(' Score =',period_evaluation_single(model.generation[0]))

# main_verion_single()
main_version_1()