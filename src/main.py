from Lesson import Lesson 
from TimeTable import TimeTable
from problem_generator import generate_problem
from constraints import define_constraints
import optapy.config
from optapy.types import Duration
import argparse


argParser = argparse.ArgumentParser()
argParser.add_argument("-ts", "--timeslots", help="CSV File path containing timeslots related information", required=True)
argParser.add_argument("-r", "--rooms", help="CSV File path containing rooms related information", required=True)
argParser.add_argument("-te", "--teachers", help="CSV File path containing teachers related information", required=True)
argParser.add_argument("-l", "--lessons", help="CSV File path containing lessons related information", required=True)
argParser.add_argument("-s", "--seconds", help="Duration you want to run the program for", type=int, required=True)

args = argParser.parse_args()

solver_config = optapy.config.solver.SolverConfig() \
    .withEntityClasses(Lesson) \
    .withSolutionClass(TimeTable) \
    .withConstraintProviderClass(define_constraints) \
    .withTerminationSpentLimit(Duration.ofSeconds(args.seconds))

from optapy import solver_factory_create

solution = solver_factory_create(solver_config) \
    .buildSolver() \
    .solve(generate_problem(args.timeslots, args.rooms, args.teachers, args.lessons))
print("Schedule written to \"final_timetable\"")
