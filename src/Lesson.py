from optapy import planning_entity, planning_variable, planning_id
from Timeslot import Timeslot
from Room import Room
@planning_entity
class Lesson:
    def __init__(self, id, subject, prof_list, ctype, student_groups, expected_students, category, timeslot=None, room=None):
        self.id = id
        self.ctype = ctype
        self.subject = subject
        self.prof_list = prof_list
        self.student_groups = student_groups
        self.timeslot = timeslot
        self.room = room
        self.expected_students = expected_students
        self.category = category 

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
