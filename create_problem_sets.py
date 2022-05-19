import random

from fitness_functions import fitness_selector
from mutations import mutations
import math


# have to fill hash table with different keys when getting the command from main


# basic class for all problem sets because fittness and the member of the population are problem specific
# ,and we have to eliminate problem specifc parameters from the Genetic algorithem
# might dd mutate !
def city_dist(city, neighbor):
    # calculates euclidean distance between two cities
    dx = city.x - neighbor.x
    dy = city.y - neighbor.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance


class Agent:
    fitnesstype = fitness_selector().select

    def __init__(self):
        self.object = []
        # self.learning_fitness = 0
        # self.algo_huristic = None
        self.age = 0
        self.fitness = 0
        self.solution = ""

    # creates a member of the population
    def create_object(self, target_size, target):
        return self.object

    def character_creation(self, target_size):
        pass

    def Learning_fitness(self, target, target_size, huristic):
        self.learning_fitness = self.fitnesstype[huristic](self, target, target_size)
        return self.learning_fitness

    # function to calculate the fitness for this specific problem

    def calculate_fittness(self, target, target_size, select_fitness, age_update=True):
        self.fitness = self.fitnesstype[select_fitness](self, target, target_size)
        self.age += 1 if age_update else 0
        return self.fitness

    def create_special_parameter(self, target_size):
        pass

    # for sorting purposes
    def __lt__(self, other):
        return self.fitness < other.fitness

    def __str__(self):
        bstr = ""
        for i in self.object:
            bstr += str(i) + ","
        bstr += self.solution
        return bstr

    def __repr__(self):
        bstr = ""
        for i in self.object:
            bstr += str(i) + " "
        return bstr

    # def __eq__(self, other):
    #     self.fitness = other.fitness
    #     self.object = other.object
    # age !
    def hash(self, other):
        return self.object


# class for first problem
class DNA(Agent):
    mutation = mutations()

    def __init__(self):
        Agent.__init__(self)
        self.diversity = 0
        # self.spiecy = 0
        self.networks_tested = 0

    def create_object(self, target_size, target):
        self.object = []
        for j in range(target_size):
            self.object += [self.character_creation(target_size)]
        self.create_special_parameter(target_size)
        return self.object

    def character_creation(self, target_size):
        return chr((random.randint(0, 90)) + 32)

    def mutate(self, target_size, member, mutation_type):
        self.mutation.select[mutation_type](target_size, member, self.character_creation)

    def hash(self, other):
        return ''.join(self.object + other.object)


class Sorting(DNA):
    def __init__(self):
        super(Sorting, self).__init__()

    def create_object(self, target_size, target):
        self.object = random.sample([i for i in range(1, target_size + 1)], target_size)


class network(DNA):
    def __init__(self):
        super(network, self).__init__()
        depth = 0

    def create_object(self, target_size, target):
        # todo define how to create the network
        for i in range(target_size):
            self.object.append(self.character_creation(target_size))

    def character_creation(self, target_size):
        pass

    def solve_network(self, set, pop):
        new_set = pop[set]
        # todo: think of what a comparator should be !
        for comperator in self.object:
            comperator(set)
        # if the solution is valid update diversity
        pop[set].diversity += 1 if self.check_solution(set) else 0
        pop[set].networks_tested += 1

    def check_solution(self, set):
        pass

    def apply(self, sets, pop):
        for set in sets:
            self.solve_network(set, pop)
        sum_of_sets = 0
        for set in sets:
            sum_of_sets += pop[set].diversity
        # we want the lower number
        self.fitness = 1-sum_of_sets / len(sets)



    def __str__(self):
        pass
