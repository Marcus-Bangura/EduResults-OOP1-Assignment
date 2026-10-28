"""Simple checks for core EduResults functionality."""
from main import Student, Examination, ResultManagementSystem

def run_tests():
    system = ResultManagementSystem()
    student = Student("ER-001", "Aminata Kamara", "SSS 2A")
    system.add_student(student)
    system.record_mark("ER-001", "Mathematics", 75)
    system.record_mark("ER-001", "English", 65)

    assert system.find_student("er-001") is student
    assert student.calculate_average() == 70
    assert student.get_grade(75) == "B"
    assert Examination().calculate_total([75, 65]) == 140

    try:
        system.add_student(Student("ER-001", "Duplicate Student", "SSS 2A"))
    except ValueError:
        pass
    else:
        raise AssertionError("Duplicate student ID should be rejected.")

    print("All EduResults checks passed.")

if __name__ == "__main__":
    run_tests()
