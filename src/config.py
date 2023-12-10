from optapy.score import HardSoftScore
penalties = {
    "room_concurrent_lessons": HardSoftScore.ONE_HARD,
    "teacher_concurrent_lessons": HardSoftScore.ONE_HARD, 
    "students_concurrent_required_lessons": HardSoftScore.ONE_HARD,
    "teacher_blocked_timeslot": HardSoftScore.ONE_HARD, 
    "insufficient_capacity_room": HardSoftScore.ONE_HARD, 
    "concurrent_classes": HardSoftScore.ofSoft(10),
    "teaching_consecutive_classes": HardSoftScore.ofSoft(10),
} 
rewards = {
    "teacher_preference": HardSoftScore.ofSoft(10)
}

