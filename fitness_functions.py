# class for fitness functions , add your fitness function here !
import math
from settings import BIN, HIGH_PENALTY, PENALTY, LIV_DIST, KINDL_TAU
from numpy import unique
import numpy

hash_table = {}


class fitness_selector:
    def __init__(self):
        self.select = {0: self.distance_fittness, 1: self.bul_pqia,
                     'baldwin': self.baldwinss,
                       "fixed": self.fixed_distance}

    def distance_fittness(self, object, target, target_size):
        fitness = 0
        for j in range(target_size):
            fit = ord(object.object[j]) - ord(target[j])
            fitness += abs(fit)
        return fitness

    def bul_pqia(self, object, target, target_size):
        fitness = 0
        for i in range(target_size):
            if ord(object.object[i]) != ord(target[i]):
                fitness += PENALTY if object.object[i] in target else HIGH_PENALTY
        return fitness

    def euclidean_distance(self, object, target, target_size=0):
        # self explanitory
        sum_of_elements = 0
        for i in range(len(object)):
            if type(object[i]) == type(''):
                sum_of_elements += (ord(object[i]) - ord(target[i])) ** 2
            else:
                sum_of_elements += (object[i] - target[i]) ** 2
        return math.sqrt(sum_of_elements)

    def fixed_distance(self, object, target, target_size=0):
        correct = incorrect = 0

        for i in range(len(target)):
            if object[i] == target[i]:
                correct += 1
            elif object[i] != '?':
                incorrect += 1
        return correct, incorrect

    def baldwinss(self, pop_size, tries, num_tries):
        return 1 + ((pop_size - 1) * tries / num_tries)
