from PyQt5.QtCore import QObject, pyqtSignal

class timeSignals(QObject):

    """ Class to emit signal, be careful using signal and add functions
       if you add 5000ms, second_elapsed signal will be emitted 5 times"""

    msecond_elapsed = pyqtSignal() # emitted each 100ms
    second_elapsed = pyqtSignal()  # emitted each 1s
    minute_elapsed = pyqtSignal()  # emitted each 1m
    hour_elapsed = pyqtSignal()    # emitted each 1h
    day_elapsed = pyqtSignal()     # emitted each 1d
    week_elapsed = pyqtSignal()    # emitted each 1w
 
class time(object): # this class is ussed manage the execution time of the app

    """ Class to handle the time from a timer, 
        it can count 'till weeks, principally use to emit signal """

    def __init__(self):
        self.signals = timeSignals()
        self.miliseconds = 0 # 1000ms = 1s
        self.seconds = 0 # 60 seconds = 1min
        self.minutes = 0 # 1min = 1hour
        self.hours = 0   # 24h = 1day
        self.days = 0    # 7 days = 1 wwek
        self.weeks = 0   

    def addMiliSeconds(self,value:int):
        self.miliseconds += value
        while value >= 100:
            value -= 100
            self.signals.msecond_elapsed.emit()

    def addSeconds(self,value:int):
        self.seconds += value
    
    def addMinutes(self,value:int):
        self.minutes += value
    
    def addHours(self,value:int):
        self.hours += value

    def addDays(self,value:int):
        self.days += value

    def addWeeks(self,value:int):
        self.weeks += value

    def restart(self):
        self.miliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.days = 0
        self.weeks= 0

    @property
    def miliseconds(self):
        return self.__miliseconds

    @miliseconds.setter
    def miliseconds(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__miliseconds = value
        while self.__miliseconds >= 1000:
            self.__miliseconds -= 1000
            self.seconds += 1
            self.signals.second_elapsed.emit()

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__seconds = value
        while self.__seconds >= 60:
            self.__seconds -= 60
            self.minutes += 1
            self.signals.minute_elapsed.emit()
            
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__minutes = value
        while self.__minutes >= 60:
            self.__minutes -= 60
            self.hours += 1
            self.signals.hour_elapsed.emit()

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self,value:int):
        if (value < 0):
            raise ValueError("cannot be more than 24 hours or negative")
        self.__hours = value
        while self.__hours >= 24 :
            self.__hours -= 24
            self.days += 1
            self.signals.hour_elapsed.emit()
        
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self,value:int):
        if (value < 0):
            raise ValueError("cannot be more than 31 days")
        self.__days = value
        while self.__days >= 7:
            self.__days -= 7
            self.weeks += 1
            self.signals.week_elapsed.emit()
        
    @property
    def weeks(self):
       return self.__weeks

    @weeks.setter
    def weeks(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__weeks = value
