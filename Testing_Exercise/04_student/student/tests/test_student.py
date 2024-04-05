from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.test_student = Student("Ivan")
        self.test_student_with_courses = Student("Ivan2", {"Test2": ["Test1", "Test2"]})

    def test_init(self):
        self.assertEqual({}, self.test_student.courses)
        self.assertEqual("Ivan", self.test_student.name)
        self.assertEqual("Ivan2", self.test_student_with_courses.name)
        self.assertEqual({"Test2": ["Test1", "Test2"]}, self.test_student_with_courses.courses)

    def test_enroll_course_name_in_courses(self):
        self.test_student.courses["Test"] = ["notes"]
        test = self.test_student.enroll("Test", ["one", "two"], "Y")

        self.assertEqual("Course already added. Notes have been updated.", test)
        self.assertEqual(["notes", "one", "two"], self.test_student.courses["Test"])

    def test_enroll_course_notes_added(self):
        self.test_student.enroll("Test", "notes")
        test = self.test_student.enroll("Test2", ["zero"])
        test2 = self.test_student.enroll("Test3", ["one", "two"], "Y")

        self.assertEqual("Course and course notes have been added.", test2)
        self.assertEqual("Course and course notes have been added.", test)
        self.assertEqual(["zero"], self.test_student.courses["Test2"])
        self.assertEqual(["one", "two"], self.test_student.courses["Test3"])
        self.assertEqual({'Test': 'notes',
                          'Test2': ['zero'],
                          'Test3': ['one', 'two']},
                         self.test_student.courses)

    def test_enroll_courses_with_courses(self):
        result = self.test_student_with_courses.enroll("Test2", ["note1", "note2", "note3"])

        self.assertEqual(["Test1", "Test2", "note1", "note2", "note3"],
                         self.test_student_with_courses.courses["Test2"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Test2': ['Test1', 'Test2', 'note1', 'note2', 'note3']},
                         self.test_student_with_courses.courses)

    def test_enroll_courses_with_courses_return_added(self):
        result = self.test_student_with_courses.enroll("Not in", "none", "no")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.test_student_with_courses.courses["Not in"])

    def test_enroll_courses_with_courses_register_append_notes(self):
        result = self.test_student_with_courses.enroll("Test4", "notes", "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual("notes", self.test_student_with_courses.courses["Test4"])

    def test_enroll_new_course_added(self):
        test = self.test_student.enroll("Test3", [], "empty")

        self.assertEqual([], self.test_student.courses["Test3"])
        self.assertEqual("Course has been added.", test)

    def test_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.add_notes("None", "None")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_for_courses_with_courses(self):
        with self.assertRaises(Exception) as ex:
            self.test_student_with_courses.add_notes("None", "None")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_with_valid_key(self):
        self.test_student.courses = {"Test4": ["nothing"]}

        test = self.test_student.add_notes("Test4", "Hello")

        self.assertEqual("Notes have been updated", test)
        self.assertEqual(["nothing", "Hello"], self.test_student.courses["Test4"])

    def test_add_notes_for_courses_in_courses_with_valid_key(self):
        test = self.test_student_with_courses.add_notes("Test2", "Hello")

        self.assertEqual("Notes have been updated", test)
        self.assertEqual(["Test1", "Test2", "Hello"], self.test_student_with_courses.courses["Test2"])

    def test_leave_course_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_student.leave_course("Something")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_success(self):
        self.test_student.courses["Test"] = ["notes"]
        result = self.test_student.leave_course("Test")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.test_student.courses)


if __name__ == "__main__":
    main()