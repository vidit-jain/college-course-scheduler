from optapy import planning_entity, planning_variable, planning_id
from Timeslot import Timeslot
from Room import Room
from Teacher import Teacher
import csv
@planning_entity
class Lesson:
    def __init__(self, id, subject, prof_list, ctype, student_groups, expected_students, category, timeslot=None, room=None):
        self.id = id
        self.ctype = ctype
        self.subject = subject
        self.prof_list = prof_list
        self.student_groups = student_groups
        self.expected_students = expected_students
        self.category = category 
        self.timeslot = timeslot
        self.room = room

    @planning_id
    def get_id(self):
        return self.id

    @planning_variable(Timeslot, ["timeslotRange"])
    def get_timeslot(self):
        return self.timeslot

    def set_timeslot(self, new_timeslot):
        self.timeslot = new_timeslot

    @planning_variable(Room, ["roomRange"])
    def get_room(self):
        return self.room

    def set_room(self, new_room):
        self.room = new_room

    def __str__(self):
        return (
            f"Lesson("
            f"id={self.id}, "
            f"timeslot={self.timeslot}, "
            f"room={self.room}, "
            f"subject={self.subject}, "
            f")"
        )


def load_lessons(file_name, prof_list):
    lesson_list = []
    with open("../data/"+file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            id, subject, prof_ids, ctype, student_groups, expected_students, category = row
            id = int(id)
            prof_ids = {prof_list[int(i.strip())] for i in prof_ids.split(",")} 
            ctype = int(ctype)
            if len(student_groups) > 2:
                student_groups = {x for x in student_groups.split(",")}
            else:
                student_groups = set()
            expected_students = int(expected_students)
            category = int(category)
            lesson_list.append(Lesson(id, subject, prof_ids, ctype, student_groups, expected_students, category))
    return lesson_list 
