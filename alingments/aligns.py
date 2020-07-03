from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtWidgets import QDesktopWidget

class Align():

    def __init__(self,Parent = None):
        if Parent is None:
            Parent = QDesktopWidget()
            Parent.setGeometry(Parent.x(),Parent.y(),Parent.width(),Parent.height()-50)
        self.parent = Parent

class TopLeft(Align):

    def __init__(self,Parent = None):
        super(TopLeft,self).__init__(Parent)

    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint(5,15+(120*multiplier))


class TopCenter(Align):
    
    def __init__(self,Parent = None):
        super(TopCenter,self).__init__(Parent)
        
    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint((size.width()-391)/2,15+(125*multiplier))

class TopRight(Align):

    def __init__(self,Parent = None):
        super(TopRight,self).__init__(Parent)
            
    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint(size.width()-391,15 + (125*multiplier))

class BottomLeft(Align):

    def __init__(self,Parent = None):
        super(BottomLeft,self).__init__(Parent)
        
    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint(5,size.height()-129-(120*multiplier))
    
class BottomCenter(Align):
    
    def __init__(self,Parent = None):
        super(BottomCenter,self).__init__(Parent)
        
    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint((size.width()-391)/2,(size.height()-129-(120*multiplier)))

class BottomRight(Align):

    def __init__(self,Parent = None):
        super(BottomRight,self).__init__(Parent)
        
    def coords(self,multiplier=0):
        size = self.parent.geometry()
        return QPoint(size.width()-391,size.height()-129-(120*multiplier))
