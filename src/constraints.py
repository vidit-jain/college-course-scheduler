from Lesson import Lesson
from Room import Room
from Teacher import Teacher
from Timeslot import Timeslot
from optapy import constraint_provider
from optapy.constraint import Joiners, ConstraintFactory
from optapy.score import HardSoftScore
from config import *
import datetime
import csv
global_mat = []
def load_conflict_matrix(file_name):
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            global_mat.append([int(element) for element in row])

def cat_conflict_val(a, b):
    if (a > b):
        a, b = b, a
    return global_mat[a][b]

@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory):
    load_conflict_matrix("../data/conflictmatrix.csv")
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
        blocked_teacher(constraint_factory),
        small_class(constraint_factory),
        # Soft constraints are only implemented in the optapy-quickstarts code
        category_conflict(constraint_factory),
        overbooking_timeslot(constraint_factory),
        teacher_preference(constraint_factory),
        teacher_consecutive_classes(constraint_factory)
    ]

def neighboring_timeslot(timeslot1: Timeslot, timeslot2: Timeslot):
    a,b = timeslot1.start_time, timeslot1.end_time
    c,d = timeslot2.start_time, timeslot2.end_time
    date = datetime.date(2021, 5, 3)
    a = datetime.datetime.combine(date, a)
    b = datetime.datetime.combine(date, b)
    c = datetime.datetime.combine(date, c)
    d = datetime.datetime.combine(date, d)
    return (timeslot1.day_of_week == timeslot2.day_of_week and ((a > d and (a - d).total_seconds() < 1200) or (c > b and (c - b).total_seconds() < 1200)))
# Hard Constraints

# A room can accommodate at most one lesson at the same time.
def room_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  # ... in the same timeslot ...
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  # ... in the same room ...
                  Joiners.equal(lambda lesson: lesson.room),
                  # ... and the pair is unique (different id, no reverse pairs) ...
                  Joiners.less_than(lambda lesson: lesson.id)
                  # At least one of them is a full course, or they both fall in the same half
                  ).filter(lambda lesson1, lesson2: (lesson1.ctype == 0 or lesson2.ctype == 0) or (lesson1.ctype == lesson2.ctype)) \
            .penalize("Room conflict", penalties["room_concurrent_lessons"])


# Ensure the group of teachers for two lessons at the same time have no overlap 
def teacher_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
                .join(Lesson,
                      Joiners.equal(lambda lesson: lesson.timeslot),
                      Joiners.less_than(lambda lesson: lesson.id)
                  ).filter(lambda lesson1, lesson2: len(lesson1.prof_list.intersection(lesson2.prof_list)) > 0)\
                          .penalize("Teacher conflict", penalties["teacher_concurrent_lessons"])

# A student group with classes in the same time slot is infeasible 
def student_group_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.less_than(lambda lesson: lesson.id)
                  ).filter(lambda lesson1, lesson2: len(lesson1.student_groups.intersection(lesson2.student_groups)) > 0)\
                          .penalize("Student group conflict", penalties["students_concurrent_required_lessons"])

# A teacher cannot teach a lesson because it's in a blocked timeslot of theirs
def blocked_teacher(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson).\
            filter(lambda lesson : any(lesson.timeslot.id in prof.blocked_timeslots for prof in lesson.prof_list))\
            .penalize("Teacher blocked timeslot", penalties["teacher_blocked_timeslot"])

# A teacher cannot teach a lesson because it's in a blocked timeslot of theirs
def small_class(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson).\
            filter(lambda lesson : lesson.expected_students > lesson.room.size)\
            .penalize("Insufficient Capacity Room", penalties["insufficient_capacity_room"])

# Soft Constraints


# If two courses belonging to different categories clash, it causes a big conflict
def category_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.less_than(lambda lesson: lesson.id),
                  ).penalize("Different categories in same timeslot", HardSoftScore.ONE_SOFT,lambda lesson1, lesson2: cat_conflict_val(lesson1.category, lesson2.category))

# A general penalty applied if two courses have the same timing to incentivize not putting everything in one slot. 
def overbooking_timeslot(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.less_than(lambda lesson: lesson.id),
                  ).penalize("Multiple courses in one timeslot", penalties["concurrent_classes"])

# It's preferred to give teachers their time slot 
def teacher_preference(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson).\
            filter(lambda lesson : any(lesson.timeslot.id in prof.preferred_timeslots for prof in lesson.prof_list))\
            .reward("Teacher got a preferred time slot", rewards["teacher_preference"])

def teacher_consecutive_classes(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  Joiners.less_than(lambda lesson: lesson.id)
                  ).filter(lambda lesson1, lesson2: neighboring_timeslot(lesson1.timeslot, lesson2.timeslot) and len(lesson1.prof_list.intersection(lesson2.prof_list)) > 0)\
                          .penalize("Teacher has to teach two consecutive classes", penalties["teaching_consecutive_classes"])
