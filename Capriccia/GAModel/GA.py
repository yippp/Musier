from settings import *
from GAModel.period import unit, period
import random
from copy import deepcopy

class GABase:
    def __init__(self, period_cross_rate, period_mutation_rate,
                 unit_cross_rate, unit_mutation_rate,
                 init_generation, unit_evaluation=lambda u:0, period_evaluation=lambda p:0):

        self.period_cross_rate = period_cross_rate
        self.period_mutation_rate = period_mutation_rate
        self.unit_cross_rate = unit_cross_rate
        self.unit_mutation_rate = unit_mutation_rate
        self.generation = []  # list of chromosomes (periods)
        self.population = len(init_generation)
        self.period_length = init_generation[0].length #the number of units each period contains
        self.unit_length = init_generation[0][0].length #the number of notes each unit contains
        self.unit_evaluation = unit_evaluation
        self.period_evaluation = period_evaluation
        self.init_p_generation(init_generation)
        self.sum_score = 0.0
        self.best_period = None

        #self.generation_score = 0

    def init_p_generation(self, input_p_generation):
        self.generation = deepcopy(input_p_generation)

    def cross_periods(self, p1, p2):
        l1 = random.randint(0, self.period_length - 1)
        r1 = random.randint(0, self.period_length - 1)
        if l1 > r1:
            l1, r1 = r1, l1
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

    def mutate_period(self, p):
        """
        TODO Update is with one or more mutation methods (reverse, change_chord, etc.)
        :param p:
        :return:
        """
        ran = random.randint(0, self.period_length - 1)
        new_period = p
        new_period[ran].notes[0] += random.randint(-5, 5)
        return new_period

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
        TODO Try adding unit_level variation in this method.
        :return: A period instance produced by cross and mutation.
        '''
        p1 = self.choose_period()

        # Judge whether p1 crosses with another period
        ran = random.random()
        if ran < self.period_cross_rate:
            p2 = self.choose_period()
            new_period = self.cross_periods(p1, p2)
        else:
            new_period = p1

        # Judge whether new_period mutates
        ran = random.random()
        if ran < self.period_mutation_rate:
            new_period = self.mutate_period(new_period)
        return new_period

    def update_periods(self):
        self.update_scores()
        new_generation = []
        new_generation.append(deepcopy(self.best_period))
        for i in range(self.population - 1):
            new_generation.append(self.produce_period())
        # self.environment_update()
        self.generation = new_generation

    def cross_units(self):
        """
        TODO do the cross between the units
        """
        pass

    def mutate_unit(self):
        """
        TODO do the mutation of a unit
        """
        pass

    def environment_update(self):
        """
        TODO update following variables
        :return:
        """
        # self.cross_rate = self.cross_rate
        # self.mutation_rate = self.mutation_rate
        # self.gene_database = self.gene_database
        # self.chromosome_length = self.chromosome_length
        # self.evaluation_func = self.evaluation_func
        pass

    def update_scores(self):
        self.sum_score = 0.0
        self.best_period = self.generation[0]
        for p in self.generation:
            for u in p:
                u.score = self.unit_evaluation(u)
            p.score = self.period_evaluation(p)
            self.sum_score += p.score
            if self.best_period.score < p.score:
                self.best_period = p

    # def natural_selection(self):
    #     """
    #     Update generation_score and select new generation according to evaluation_function
    #     TODO update the generation
    #     :return:
    #     """
    #     for chromosome in self.generation:
    #         chromosome.score = self.evaluation_func(chromosome)
    #     try:
    #         # self.generation = self.generation  # TODO select chromosome in generation
    #         # self.gene_database = self.gene_database  # TODO after selection, update self.gene_database
    #         self.update_gen_score()
    #     except ZeroDivisionError:
    #         print("All chromosomes in the generation were eliminated by the environment.")
    #         # self.generation = self.generation  # TODO: revert this evolution, this should happen before self.evolve()