from Lesson import Lesson 
from TimeTable import TimeTable
from problem_generator import generate_problem
from constraints import define_constraints
import optapy.config
from optapy.types import Duration

solver_config = optapy.config.solver.SolverConfig() \
    .withEntityClasses(Lesson) \
    .withSolutionClass(TimeTable) \
    .withConstraintProviderClass(define_constraints) \
    .withTerminationSpentLimit(Duration.ofSeconds(30))

from optapy import solver_factory_create

solution = solver_factory_create(solver_config) \
    .buildSolver() \
    .solve(generate_problem())

print(solution)

print(type(solution))
