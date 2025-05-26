class Student:
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("The ID and name cannot be empty.")
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor_roll = False
        self.letter = "F"

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print(f"Ignoring invalid grade (not a number): {grade!r}")
            return
        if not (0 <= grade <= 100):
            print(f"Ignoring invalid grade (out of range 0–100): {grade}")
            return
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def determine_letter(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def evaluate_status(self):
        avg = self.calculate_average()
        self.is_passed = (avg >= 60)
        self.honor_roll = (avg >= 90)
        self.letter = self.determine_letter()

    def remove_grade_at(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Cannot remove grade at index {index}: out of range")

    def remove_grade_value(self, value):
        try:
            self.grades.remove(value)
        except ValueError:
            print(f"Cannot remove grade {value}: not found")

    def generate_report(self):
        self.evaluate_status()
        print(f"ID:               {self.id}")
        print(f"Name:             {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade:    {self.calculate_average():.2f}")
        print(f"Letter Grade:     {self.letter}")
        print(f"Pass/Fail:        {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll:       {self.honor_roll}")


def start_run():
    s = Student("1", "José Ramos")
    s.add_grade(100)
    s.add_grade(85)
    s.add_grade(150)     # Ignored
    s.add_grade("Fifty")  # Ignored
    s.remove_grade_value(85)
    s.remove_grade_at(5)  # Advice
    s.generate_report()


start_run()
