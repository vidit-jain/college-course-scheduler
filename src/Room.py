from optapy import problem_fact, planning_id
import csv

@problem_fact
class Room:
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return f"Room(name={self.name}, size={self.size})"


def load_rooms(file_name):
    room_list = []
    with open("../data/" + file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            id, name, size = row
            room_list.append(Room(int(id), name, int(size)))
    return room_list
