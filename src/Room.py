from optapy import problem_fact, planning_id

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
        return f"Room(id={self.id}, name={self.name}, size={self.size})"
