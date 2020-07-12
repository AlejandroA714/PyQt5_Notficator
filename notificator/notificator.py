from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QApplication
from notificator.alingments import TopLeft,TopCenter,TopRight,BottomLeft,BottomCenter,BottomRight, Align
from notificator.UI import UINotificationModal

class notificator(QObject):

    __instance = None
    __instanced = False

    def __new__(cls):
        if cls.__instance is None :
            cls.__instance =  QObject.__new__(cls) 
            super(notificator,cls.__instance).__init__()
        return cls.__instance

    def __init__(self):
        if not self.__instanced:
            self.UIContainer = dict()
            self.UIContainer[TopLeft] = dict()
            self.UIContainer[TopCenter] = dict()
            self.UIContainer[TopRight] = dict()
            self.UIContainer[BottomLeft] = dict()
            self.UIContainer[BottomCenter] = dict()
            self.UIContainer[BottomRight] = dict()
            self.__instanced = True

    def critical(self,Title:str,Message:str,Parent:QMainWindow=None,Align:Align=TopRight,progressBar=False,duracion=15,onclick=None,ondoubleclick=None,onrightclick=None):
        if not Parent in self.UIContainer[Align]:
            self.UIContainer[Align][Parent] = []
        UI = UINotificationModal(Title,Message,Parent,Align,progressBar,
                                backgroundColor="#dc3545",icon=QPixmap(":/source/img/errorNotify.png"),multiplier=len(self.UIContainer[Align][Parent]),duracion=duracion)
        UI.signals.close.connect(self.updateUI)
        if not onclick is None:
            UI.signals.left_click.connect(onclick)
        if not ondoubleclick is None:
            UI.signals.double_click.connect(ondoubleclick)
        if not onrightclick is None:
            UI.signals.right_click.connect(onrightclick)
        UI.show()
        self.UIContainer[Align][Parent].append(UI)

    def warning(self,Title:str,Message:str,Parent=None,Align:Align=TopRight,progressBar=False,duracion=15,onclick=None,ondoubleclick=None,onrightclick=None):
        if not Parent in self.UIContainer[Align]:
            self.UIContainer[Align][Parent] = []
        UI = UINotificationModal(Title,Message,Parent,Align,progressBar,
                                backgroundColor="#ffc107",icon=QPixmap(":/source/img/warningNotify.png"),multiplier=len(self.UIContainer[Align][Parent]),duracion=duracion)
        UI.signals.close.connect(self.updateUI)
        if not onclick is None:
            UI.signals.left_click.connect(onclick)
        if not ondoubleclick is None:
            UI.signals.double_click.connect(ondoubleclick)
        if not onrightclick is None:
            UI.signals.right_click.connect(onrightclick)
        UI.show()
        self.UIContainer[Align][Parent].append(UI)

    def sucess(self,Title:str,Message:str,Parent=None,Align:Align=TopRight,progressBar=False,duracion=15,onclick=None,ondoubleclick=None,onrightclick=None):
        if not Parent in self.UIContainer[Align]:
            self.UIContainer[Align][Parent] = []
        UI = UINotificationModal(Title,Message,Parent,Align,progressBar,
                                backgroundColor="#28a745",icon=QPixmap(":/source/img/successNotify.png"),multiplier=len(self.UIContainer[Align][Parent]),duracion=duracion)
        UI.signals.close.connect(self.updateUI)
        if not onclick is None:
            UI.signals.left_click.connect(onclick)
        if not ondoubleclick is None:
            UI.signals.double_click.connect(ondoubleclick)
        if not onrightclick is None:
            UI.signals.right_click.connect(onrightclick)
        UI.show()
        self.UIContainer[Align][Parent].append(UI)
    
    def info(self,Title:str,Message:str,Parent=None,Align:Align=TopRight,progressBar=False,duracion=15,onclick=None,ondoubleclick=None,onrightclick=None):
        if not Parent in self.UIContainer[Align]:
            self.UIContainer[Align][Parent] = []
        UI = UINotificationModal(Title,Message,Parent,Align,progressBar,
                                backgroundColor="#17a2b8",icon=QPixmap(":/source/img/infoNotify.png"),multiplier=len(self.UIContainer[Align][Parent]),duracion=duracion)
        UI.signals.close.connect(self.updateUI)
        if not onclick is None:
            UI.signals.left_click.connect(onclick)
        if not ondoubleclick is None:
            UI.signals.double_click.connect(ondoubleclick)
        if not onrightclick is None:
            UI.signals.right_click.connect(onrightclick)
        UI.show()
        self.UIContainer[Align][Parent].append(UI)

    def custom(self,Title:str,Message:str,backgroundColor:str,foregroundColor:str,icon:QPixmap,Parent=None,Align:Align=TopRight,progressBar:bool=False,duracion=15,onclick=None,ondoubleclick=None,onrightclick=None):
        if not Parent in self.UIContainer[Align]:
            self.UIContainer[Align][Parent] = []
        UI = UINotificationModal(Title,Message,Parent,Align,progressBar,backgroundColor,foregroundColor,icon,multiplier=len(self.UIContainer[Align][Parent]),duracion=duracion)
        UI.signals.close.connect(self.updateUI)
        if not onclick is None:
            UI.signals.left_click.connect(onclick)
        if not ondoubleclick is None:
            UI.signals.double_click.connect(ondoubleclick)
        if not onrightclick is None:
            UI.signals.right_click.connect(onrightclick)
        UI.show()
        self.UIContainer[Align][Parent].append(UI)
    
    def updateUI(self,UINotifity):
        UIs = list(filter(lambda UI: UI.multiplier > UINotifity.multiplier,self.UIContainer[UINotifity.Aling][UINotifity.Parent] ))
        self.UIContainer[UINotifity.Aling][UINotifity.Parent].remove(UINotifity)
        UINotifity.deleteLater()
        for UI in UIs:
            UI.updateLocation()

    @classmethod
    def destroy(cls):
        cls.__instance = None
        cls.__instanced = False

    def close(self):
        self.destroy()


