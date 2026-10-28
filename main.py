"""
EduResults: Student Digital Examination and Result Management System
OOP1 assignment version.

This is a menu-driven console application. Records are stored in memory
using a dictionary and are cleared when the program exits.
"""

class Student:
    """Represents one student."""

    school_name = "EduResults Demonstration School"

    def __init__(self, student_id, full_name, class_name):
        self.student_id = student_id.strip().upper()
        self.full_name = full_name.strip()
        self.class_name = class_name.strip()
        self.examinations = {}

    def add_mark(self, subject, mark):
        """Add or update a subject mark for this student."""
        subject = subject.strip().title()
        if not subject:
            raise ValueError("Subject cannot be empty.")
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.examinations[subject] = mark

    def calculate_average(self):
        """Return the average of recorded subject marks, or None if no marks."""
        if not self.examinations:
            return None
        return sum(self.examinations.values()) / len(self.examinations)

    def get_grade(self, mark):
        """Return a grade using the demonstration grading scale."""
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        if mark >= 80:
            return "A"
        if mark >= 70:
            return "B"
        if mark >= 60:
            return "C"
        if mark >= 50:
            return "D"
        return "F"

    def display_details(self):
        """Display the student's basic details."""
        print(f"Student ID : {self.student_id}")
        print(f"Full name  : {self.full_name}")
        print(f"Class      : {self.class_name}")

    @classmethod
    def change_school_name(cls, new_name):
        """Change the shared school name for all Student objects."""
        if not new_name.strip():
            raise ValueError("School name cannot be empty.")
        cls.school_name = new_name.strip()


class Examination:
    """Provides examination-related calculations."""

    def __init__(self, title="General Examination"):
        self.title = title

    def calculate_total(self, marks):
        """Calculate the total of a sequence of marks."""
        return sum(marks)

    def calculate_average(self, marks):
        """Calculate the average of a sequence of marks."""
        if not marks:
            return None
        return sum(marks) / len(marks)


class ResultManagementSystem:
    """Stores and manages Student objects in a dictionary."""

    def __init__(self):
        # Dictionary data structure: student ID is the key, Student object is the value.
        self.students = {}
        self.examination = Examination()

    def add_student(self, student):
        """Register a Student object. Student IDs must be unique."""
        if student.student_id in self.students:
            raise ValueError("That student ID is already registered.")
        self.students[student.student_id] = student

    def find_student(self, student_id):
        """Find a student by ID; return None when not found."""
        return self.students.get(student_id.strip().upper())

    def display_all_students(self):
        """Display all registered students."""
        if not self.students:
            print("No students have been registered yet.")
            return
        for student in self.students.values():
            print("-" * 35)
            student.display_details()

    def record_mark(self, student_id, subject, mark):
        """Record a subject mark for a registered student."""
        student = self.find_student(student_id)
        if student is None:
            raise ValueError("Student ID was not found.")
        student.add_mark(subject, mark)

    def display_report_card(self, student_id):
        """Display a student's marks, grades, total and average."""
        student = self.find_student(student_id)
        if student is None:
            print("Student ID was not found.")
            return

        print("\n" + "=" * 42)
        print(self.examination.title)
        print(Student.school_name)
        print("=" * 42)
        student.display_details()
        print("-" * 42)

        if not student.examinations:
            print("No examination marks have been recorded.")
            return

        marks = list(student.examinations.values())
        for subject, mark in student.examinations.items():
            print(f"{subject:<22} {mark:>5.1f}   Grade: {student.get_grade(mark)}")

        total = self.examination.calculate_total(marks)
        average = self.examination.calculate_average(marks)
        overall_grade = student.get_grade(average)
        status = "PASS" if average >= 50 else "FAIL"

        print("-" * 42)
        print(f"{'Total':<22} {total:.1f} / {len(marks) * 100}")
        print(f"{'Average':<22} {average:.2f}%")
        print(f"{'Overall grade':<22} {overall_grade}")
        print(f"{'Overall status':<22} {status}")
        print("=" * 42)


def read_non_empty(prompt):
    """Ask until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_mark():
    """Ask for a valid mark from 0 to 100."""
    while True:
        try:
            mark = float(input("Enter mark (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number, for example 72 or 65.5.")


def show_menu():
    print("\n" + "=" * 48)
    print("EDURESULTS: STUDENT EXAMINATION SYSTEM")
    print("=" * 48)
    print("1. Register a student")
    print("2. Record examination marks")
    print("3. Display a student's report card")
    print("4. Search for a student")
    print("5. Display all students")
    print("6. Change school name (class method demo)")
    print("7. Exit")


def main():
    system = ResultManagementSystem()
    print(f"Welcome to {Student.school_name}")
    print("Note: records are stored only while this program is running.")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                student_id = read_non_empty("Student ID: ")
                full_name = read_non_empty("Full name: ")
                class_name = read_non_empty("Class: ")
                system.add_student(Student(student_id, full_name, class_name))
                print("Student registered successfully.")

            elif choice == "2":
                student_id = read_non_empty("Student ID: ")
                subject = read_non_empty("Subject: ")
                mark = read_mark()
                system.record_mark(student_id, subject, mark)
                print("Examination mark recorded successfully.")

            elif choice == "3":
                student_id = read_non_empty("Student ID: ")
                system.display_report_card(student_id)

            elif choice == "4":
                student_id = read_non_empty("Student ID to search: ")
                student = system.find_student(student_id)
                if student:
                    print("\nStudent found:")
                    student.display_details()
                else:
                    print("Student ID was not found.")

            elif choice == "5":
                system.display_all_students()

            elif choice == "6":
                new_name = read_non_empty("Enter the new school name: ")
                Student.change_school_name(new_name)
                print(f"School name updated to: {Student.school_name}")

            elif choice == "7":
                print("Thank you for using EduResults. Goodbye.")
                break

            else:
                print("Please choose a number from 1 to 7.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
