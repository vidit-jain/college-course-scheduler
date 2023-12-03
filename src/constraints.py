from Lesson import Lesson
from Room import Room
from Teacher import Teacher
from optapy import constraint_provider
from optapy.constraint import Joiners, ConstraintFactory
from optapy.score import HardSoftScore

@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory):
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
        blocked_teacher(constraint_factory),
        small_class(constraint_factory)
        # Soft constraints are only implemented in the optapy-quickstarts code
    ]

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
             ) \
            .penalize("Room conflict", HardSoftScore.ONE_HARD)


# Ensure the group of teachers for two lessons at the same time have no overlap 
def teacher_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
                .join(Lesson,
                      Joiners.equal(lambda lesson: lesson.timeslot),
                      Joiners.less_than(lambda lesson: lesson.id)
                  ).filter(lambda lesson1, lesson2: len(lesson1.prof_list.intersection(lesson2.prof_list)) > 0)\
                          .penalize("Teacher conflict", HardSoftScore.ONE_HARD)

# A student group with classes in the same time slot is infeasible 
def student_group_conflict(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson) \
            .join(Lesson,
                  Joiners.equal(lambda lesson: lesson.timeslot),
                  Joiners.less_than(lambda lesson: lesson.id)
                  ).filter(lambda lesson1, lesson2: len(lesson1.student_groups.intersection(lesson2.student_groups)) > 0)\
                          .penalize("Student group conflict", HardSoftScore.ONE_HARD)

# A teacher cannot teach a lesson because it's in a blocked timeslot of theirs
def blocked_teacher(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson).\
            filter(lambda lesson : any(lesson.timeslot in prof.blocked_timeslots for prof in lesson.prof_list))\
            .penalize("Teacher blocked timeslot", HardSoftScore.ONE_HARD)

# A teacher cannot teach a lesson because it's in a blocked timeslot of theirs
def small_class(constraint_factory: ConstraintFactory):
    return constraint_factory.for_each(Lesson).\
            filter(lambda lesson : lesson.expected_students > lesson.room.size)\
            .penalize("Insufficient Capacity Room", HardSoftScore.ONE_HARD)


