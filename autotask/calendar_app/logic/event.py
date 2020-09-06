
class Event():
    """Clase base que representa un evento
    """    
    def __init__ (self,name,date,startTime,endTime):
        """Constructor

        Args:
            name (string): Nombre del evento
            date (date): fecha del eveto
            startTime (time): hora de inicio del evento
            endTime (time): hora de fin del evento
        
        Metodos:
            getName(),getDate(),srt(),repr()
        """
        self.name = name
        self.date= date
        self.startTime=startTime
        self.endTime=endTime

    def getName(self):
        """Retorna el nombre del evento

        Returns:
            string: nombre
        """        
        return self.name

    def getDate(self):
        """Retorna la fecha del evento

        Returns:
            date: fecha
        """        
        return self.date

    def getTime(self):
        """Retorna la hora de inicio y de fin del evento

        Returns:
            tupla: Tupa que contiene en la posición la hora de inicio y en la posición dos la hora de fin
        """    
        return (self.startTime, self.endTime)

    def __str__(self):
        """str: nombre del evento

        Returns:
            string: nombre del evento
        """        
        return '{}'.format(self.name)

    def __repr__(self):
        """repr: fecha y nombre del evento

        Returns:
            string: fecha, nombre del evento 
        """        
        return '{},{} \n'.format(self.date,self.name)

    def toJSON(self):
        me = {
            'name': self.name,
            'date': str(self.date)
        }
        return me 