from discrete_dimension import Position, Velocity
from utils import fitness
from solver import Solver
import numpy as np
import random
from math import comb
import datetime


def random_swap(n: int):
    num_swaps = np.random.randint(1, n//2 + 1)
    swaps: list[tuple[int, int]] = []

    for _ in range(num_swaps):
        i: int
        j: int
        i, j = np.random.randint(0, n, 2)
        swaps.append((i, j))
    
    return swaps


class Particle:
    def __init__(self, num_queens: int):

        self.position = Position()
        self.position.values = np.random.permutation([i+1 for i in range(num_queens)]).tolist()

        self.velocity = Velocity()
        self.velocity.values = random_swap(num_queens)

        self.best = (self.position, fitness(self.position.values))
        
        self.alpha = 1.3
        self.beta = 2.3
        self.omega = 0.8

    def update(self, cbest: Position):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)

        inertia = self.omega * self.velocity
        cognitive = self.alpha * r1 * (self.best[0] - self.position)
        social = self.beta * r2 * (cbest - self.position)

        self.velocity = inertia + cognitive + social
        self.position = self.position + self.velocity

        fit = fitness(self.position.values)
        # print(f"position = {self.position}")

        if fit > self.best[1]:
            self.best = (self.position, fit)

class PSOSolver(Solver):
    def __init__(self, num_queens: int):
        super().__init__(num_queens)

        self.particle_number = 20
        self.swarm = [Particle(num_queens) for _ in range(self.particle_number)]

        self.solution_fitness = comb(8, 2)

    def update_best(self, best: tuple[Position, int]):
        best_aux = best

        for particle in self.swarm:
            if particle.best[1] > best_aux[1]:
                best_aux = (particle.best[0], particle.best[1])
        
        return best_aux

    def convergence_criteria(self, best: tuple[Position, int]):
        count = 0

        for part in self.swarm:
            if part.best[1] == best[1]:
                count = count + 1

        return (best[1] == self.solution_fitness and count >= self.particle_number/2)

    def solve(self):
        best_particle = self.swarm[0]

        best = self.update_best(best_particle.best)

        while not self.convergence_criteria(best):
            self.iterations += 1
            #t0 = datetime.datetime.now()
            for particle in self.swarm:
                particle.update(best[0])
            #t1 = datetime.datetime.now()
            #print(f"delta = {t1 - t0}")
            best = self.update_best(best)

        self.solution = best[0].values

