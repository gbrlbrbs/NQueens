from abc import ABC, abstractmethod
from utils import fitness

class Solver(ABC):

    def __init__(self, num_queens: int):
        self.num_queens = num_queens
        self.iterations = 0
        self.max_iterations = 1000
        self.solution_fitness = None
        self.solution = None

    @abstractmethod
    def solve(self):
        pass

    def get_solution(self):
        return self.solution, fitness(self.solution), self.iterations