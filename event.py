
class Event():

    def __init__ (self,name,date,startTime,endTime):
        self.name = name
        self.date= date
        self.startTime=startTime
        self.endTime=endTime

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return '{},{} \n'.format(self.date,self.name)