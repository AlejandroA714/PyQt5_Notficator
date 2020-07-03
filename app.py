from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import UINotificationModal
from utils import timer
from alingments import BottomLeft,BottomCenter,BottomRight,TopCenter,TopLeft,TopRight
from notificator import notificator
from uuid import uuid4
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal,QObject

class application(QApplication):

    def __init__(self,*args):
        super(application,self).__init__(*args)

class signals(QObject):
    resize = pyqtSignal()
        
class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow,self).__init__()
        self.signals = signals()
        self.setupUI()

    def setupUI(self):
        main = self
        main.resize(1366,720)
        notf = notificator()

        notf.critical(Title="¡Hola Mundo 1",Message="¡Alerta! Variable \"Variable 1\" ha lanzado una alerta",Parent=self,Align=TopLeft,progressBar=False,duracion=5)
        notf.critical(Title="¡Hola Mundo 2",Message="¡Alerta! Variable \"Variable 2\" ha lanzado una alerta",Parent=self,Align=TopLeft,progressBar=False,duracion=10)
        notf.critical(Title="¡Hola Mundo 3",Message="¡Alerta! Variable \"Variable 3\" ha lanzado una alerta",Parent=self,Align=TopLeft,progressBar=False,duracion=15)
        notf.critical(Title="¡Hola Mundo 4",Message="¡Alerta! Variable \"Variable 4\" ha lanzado una alerta",Parent=None,Align=TopLeft,progressBar=False,duracion=20)
        notf.critical(Title="¡Hola Mundo 5",Message="¡Alerta! Variable \"Variable 5\" ha lanzado una alerta",Parent=self,Align=TopLeft,progressBar=False,duracion=25)
         
        notf.sucess(Title="¡Hola Mundo 1",Message="¡Alerta! Variable \"Variable 1\" ha lanzado una alerta",Parent=None,Align=TopCenter,progressBar=False,duracion=5)
        notf.sucess(Title="¡Hola Mundo 2",Message="¡Alerta! Variable \"Variable 2\" ha lanzado una alerta",Parent=None,Align=TopCenter,progressBar=False,duracion=10)
        notf.sucess(Title="¡Hola Mundo 3",Message="¡Alerta! Variable \"Variable 3\" ha lanzado una alerta",Parent=None,Align=TopCenter,progressBar=False,duracion=15)
        notf.sucess(Title="¡Hola Mundo 4",Message="¡Alerta! Variable \"Variable 4\" ha lanzado una alerta",Parent=self,Align=TopCenter,progressBar=False,duracion=20)
        notf.sucess(Title="¡Hola Mundo 5",Message="¡Alerta! Variable \"Variable 5\" ha lanzado una alerta",Parent=None,Align=TopCenter,progressBar=False,duracion=25)
    
        notf.info(Title="¡Hola Mundo 1",Message="¡Alerta! Variable \"Variable 1\" ha lanzado una alerta",Parent=None,Align=TopRight,progressBar=False,duracion=5)
        notf.info(Title="¡Hola Mundo 2",Message="¡Alerta! Variable \"Variable 2\" ha lanzado una alerta",Parent=None,Align=TopRight,progressBar=False,duracion=10)
        notf.info(Title="¡Hola Mundo 3",Message="¡Alerta! Variable \"Variable 3\" ha lanzado una alerta",Parent=self,Align=TopRight,progressBar=False,duracion=15)
        notf.info(Title="¡Hola Mundo 4",Message="¡Alerta! Variable \"Variable 4\" ha lanzado una alerta",Parent=None,Align=TopRight,progressBar=False,duracion=20)
        notf.info(Title="¡Hola Mundo 5",Message="¡Alerta! Variable \"Variable 5\" ha lanzado una alerta",Parent=self,Align=TopRight,progressBar=False,duracion=25)
    
    def resizeEvent(self,evt):
        self.signals.resize.emit()

    def updateUI(self,reponse):
        print(reponse)

    def closeEvent(self,evt):
        QApplication.quit()


if __name__ == "__main__":
    app = application([])
    notificator(app)
    main = mainWindow()
    main.show()
    app.exec()

    