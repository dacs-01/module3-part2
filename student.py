class stu(object):

    name = ''
    GPA = 0.0

    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA

    def get_name(self):
        return self.name

    def get_GPA(self):
        return self.GPA

    def report_GPA(self):
        return self.get_name() + ' has a GPA of ' + str(self.get_GPA())
    