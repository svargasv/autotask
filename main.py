from icalendar import Calendar
import calendar
from event import Event
from datetime import date,datetime

events = list()

year = date.today().year

days_abrr=['MO','TH','WE','TU','FR','SA','SU']
def createCalendar():
    contador = 0
    almanac = Calendar()
    with open('calendar.ics','r') as f:
        almanac= Calendar.from_ical(f.read())


    for component in almanac.walk():
        #getting the info of each class
        if component.name == 'VEVENT':
            name=component.get('summary')
            startDate=component.get('dtstart').dt
            endTime=component.get('dtend').dt
            daysWeek=component.get('rrule').get('byday')
            until=component.get('rrule').get('until')[0]
            end= date(until.year,until.month,until.day)
            act= date(startDate.year,startDate.month,startDate.day)
            
            #creating the numbers of events equals of the number of classes until it ends
            for weekday in daysWeek:

                while act != end:

                    diasemana=calendar.weekday(year,act.month,act.day)
                    if days_abrr[calendar.weekday(year,act.month,act.day)]== weekday:

                        event= Event(name,act)
                        events.append(event)
                        contador=contador + 1
                    act=checkdaymonth(act)


def checkdaymonth(act):
    x,numDays=calendar.monthrange(year,act.month)
    if act.day < numDays :

        act=date(act.year,act.month,act.day+1)
    else: 

        act = datetime(act.year,act.month+1,1)
    return act

#TODO : Crear la estructura donde va a estar montada la información 
if __name__ == "__main__":
    createCalendar()
    