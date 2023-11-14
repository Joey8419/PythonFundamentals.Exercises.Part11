from enum import Enum


class AliveStatus(Enum):
    # Enum class with two symbolic names
    Deceased = 0
    Alive = 1


class Person:

    def __int__(self, first_name, last_name, dob, alive_status):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive_status = alive_status

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_alive_status(self, alive_status):
        self.alive_status = alive_status

        # Declare instructor class and class must inherit from Person class above
        class Instructor(Person):

            def __init__(self, first_name, last_name, dob, alive_status):
                # Call __init__ method of base class (Person)
                super().__init__(first_name, last_name, dob, alive_status)

                # Generate Universal Unique Identifier for instructor id
                self.instructor_id = f"Instructor Universal Unique Identifier (uuid)"

        class Student(Person):

            def __init__(self, first_name, last_name, dob, alive_status):
                # Call __init__ method of base class (Person)
                super().__init__(first_name, last_name, dob, alive_status)

            # Generate Universal Unique Identifier for instructor id
            self.instructor_id = f"Student Universal Unique Identifier (uuid)"

        class ZipCodeStudent(Student):
            # If 'ZipCodeStudent'  does not have any additional attributes or methods beyond what is has inherited
            # from the 'Student' class, then the method body remains empty:
            pass

        class CollegeStudent(Student):
            # If 'CollegeStudent'  does not have any additional attributes or methods beyond what is has inherited
            # from the 'Student' class, then the method body remains empty:
            pass

        class Classroom:

            def __init__(self):
                self.students = []
                self.instructors = []

            def add_student(self, student):
                self.students.append(student)

            def add_instructor(self, instructor):
                self.instructors.append(instructor)

            def remove_student(self, student):
                self.students.remove(student)

            def remove_instructor(self, instructor):
                self.instructors.remove(instructor)

            def print_students(self):
                for student in self.students:
                    print(f"Student: {student.first_name} {student.last_name}, ID: {Student.student_id}")

            def print_instructors(self):
                for instructor in self.instructors:
                    print(
                        f"Instructors: {instructor.first_name} {instructor.last_name}, ID: {Instructor.instructor_id}")
