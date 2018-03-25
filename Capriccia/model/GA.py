from setting import *


class Chromosome:
    # TODO initialization
    def __init__(self,):
        self.genes = []
        self.chromosome_length = 0
        self.score = 0


class GABase:
    def __init__(self, cross_rate, mutation_rate, generation_count, chromosome_length, init_p_generation,
                 evaluation_func=lambda chromosome: 1):
        """
        TODO better initialization way
        :param cross_rate:
        :param mutation_rate:
        :param generation_count:
        :param chromosome_length:
        :param evaluation_func:
        """
        self.cross_rate = cross_rate
        self.mutation_rate = mutation_rate
        self.gene_database = []
        self.generation = []  # list of Chromosome
        self.generation_count = generation_count
        self.chromosome_length = chromosome_length
        self.evaluation_func = evaluation_func
        self.generation_score = 0

        self.init_p_generation(init_p_generation)

    def init_p_generation(self, input_p_generation):
        """
        TODO define the initialization way for group, may not all by inputting
        :param input_p_generation:
        :return:
        """
        # self.generation = input_p_generation
        pass

    def init_environment(self):
        """
        TODO initialize environment including following variables
        :return:
        """
        # self.cross_rate = self.cross_rate
        # self.mutation_rate = self.mutation_rate
        # self.gene_database = self.gene_database
        # self.chromosome_length = self.chromosome_length
        # self.evaluation_func = self.evaluation_func
        pass

    def update(self):
        self.evolve()
        self.environment_update()
        self.natural_selection()

    def evolve(self):
        """
        TODO except cross and mutate, other evolution may occur
        :return:
        """
        self.cross()
        self.mutate()
        self.generation_count += 1

    def cross(self):
        """
        TODO do the cross between the generation
        :return:
        """
        # self.generation = self.generation
        # self.gene_database = self.gene_database
        pass

    def mutate(self):
        """
        TODO do the mutation between the generation
        :return:
        """
        # self.generation = self.generation
        # self.gene_database = self.gene_database
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

    def natural_selection(self):
        """
        Update generation_score and select new generation according to evaluation_function
        TODO update the generation
        :return:
        """
        for chromosome in self.generation:
            chromosome.score = self.evaluation_func(chromosome)
        try:
            # self.generation = self.generation  # TODO select chromosome in generation
            # self.gene_database = self.gene_database  # TODO after selection, update self.gene_database
            self.update_gen_score()
        except ZeroDivisionError:
            print("All chromosomes in the generation were eliminated by the environment.")
            # self.generation = self.generation  # TODO: revert this evolution, this should happen before self.evolve()

    def update_gen_score(self):
        """
        Update self.generation_score according to current self.generation
        :return:
        """
        gen_score = 0
        for chromosome in self.generation:
            gen_score += chromosome.score
        gen_score /= len(self.generation)

    def output_if(self, condition=lambda gen_score, gen: gen_score >= 1):
        """
        Interface
        output an result if the condition is satisfied
        :param condition: function, default self.generation_score >= 1
        :return: self.generation
        """
        while not condition(self.generation_score, self.generation):
            self.update()
        return self.generation
