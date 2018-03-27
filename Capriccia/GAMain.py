# Main program running GA Model to generate an acceptable period
# Containing definitions of evaluation functions
# Version 1.0

from settings import *
from GAModel.period import unit, period
from GAModel.GA import GABase
import random

def unit_evaluation(u):
    '''
    TODO Implement unit_evaluation.
    :param u:
    :return:
    '''
    return 0

def period_evaluation(p):
    """
    TODO Optimize it.
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

init_generation = []
population = 35
period_length = 25
update_time = 45

for j in range(population):
    p = []
    for i in range(period_length):
        ran = random.randint(-3, 12)
        p.append(unit([ran]))
    p = period(p)
    init_generation.append(p)
model = GABase(0.6, 0.04, 0, 0, init_generation, unit_evaluation, period_evaluation)
for k in range(update_time):
    model.update_periods()
print('NoteList = ',end = '')
for i in range(period_length):
    print(model.generation[0][i][0], end=',')
print(' Score =',period_evaluation(model.generation[0]))