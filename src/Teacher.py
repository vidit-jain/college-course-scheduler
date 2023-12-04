from optapy import problem_fact, planning_id
from Timeslot import Timeslot
import csv
@problem_fact
class Teacher:
    def __init__(self, id, name, blocked_timeslots, preferred_timeslots):
        self.id = id
        self.name = name
        self.blocked_timeslots = blocked_timeslots
        self.preferred_timeslots = preferred_timeslots 

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return f"Teacher(id={self.id}, name={self.name}, blocked_timeslots={self.blocked_timeslots}, preferred_timeslots={self.preferred_timeslots})"


def load_teachers(file_name):
    teacher_list = []
    with open("../data/" + file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            id, name, blocked_timeslots, preferred_timeslots = row
            if len(blocked_timeslots) > 2:
                blocked_timeslots = {int(element.strip()) for element in blocked_timeslots.split(",")}
            else:
                blocked_timeslots = {}

            if len(preferred_timeslots) > 2:
                preferred_timeslots = {int(element.strip()) for element in preferred_timeslots.split(",")}
            else:
                preferred_timeslots = {}
            teacher_list.append(Teacher(int(id), name, blocked_timeslots, preferred_timeslots))
    return teacher_list 
