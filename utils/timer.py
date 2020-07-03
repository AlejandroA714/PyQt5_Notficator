from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from .time import time

class timer(QTimer):

    __instance = None # Instance of the timer; just can exists one on all the app
  
    def timerEvent(self,event):
        self.__time.addMiliSeconds(100)
        #print(self.__time.__dict__) # debug

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  QTimer.__new__(cls) 
            super(timer,cls.__instance).__init__()
            cls.__time = time()     
        return cls.__instance

    def startTimer(self):
        self.timerid = super(timer,self).startTimer(100)

    @classmethod
    def destroy(cls):
        cls.__instance = None
        cls.__time = None

    @property
    def signals(self):
        return self.__time.signals

    def close(self):
        self.destroy()
        self.killTimer(self.timerId())

    @property
    def time(self):
        return self.__time

