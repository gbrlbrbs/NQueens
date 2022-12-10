from pso import PSOSolver
from de import DESolver

print("Solving for 8 queens\n")
print("PSO")
algorithm = PSOSolver(8)
algorithm.solve()
pso_solution = algorithm.get_solution()

print("Particle Swarm Optimization (PSO) Solution")
print(pso_solution)
print("\n")

print("DE")
algorithm = DESolver(8)
algorithm.solve()
de_solution = algorithm.get_solution()

print("Differential Evolution (DE) Solution")
print(de_solution)
print("\n\n")