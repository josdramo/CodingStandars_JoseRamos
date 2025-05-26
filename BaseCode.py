class student:

    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcAverage(self):
        t = 0
        for x in self.gradez:
            t += x
        if len(self.gradez) > 0:
            avg = t/len(self.gradez)
        else:
            avg = 0
        return avg

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honbr = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startRun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcAverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startRun()
