# sams_package/student.py
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


# sams_package/faculty.py
class Faculty:
    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name

    def __str__(self):
        return f"{self.name} [ID: {self.faculty_id}]"


# sams_package/course.py
class Course:
    def __init__(self, code, title, credits=0):
        self.code = code
        self.title = title
        self.credits = credits

    def __str__(self):
        return f"{self.title} ({self.code}) - {self.credits} credits"


# sams_package/result.py
def compile_result(student, marks_list):
    if not marks_list:  # safe guard
        return {"roll_no": student.roll_no, "total": 0, "average": 0.0}
    total = sum(marks_list)
    average = round(total / len(marks_list), 2)
    return {"roll_no": student.roll_no, "total": total, "average": average}


# sams_package/__init__.