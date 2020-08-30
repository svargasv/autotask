from icalendar import Calendar
import calendar
from event import Event
from datetime import date,datetime,time
from operator import attrgetter
import html


events = list()

year = date.today().year

days_abrr=['MO','TH','WE','TU','FR','SA','SU']
def createCalendar():
    almanac = Calendar()
    with open('calendar.ics','rb') as f:
        almanac= Calendar.from_ical(f.read())


    for component in almanac.walk():
        #getting the info of each class
        if component.name == 'VEVENT':
            name=html.unescape(component.get('summary'))
            startDate=component.get('dtstart').dt
            endDate=component.get('dtend').dt
            daysWeek=component.get('rrule').get('byday')
            until=component.get('rrule').get('until')[0]
            end= date(until.year,until.month,until.day)
            act= date(startDate.year,startDate.month,startDate.day)
            startTime=time(startDate.hour,startDate.minute)
            endTime= time(endDate.hour,endDate.minute)
            #creating the numbers of events equals of the number of classes until it ends
            prueba1=daysWeek
            for weekday in daysWeek:
                while act <= end:
                    
                    diasemana=calendar.weekday(year,act.month,act.day)
                    if days_abrr[calendar.weekday(year,act.month,act.day)]== weekday:
                        
                        event= Event(str(name),act,startTime,endTime)
                        events.append(event)
                    act=checkdaymonth(act)
                act=date(startDate.year,startDate.month,startDate.day)

    
def checkdaymonth(act):
    x,numDays=calendar.monthrange(year,act.month)
    if act.day < numDays :

        act=date(act.year,act.month,act.day+1)
    else: 

        act = date(act.year,act.month+1,1)
    return act

def sortCalendar():
    events.sort(key= attrgetter('date','startTime'))
    print(events)
#TODO : Crear la estructura donde va a estar montada la información 
if __name__ == "__main__":
    createCalendar()
    sortCalendar()
    