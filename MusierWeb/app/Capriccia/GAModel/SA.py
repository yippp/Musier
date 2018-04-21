from settings import *
from math import exp
from copy import deepcopy
import random
from GAModel.period import unit

def create_mutated_unit(u):
    '''
    :return: a new unit mutated from u
    '''
    u_m = deepcopy(u)
    ran = random.randint(0, u.length - 1)
    if u_m.notes[ran] is not None:
        if random.random() > 0.5:
            u_m.notes[ran] = u_m.notes[ran] + random.randint(max(-4, LOWER_LIMIT - u_m.notes[ran]), min(4, UPPER_LIMIT - u_m.notes[ran]))
        else:
            u_m.notes[ran] = None
    else:
        i = ran
        while (i >= 0) and (u_m.notes[i] is None):
            i -= 1
        if i < 0:
            left = MID_PITCH
        else:
            left = u_m.notes[i]
        i = ran
        while (i < u.length) and (u_m.notes[i] is None):
            i += 1
        if i >= u.length:
            right = MID_PITCH
        else:
            right = u_m.notes[i]
        u_m.notes[ran] = (left + right) // 2
        u_m.notes[ran] = u_m.notes[ran] + random.randint(max(-4, LOWER_LIMIT - u_m.notes[ran]), min(4, UPPER_LIMIT - u_m.notes[ran]))
    return u_m


def create_same_rhythm_mutated_unit(u):
    '''
        :return: a new unit mutated from u with the same rhythm
    '''
    u_m = deepcopy(u)
    ran = random.randint(0, u.length - 1)
    if u_m.notes[ran] is not None:
        u_m.notes[ran] = u_m.notes[ran] + random.randint(max(-4, LOWER_LIMIT - u_m.notes[ran]), min(4, UPPER_LIMIT - u_m.notes[ran]))
    return u_m


def unit_evaluation(u, debug=False):
    note_list = []
    last = 0
    for i in range(u.length):
        if u[i] is not None:
            note_list.append((i, u[i]))
            last = u[i]
    if len(note_list) == 0:
        return 0
    note_list.append((u.length, last))
    length_on_chord = 0
    fierce_jump = 0
    taboo_jump = 0
    bad_downbeat = 0
    bad_start = 0
    overtone = 0
    black = 0
    total_downbeat = 0
    for i in range(1, len(note_list)):
        x = note_list[i - 1]
        y = note_list[i]
        t_diff = y[0] - x[0]  # length
        p_diff = abs(y[1] - x[1])  # pitch difference
        if (x[1] % 12) in CHORD[u.chordID]:
            length_on_chord += t_diff
        if t_diff == 1:
            if p_diff > 4:
                fierce_jump += 1
            if (p_diff == 6) or (p_diff > 7):
                taboo_jump += 1
        elif t_diff == 2:
            if p_diff > 5:
                fierce_jump += 1
            if (p_diff in {6, 10, 11}) or (p_diff > 8): # TODO optimize these constants
                taboo_jump += 1
        else:
            if p_diff > 7:
                fierce_jump += 1
            if (p_diff in {6, 10, 11}) or (p_diff > 12):
                taboo_jump += 1
        if DOWNBEAT[u.length].get(x[0], False):
            total_downbeat += DOWNBEAT[u.length][x[0]]
            if (x[1] % 12) not in CHORD[u.chordID]:  # downbeat out of chord
                bad_downbeat += DOWNBEAT[u.length][x[0]]
        if (i == 1) and ((x[0] != 0) or ((x[0] == 0) and ((x[1] % 12) not in CHORD[u.chordID]))):  # start pitch out of chord
            bad_start = 1
        if ((x[1] % 12) not in CHORD[u.chordID]) and ((y[1] % 12) in CHORD[u.chordID]):
            overtone += 1
        if (y[1] % 12) not in {0, 2, 4, 5, 7, 9, 11}:
            black += 1
    score = 50 - 8 * bad_start - 7 * taboo_jump
    if length_on_chord > u.length // 2:
        score += length_on_chord
    else:
        score += 3 * length_on_chord - u.length - 2
    if bad_downbeat > 0:
        score -= 3 * bad_downbeat - 2
    if total_downbeat * 2 + 1 < len(note_list):
        score -= 3 * (len(note_list) - total_downbeat * 2 - 1)
    if black > 0:
        score -= 2 * black
    if fierce_jump > 0:
        score -= 4 * fierce_jump - 4
    if (overtone > 0) and (overtone < 3):
        score += 1 + overtone
    return score


def unit_evaluation_ending(u):
    note_list = []
    last = 0
    for i in range(u.length):
        if u[i] is not None:
            note_list.append((i, u[i]))
            last = u[i]
    if len(note_list) == 0:
        return 0
    note_list.append((u.length, last))
    length_on_chord = 0
    fierce_jump = 0
    taboo_jump = 0
    bad_downbeat = 0
    bad_start = 0
    overtone = 0
    black = 0
    total_downbeat = 0
    for i in range(1, len(note_list)):
        x = note_list[i - 1]
        y = note_list[i]
        t_diff = y[0] - x[0]  # length
        p_diff = abs(y[1] - x[1])  # pitch difference
        if (x[1] % 12) in CHORD[u.chordID]:
            length_on_chord += t_diff
        if t_diff == 1:
            if p_diff > 4:
                fierce_jump += 1
            if (p_diff == 6) or (p_diff > 7):
                taboo_jump += 1
        elif t_diff == 2:
            if p_diff > 5:
                fierce_jump += 1
            if (p_diff in {6, 10, 11}) or (p_diff > 8):  # TODO optimize these constants
                taboo_jump += 1
        else:
            if p_diff > 7:
                fierce_jump += 1
            if (p_diff in {6, 10, 11}) or (p_diff > 12):
                taboo_jump += 1
        if DOWNBEAT[u.length].get(x[0], False):
            total_downbeat += DOWNBEAT[u.length][x[0]]
            if (x[1] % 12) not in CHORD[u.chordID]:  # downbeat out of chord
                bad_downbeat += DOWNBEAT[u.length][x[0]]
        if (i == 1) and (
                (x[0] != 0) or ((x[0] == 0) and ((x[1] % 12) not in CHORD[u.chordID]))):  # start pitch out of chord
            bad_start = 1
        if ((x[1] % 12) not in CHORD[u.chordID]) and ((y[1] % 12) in CHORD[u.chordID]):
            overtone += 1
        if (y[1] % 12) not in {0, 2, 4, 5, 7, 9, 11}:
            black += 1
    score = 50 - 8 * bad_start - 7 * taboo_jump
    if length_on_chord > u.length // 2:
        score += length_on_chord
    else:
        score += 3 * length_on_chord - u.length - 2
    if bad_downbeat > 0:
        score -= 3 * bad_downbeat - 2
    if total_downbeat * 2 + 1 < len(note_list):
        score -= 3 * (len(note_list) - total_downbeat * 2 - 1)
    if black > 0:
        score -= 2 * black
    if fierce_jump > 0:
        score -= 4 * fierce_jump - 4
    if (overtone > 0) and (overtone < 3):
        score += 1 + overtone
    score += note_list[-1][0] - note_list[-2][0]
    return score


def SA_optimize(u, t, t_delta, time, ending=False, vari=True):
    if ending:
        u.score = unit_evaluation_ending(u)
    else:
        u.score = unit_evaluation(u)
    for i in range(time):
        if vari:
            u_m = create_mutated_unit(u)
        else:
            u_m = create_same_rhythm_mutated_unit(u)
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
