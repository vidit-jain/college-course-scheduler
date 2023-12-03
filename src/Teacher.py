from optapy import problem_fact, planning_id
from Timeslot import Timeslot

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
        return f"Room(id={self.id}, name={self.name}, blocked_timeslots={self.blocked_timeslots}, preferred_timeslots={self.preferred_timeslots})"
