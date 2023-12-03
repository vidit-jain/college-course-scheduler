from Timeslot import Timeslot
from Teacher import Teacher
from Lesson import Lesson
from TimeTable import TimeTable
from Room import Room
from datetime import time
def generate_problem():
    timeslot_list = [
        Timeslot(1, "MONDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(2, "MONDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(3, "MONDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(4, "MONDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(5, "MONDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
        Timeslot(6, "TUESDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(7, "TUESDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(8, "TUESDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(9, "TUESDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(10, "TUESDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
    ]
    room_list = [
        Room(1, "Room A", 250),
        Room(2, "Room B", 30),
        Room(3, "Room C", 120)
    ]
    teacher_list = [
           Teacher(1, "A. Turing", {timeslot_list[0], timeslot_list[1]}, {}),
           Teacher(2, "M. Curie", {timeslot_list[1], timeslot_list[2]}, {}),
           Teacher(3, "C. Darwin", {timeslot_list[3], timeslot_list[0]}, {}),
           Teacher(4, "I. Jones", {timeslot_list[0], timeslot_list[1]}, {}),
           Teacher(5, "P. Cruz", {timeslot_list[8], timeslot_list[9]}, {}),
            ]
    lesson_list = [
        Lesson(1, "Math", {teacher_list[0]}, 0, {"9th grade"}, 50, 1),
        Lesson(2, "Math", {teacher_list[0]}, 0, {"9th grade"}, 50, 1),
        Lesson(3, "Physics", {teacher_list[1]}, 0, {"9th grade"}, 50, 1),
        Lesson(4, "Chemistry", {teacher_list[1]}, 0, {"9th grade"}, 50, 1),
        Lesson(5, "Biology", {teacher_list[2]}, 0, {"9th grade"}, 50, 1),
        Lesson(6, "History", {teacher_list[2]}, 0, {"9th grade"}, 50, 1),
        Lesson(7, "English", {teacher_list[2]}, 0, {"9th grade"}, 50, 1),
        Lesson(8, "English", {teacher_list[2]}, 0, {"9th grade"}, 50, 1),
        Lesson(9, "Spanish", {teacher_list[3]}, 0, {"9th grade"}, 50, 1),
        Lesson(10, "Spanish", {teacher_list[3]}, 0, {"9th grade"}, 50, 1),
        Lesson(11, "Math", {teacher_list[0]}, 0, {"10th grade"}, 50, 1),
        Lesson(12, "Math", {teacher_list[0]}, 0, {"10th grade"}, 50, 1),
        Lesson(13, "Math", {teacher_list[0]}, 0, {"10th grade"}, 50, 1),
        Lesson(14, "Physics", {teacher_list[1]}, 0, {"10th grade"}, 50, 1),
        Lesson(15, "Chemistry", {teacher_list[1]}, 0, {"10th grade"}, 50, 1),
        Lesson(16, "French", {teacher_list[1]}, 0, {"10th grade"}, 50, 1),
        Lesson(17, "Geography", {teacher_list[2]}, 0, {"10th grade"}, 50, 1),
        Lesson(18, "History", {teacher_list[2]}, 0, {"10th grade"}, 50, 1),
        Lesson(19, "English", {teacher_list[3]}, 0, {"10th grade"}, 50, 1),
        Lesson(20, "Spanish", {teacher_list[3]}, 0, {"10th grade"}, 50, 1),
    ]
    # lesson = lesson_list[0]
    # lesson.set_timeslot(timeslot_list[0])
    # lesson.set_room(room_list[0])

    return TimeTable(timeslot_list, room_list, lesson_list)

