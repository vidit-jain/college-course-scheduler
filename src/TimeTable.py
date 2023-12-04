from optapy import planning_solution, planning_entity_collection_property, \
                   problem_fact_collection_property, \
                   value_range_provider, planning_score
from optapy.score import HardSoftScore
from Timeslot import Timeslot
from Room import Room
from Lesson import Lesson
from Teacher import Teacher
import sys
def format_list(a_list):
    return ',\n'.join(map(str, a_list))

def time_table_printer(self):
    a = dict()
    orig_stdout = sys.stdout
    with open('final_timetable', 'w') as file:
        sys.stdout = file   
        for lesson in self.lesson_list:
            if lesson.timeslot not in a:
                a[lesson.timeslot] = []
            a[lesson.timeslot].append(lesson)
        for k, v in a.items():
            print(k.day_of_week, " ", k.start_time, " ", k.end_time)
            for r in v:
                print(r.subject)
    sys.stdout = orig_stdout

@planning_solution
class TimeTable:
    def __init__(self, timeslot_list, room_list, teacher_list, lesson_list, score=None):
        self.timeslot_list = timeslot_list
        self.room_list = room_list
        self.teacher_list = teacher_list
        self.lesson_list = lesson_list
        self.score = score

    @problem_fact_collection_property(Timeslot)
    @value_range_provider("timeslotRange")
    def get_timeslot_list(self):
        return self.timeslot_list

    @problem_fact_collection_property(Teacher)
    @value_range_provider("teacherRange")
    def get_teacher_list(self):
        return self.teacher_list

    @problem_fact_collection_property(Room)
    @value_range_provider("roomRange")
    def get_room_list(self):
        return self.room_list

    @planning_entity_collection_property(Lesson)
    def get_lesson_list(self):
        return self.lesson_list

    @planning_score(HardSoftScore)
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


    def __str__(self):
        time_table_printer(self)
        return (
            f"TimeTable("
            f"timeslot_list={format_list(self.timeslot_list)},\n"
            f"room_list={format_list(self.room_list)},\n"
            f"teacher_list={format_list(self.teacher_list)},\n"
            f"lesson_list={format_list(self.lesson_list)},\n"
            f"score={str(self.score.toString()) if self.score is not None else 'None'}"
            f")"
        )

