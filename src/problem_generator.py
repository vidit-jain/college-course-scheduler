from Timeslot import Timeslot, load_timeslots
from Teacher import Teacher, load_teachers
from Lesson import Lesson, load_lessons
from TimeTable import TimeTable
from Room import Room, load_rooms
from datetime import time
def generate_problem():
    timeslot_list = load_timeslots("timeslots.csv")
    # timeslot_list = [
    #     Timeslot(1, "MONDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
    #     Timeslot(2, "MONDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
    #     Timeslot(3, "MONDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
    #     Timeslot(4, "MONDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
    #     Timeslot(5, "MONDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
    #     Timeslot(6, "TUESDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
    #     Timeslot(7, "TUESDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
    #     Timeslot(8, "TUESDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
    #     Timeslot(9, "TUESDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
    #     Timeslot(10, "TUESDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
    # ]
    room_list = load_rooms("rooms.csv")
    prof_list = load_teachers("teachers2.csv")
    #[
    #       Teacher(1, "A. Turing", {timeslot_list[0], timeslot_list[1]}, {}),
    #       Teacher(2, "M. Curie", {timeslot_list[1], timeslot_list[2]}, {}),
    #       Teacher(3, "C. Darwin", {timeslot_list[3], timeslot_list[0]}, {}),
    #       Teacher(4, "I. Jones", {timeslot_list[0], timeslot_list[1]}, {}),
    #       Teacher(5, "P. Cruz", {timeslot_list[8], timeslot_list[9]}, {}),
    #        ]
    lesson_list = load_lessons("lesson.csv", prof_list)
    # lesson_list = [
    #     Lesson(1, "Math", {prof_list[0]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(2, "Math", {prof_list[0]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(3, "Physics", {prof_list[1]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(4, "Chemistry", {prof_list[1]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(5, "Biology", {prof_list[2]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(6, "History", {prof_list[2]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(7, "English", {prof_list[2]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(8, "English", {prof_list[2]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(9, "Spanish", {prof_list[3]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(10, "Spanish", {prof_list[3]}, 0, {"9th grade"}, 50, 1),
    #     Lesson(11, "Math", {prof_list[0]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(12, "Math", {prof_list[0]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(13, "Math", {prof_list[0]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(14, "Physics", {prof_list[1]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(15, "Chemistry", {prof_list[1]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(16, "French", {prof_list[1]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(17, "Geography", {prof_list[2]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(18, "History", {prof_list[2]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(19, "English", {prof_list[3]}, 0, {"10th grade"}, 50, 1),
    #     Lesson(20, "Spanish", {prof_list[3]}, 0, {"10th grade"}, 50, 1),
    # ]
    # lesson = lesson_list[0]
    # lesson.set_timeslot(timeslot_list[0])
    # lesson.set_room(room_list[0])

    return TimeTable(timeslot_list, room_list, prof_list, lesson_list)

