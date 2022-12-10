from solver import Solver
from utils import fitness
import numpy as np
import random
from math import comb

class DESolver(Solver):
    def __init__(self, num_queens: int):
        super().__init__(num_queens)
        self.scale = 0.6
        self.genome_number = 50
        self.crossover = 0.5
        self.max_iterations = 1000

        self.solution = num_queens * [0]
        self.solution_fitness = comb(8, 2)
        self.genomes: list[list[int]] = [np.random.randint(1, num_queens+1, size=num_queens).tolist() for _ in range(self.genome_number)]

    def generate_donor(self, g1: list[int], g2: list[int], g3: list[int]):
        bound_value = lambda x: 8 if x > 8 else x if x >= 0 else 0
        donor: list[int] = []
        g_len = len(g1)

        for i in range(g_len):
            nv = g1[i] + self.scale * (g2[i] - g3[i])
            nv = int(nv + 0.5)
            nv = bound_value(nv)
            donor.append(nv)

        return donor

    def generate_trial(self, g: list[int], donor: list[int]):
        trial: list[int] = []

        for i, d in enumerate(donor):
            if random.uniform(0, 1) < self.crossover:
                trial.append(d)
            else:
                trial.append(g[i])

        return trial

    def convergence_criteria(self):
        return (fitness(self.solution) == self.solution_fitness)

    def solve(self):
        while not self.convergence_criteria():
            self.iterations += 1
            for i, genom in enumerate(self.genomes):
                gi1, gi2, gi3 = np.random.randint(0, self.genome_number, 3)
                g1, g2, g3 = self.genomes[gi1], self.genomes[gi2], self.genomes[gi3]
                donor = self.generate_donor(g1, g2, g3)
                trial = self.generate_trial(genom, donor)
                trial_fitness = fitness(trial)
                if fitness(genom) < trial_fitness:
                    self.genomes[i] = trial
                    if fitness(self.solution) < trial_fitness:
                        self.solution = trial
            
            if self.iterations > self.max_iterations:
                break
