from settings import *
from GAModel.period import unit, period
import random
from copy import deepcopy
from GAModel.SA import SA_optimize


class GABase:
    def __init__(self, period_cross_rate, period_mutation_rate,
                 init_generation, period_evaluation):

        self.period_cross_rate = period_cross_rate
        self.period_mutation_rate = period_mutation_rate
        self.generation = []  # list of chromosomes (periods)
        self.population = len(init_generation)
        self.period_length = init_generation[0].length #the number of units each period contains
        self.unit_length = init_generation[0][0].length #the number of notes each unit contains
        self.period_evaluation = period_evaluation
        self.init_p_generation(init_generation)
        self.sum_score = 0.0
        self.best_period = None

    def init_p_generation(self, input_p_generation):
        self.generation = deepcopy(input_p_generation)

    def cross_periods(self, p1, p2):
        l1 = random.randint(0, self.period_length - 1)
        r1 = random.randint(0, self.period_length - 1)
        if l1 > r1:
            l1, r1 = r1, l1
        if p1 == p2:
            new_period = deepcopy(p1)
            return new_period
        l2 = random.randint(0, self.period_length - 1 - (r1 - l1))
        r2 = l2 + (r1 - l1)
        new_period = period()
        for i in range(l2):
            new_period.append(p2[i])
        for i in range(l1, r1 + 1):
            new_period.append(p1[i])
        for i in range(r2 + 1, self.period_length):
            new_period.append(p2[i])
        return new_period

    def cross_periods_v2(self, p1, p2):
        l1 = random.randint(0, self.period_length - 1)
        r1 = random.randint(0, self.period_length - 1)
        if l1 > r1:
            l1, r1 = r1, l1
        new_period = period()
        for i in range(l1):
            new_period.append(p2[i])
        for i in range(l1, r1 + 1):
            new_period.append(p1[i])
        for i in range(r1 + 1, self.period_length):
            new_period.append(p2[i])
        return new_period

    def mutate_period(self, p):
        ran = random.randint(0, self.period_length - 1)
        if ran == self.period_length - 1:
            p.units[ran] = SA_optimize(p.units[ran], 100, 0.95, 60, True)
        else:
            p.units[ran] = SA_optimize(p.units[ran], 100, 0.95, 60)
        return p

    def choose_period(self):
        '''
        TODO Implement other choosing functions and evaluate whether they are better.
        :return: A period chosen by "roulette wheel" method.
        '''
        ran = random.uniform(0, self.sum_score)
        for p in self.generation:
            ran -= p.score
            if ran <= 0:
                return p
        raise Exception('Error: Wrong sum_score.')

    def produce_period(self):
        '''
        :return: a generated period (using cross and mutation)
        '''
        p1 = self.choose_period()
        # Judge whether p1 crosses with another period
        ran = random.random()
        if ran < self.period_cross_rate:
            p2 = self.choose_period()
            new_period = self.cross_periods_v2(p1, p2)
        else:
            new_period = p1
        # Judge whether new_period mutates
        ran = random.random()
        if ran < self.period_mutation_rate:
            new_period = self.mutate_period(new_period)
        return new_period

    def update_periods(self):
        '''
        :return: a new generation of periods
        '''
        self.update_scores()
        new_generation = []
        new_generation.append(deepcopy(self.best_period))
        for i in range(self.population - 1):
            new_generation.append(self.produce_period())
        # self.environment_update()
        self.generation = new_generation

    def update_scores(self):
        self.sum_score = 0.0
        self.best_period = self.generation[0]
        for p in self.generation:
            p.score = self.period_evaluation(p)
            self.sum_score += p.score
            if self.best_period.score < p.score:
                self.best_period = p