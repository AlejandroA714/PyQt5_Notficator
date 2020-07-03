from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QEvent,QRect, QPropertyAnimation, QAbstractAnimation, QTimer, QEvent
from alingments import TopRight
from resources import *

class notifySignals(QObject):

    left_click = pyqtSignal(object)
    right_click = pyqtSignal(object)
    double_click = pyqtSignal(object)
    close = pyqtSignal(object)
    parent_resize = pyqtSignal()

class UINotificationModal(QDialog):

    def __init__(self,Title:str,Message:str,Parent:QMainWindow = None, Align = TopRight, 
                 progressBar = False,backgroundColor = "#17a2b8",foregroundColor="#FFFFFF",icon=":/source/img/infoNotify.png",multiplier = 1,duracion=15):
        self.Parent = Parent
        self.signals = notifySignals()
        self.progressBar = progressBar
        self.Aling = Align
        self.coords = Align(Parent).coords
        self.title = Title
        self.msg = Message
        self.multiplier = multiplier
        self.bg = backgroundColor
        self.fg = foregroundColor
        self.icon = icon
        self.duracion = duracion
        self.focus = False
        QDialog.__init__(self,Parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # removes borders
        self.setAttribute(Qt.WA_TranslucentBackground) # Making it translucent to make a trick with the shadows
        self.setAttribute( Qt.WA_DeleteOnClose) # this should liberate ram
        if not self.Parent is None:
            try:
                self.Parent.signals.resize.connect(self.resizeNotify)
            except:
                pass
        self.setupUi()
        
    def setupUi(self):
        self.NotificationModal = self
        self.NotificationModal.setObjectName("NotificationModal")
        self.NotificationModal.setWindowModality(QtCore.Qt.WindowModal)
        self.NotificationModal.resize(391, 129)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NotificationModal.sizePolicy().hasHeightForWidth())
        self.NotificationModal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.NotificationModal.setFont(font)
        self.NotificationModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.NotificationModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NotificationModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.NotificationModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(self.NotificationModal)
        self.MainFrame.setMinimumSize(QtCore.QSize(240, 110))
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2)
        self.MainFrame.setGraphicsEffect(self.shadow)
        
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.lblIcon = QtWidgets.QLabel(self.MainFrame)
        self.lblIcon.setGeometry(QtCore.QRect(7, 21, 70, 81))
        self.lblIcon.setText("")
        
        self.lblIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIcon.setObjectName("lblIcon")
        self.lblTitleScroll = QtWidgets.QScrollArea(self.MainFrame)
        self.lblTitleScroll.setGeometry(QtCore.QRect(75, 10, 151, 24))
        self.lblTitleScroll.setMinimumSize(QtCore.QSize(65, 20))
        self.lblTitleScroll.setMaximumSize(QtCore.QSize(167772, 167772))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitleScroll.setFont(font)
        self.lblTitleScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitleScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitleScroll.setLineWidth(0)
        self.lblTitleScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lblTitleScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblTitleScroll.setWidgetResizable(True)
        self.lblTitleScroll.setObjectName("lblTitleScroll")
        self.lblTitleScroll.setStyleSheet("background-color:transparent;")
        self.ScrollTitleLayout = QtWidgets.QWidget()
        self.ScrollTitleLayout.setGeometry(QtCore.QRect(0, 0, 151, 24))
        self.ScrollTitleLayout.setObjectName("ScrollTitleLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.ScrollTitleLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.txtNombre = QtWidgets.QLabel(self.ScrollTitleLayout)
        self.txtNombre.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtNombre.setFont(font)
        self.txtNombre.setLineWidth(0)
        self.txtNombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txtNombre.setWordWrap(True)
        self.txtNombre.setIndent(5)
        self.txtNombre.setObjectName("txtNombre")
        self.vboxlayout.addWidget(self.txtNombre)
        self.lblTitleScroll.setWidget(self.ScrollTitleLayout)
        self.lblContentScroll = QtWidgets.QScrollArea(self.MainFrame)
        self.lblContentScroll.setGeometry(QtCore.QRect(75, 35, 271, 64))
        self.lblContentScroll.setMinimumSize(QtCore.QSize(65, 20))
        self.lblContentScroll.setMaximumSize(QtCore.QSize(167772, 167772))
        self.lblContentScroll.setStyleSheet("background-color:transparent;")
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblContentScroll.setFont(font)
        self.lblContentScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblContentScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblContentScroll.setLineWidth(0)
        self.lblContentScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lblContentScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblContentScroll.setWidgetResizable(True)
        self.lblContentScroll.setObjectName("lblContentScroll")
        self.ScrollContentLayout = QtWidgets.QWidget()
        self.ScrollContentLayout.setGeometry(QtCore.QRect(0, 0, 271, 64))
        self.ScrollContentLayout.setObjectName("ScrollContentLayout")
        self._2 = QtWidgets.QVBoxLayout(self.ScrollContentLayout)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        self.txtContent = QtWidgets.QLabel(self.ScrollContentLayout)
        self.txtContent.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtContent.setFont(font)
        
        self.txtContent.setLineWidth(0)
        self.txtContent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.txtContent.setWordWrap(True)
        self.txtContent.setIndent(5)
        self.txtContent.setObjectName("txtContent")
        self._2.addWidget(self.txtContent)
        self.lblContentScroll.setWidget(self.ScrollContentLayout)
        self.btnExit = QtWidgets.QPushButton(self.MainFrame)
        self.btnExit.setGeometry(QtCore.QRect(345, 5, 24, 24))
        self.btnExit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/exitNotify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")        
        self.verticalLayout.addWidget(self.MainFrame)
        QtCore.QMetaObject.connectSlotsByName(self.NotificationModal)

        self.btnExit.clicked.connect(self.close)

        # set the color
        self.MainFrame.setStyleSheet("background-color:%s;" % self.bg)

        # set the foregroundColor

        self.txtContent.setStyleSheet("color:%s;" % self.fg)
        self.txtNombre.setStyleSheet("color:%s;background-color:transparent;" % self.fg)

        # progress bar

        if self.progressBar and not self.duracion is None:
            self.progressBar = QtWidgets.QProgressBar(self.MainFrame)
            self.progressBar.setGeometry(QtCore.QRect(0, 105, 371, 5))
            self.progressBar.setStyleSheet("QProgressBar {border: none;background-color:transparent;} QProgressBar::chunk {background-color: #A9A9A9;width: 20px;}")
            self.progressBar.setProperty("value", 100)
            self.progressBar.setFormat("")
            self.progressBar.setObjectName("progressBar")
            self.animBar = QPropertyAnimation(self.progressBar, b"value")
            self.animBar.setDuration(self.duracion*1000)
            self.animBar.setStartValue(100)
            self.animBar.setEndValue(0)
            self.animBar.start(QAbstractAnimation.DeleteWhenStopped)
            self.animBar.finished.connect(self.close)
        
        if not self.progressBar and not self.duracion is None:
            QTimer.singleShot(self.duracion*1000,self.close)
        
        # set the icon

        self.lblIcon.setPixmap(self.icon)
        self.lblIcon.setScaledContents(False)

        #set the text

        self.txtNombre.setText(self.title)
        self.txtContent.setText(self.msg)
        self.txtContent.setWordWrap(True)

        # set the location
        self.NotificationModal.setGeometry(self.coords(self.multiplier).x(),self.coords(self.multiplier).y(),391,128)

        # handle over and leave mouse event

    def updateLocation(self):
        self.animLocation = QPropertyAnimation(self.NotificationModal, b"geometry")
        self.animLocation.setDuration(100)
        self.animLocation.setStartValue(QRect(self.coords(self.multiplier).x(),self.coords(self.multiplier).y(), 391, 128))
        self.multiplier -= 1
        self.animLocation.setEndValue(QRect(self.coords(self.multiplier).x(),self.coords(self.multiplier).y(), 391, 128))
        self.animLocation.start(QAbstractAnimation.DeleteWhenStopped)

    def enterEvent(self,evt):
        self.focus=True

    def leaveEvent(self,evt):
        self.focus=False
     
    def mousePressEvent(self,evt):
        self.clickCount = 1

    def mouseReleaseEvent(self,evt):
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import QTimer
        if self.clickCount == 1:
            QTimer.singleShot(QApplication.doubleClickInterval(),self.perfomClickAction)
       
    def mouseDoubleClickEvent(self,evt):
        self.clickCount = 2
        print("2 click")

    def perfomClickAction(self):
        if self.clickCount == 1:
           print("1 click")

    def resizeNotify(self):
        self.NotificationModal.setGeometry(self.coords(self.multiplier).x(),self.coords(self.multiplier).y(),391,128)
            
    def close(self):
        self.signals.close.emit(self)
        if not self.Parent is None:
            try:
               self.Parent.signals.resize.disconnect(self.resizeNotify)
            except:
                pass

    def sizeHint(self):
        return QtCore.QSize(391,129)

