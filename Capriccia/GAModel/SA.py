from settings import *
from math import exp
from copy import deepcopy
import random


def create_mutated_unit(u):
    '''
    :return: a new unit mutated from u
    '''
    u_m = deepcopy(u)
    ran = random.randint(0, u.length - 1)
    if u_m.notes[ran] != None:
        if random.random() > 0.5:
            u_m.notes[ran] = u_m.notes[ran] + random.randint(-5, 5)
        else:
            u_m.notes[ran] = None
    else:
        u_m.notes[ran] = random.randint(-3, 12)
    return u_m


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
        if p_diff in {2, 3, 4, 8, 9, 10, 12}:
            score += 2
        if i == len(note_list) - 1:
            score += u.length - y[0] - 1
    score -= len(note_list)
    score += u.chord_score
    return score


def unit_evaluation_ending(u):
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
        if p_diff in {2, 3, 4, 8, 9, 10, 12}:
            score += 2
        # For ending in root pitch 'La'
        if (i == len(note_list) - 1) and (y[1] % 12 == 9):
            score += (u.length - y[0]) * 12
    score -= len(note_list)
    score += u.chord_score
    return score


def SA_optimize(u, t, t_delta, time, ending = False):
    for i in range(time):
        u_m = create_mutated_unit(u)
        u_m.update_chord_4()
        if ending:
            u_m.score = unit_evaluation_ending(u_m)
        else:
            u_m.score = unit_evaluation(u_m)
        if u_m.score > u.score:
            u = u_m
        else:
            if exp((u_m.score - u.score) / t) > random.random():
                u = u_m
        t = t * t_delta
    return u