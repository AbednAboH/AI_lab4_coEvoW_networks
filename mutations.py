# class for mutations !!
import numpy

from settings import BIN
import random
class mutations:
    def __init__(self):
        self.select = {1: self.random_mutate, 2: self.swap_mutate, 3: self.insertion_mutate}

    def random_mutate(self, target_size, member, options):
        ipos = random.randint(0, target_size - 1)
        new_options = member.valid_insertion(ipos, options)
        delta = member.character_create(len(new_options),new_options)
        member.object = member.object[:ipos] + [delta] + member.object[ipos + 1:]



    def swap_mutate(self, target_size, member, character_creation):
        size=len(member.object)
        ipos = random.randint(0, size - 2)
        ipos2 = random.randint(ipos + 1, size - 1)
        member.object = member.object[:ipos] + [member.object[ipos2]] + member.object[ipos + 1:ipos2] + [
            member.object[ipos]] + member.object[ipos2 + 1:]

    def insertion_mutate(self, target_size, member, character_creation):
        size = len(member.object)
        ipos = random.randint(0, size - 2)
        ipos2 = random.randint(ipos + 1, size - 1)
        member.object = member.object[:ipos] + member.object[ipos + 1:ipos2] + [member.object[ipos]] + member.object[
                                                                                                       ipos2:]
