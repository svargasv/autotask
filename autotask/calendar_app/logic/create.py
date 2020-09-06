"""Logica para crear un calendario desde un archivo .ics

   
"""


from icalendar import Calendar
import calendar
from .event import Event
from datetime import date,datetime,time
from operator import attrgetter
import html
events = list()
year = date.today().year
days_abrr=['MO','TH','WE','TU','FR','SA','SU']
    
def createCalendar():
    """Crea un calendario a partir de un arreglo de objetos event

    Returns:
        array: Arreglo que contiene todos los eventos del calendario
    """
    almanac = Calendar()
    with open('calen.ics','rb') as f:
        almanac= Calendar.from_ical(f.read())

    for component in almanac.walk():
        #Extrayendo la información del evento
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
            #Creando una cantidad de eventos equivalente al numero de veces que el evento sucede hsata la fecha de terminación
            prueba1=daysWeek
            for weekday in daysWeek:
                while act <= end:
                    
                    diasemana=calendar.weekday(year,act.month,act.day)
                    if days_abrr[calendar.weekday(year,act.month,act.day)]== weekday:
                        print(str(name))
                        event= Event(str(name),act,startTime,endTime)
                        events.append(event)
                    act=checkdaymonth(act)
                act=date(startDate.year,startDate.month,startDate.day)

    return events

#TODO OpenEnglish 
def checkdaymonth(act):
    """[Verifica si la varible act esta en el ultimo dia del mes, aumenta el mes en 1 y vuelve al primer día de ser así, de lo contrario aumenta en 1 el día ]

    Args:
        act ([date]): [Representa el apuntador a una fecha]

    Returns:
        [act]: [ Representa el nuevo apuntador a una fecha aumentada en 1 día ]
    """    

    x,numDays=calendar.monthrange(year,act.month)
    if act.day < numDays :

        act=date(act.year,act.month,act.day+1)
    else: 

        act = date(act.year,act.month+1,1)
    return act


def sortCalendar():
    """[Ordena los eventos del arreglo de forma ascendente por efecha y hora de inicio]
    """    
    events.sort(key= attrgetter('date','startTime'))

if __name__ == "__main__":
   createCalendar() 