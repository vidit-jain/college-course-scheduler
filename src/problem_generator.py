from Timeslot import Timeslot, load_timeslots
from Teacher import Teacher, load_teachers
from Lesson import Lesson, load_lessons
from TimeTable import TimeTable
from Room import Room, load_rooms
from datetime import time
def generate_problem(timeslots_file, rooms_file, teachers_file, lessons_file):
    timeslot_list = load_timeslots(timeslots_file)
    room_list = load_rooms(rooms_file)
    prof_list = load_teachers(teachers_file)
    lesson_list = load_lessons(lessons_file, prof_list)
    return TimeTable(timeslot_list, room_list, prof_list, lesson_list)

