from optapy import problem_fact, planning_id
from datetime import datetime
import csv
@problem_fact
class Timeslot:
    def __init__(self, id, day_of_week, start_time, end_time):
        self.id = id
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return (
                f"Timeslot("
                f"id={self.id}, "
                f"day_of_week={self.day_of_week}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})"
        )

def load_timeslots(file_name):
    timeslot_list = []
    with open("../data/" + file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            id, day_of_week, start_time, end_time = row
            start_time = datetime.strptime(start_time, "%H:%M").time()
            end_time = datetime.strptime(end_time, "%H:%M").time()
            timeslot_list.append(Timeslot(int(id), day_of_week, start_time, end_time))
    return timeslot_list
