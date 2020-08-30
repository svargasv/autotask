
class Event():

    def __init__ (self,name,date):
        self.name = name
        self.date= date

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def __str__(self):
        return '{}'.format(self.name)
