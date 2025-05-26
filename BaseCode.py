class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.isPassed = False
        self.honor = False

    def addGrade(self, g):
        if isinstance(g, (int, float)):
            self.grades.append(g)
        else:
            print(f"Ignoring invalid grade: {g!r}")

    def calculateAverage(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def honorStatus(self):
        if self.calculateAverage() > 90:
            self.honor = True

    def removeGradeAt(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Cannot delete grade at index {index}: out of range")

    def generateReport(self):  # broken format
        print("ID: ", self.id)
        print("Your Name is: ", self.name)
        print("Grades Count: ", len(self.grades))
        print("Your Final Grade is: ", self.calculateAverage())
        print("Your Honor is: ", self.honor)


def startRun():
    a = Student("x", "José Ramos")
    a.addGrade(100)
    a.addGrade("Fifty")  # broken
    a.calculateAverage()
    a.honorStatus()
    a.removeGradeAt(5)  # IndexError
    a.generateReport()


startRun()
