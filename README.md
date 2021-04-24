# Pyqt5 Module Notificator

A module create to generate pyqt5 desktop notification

installing using

pip install pyqt5-notificator

use:

fron notificator import notificator

from notificator.alingmentes import TopLeft,TopCenter,TopRight,BottomLeft,BottomCenter,BottomRight # just import what you need

instance

noft = notificator()

noft.critical("Title","Message",parent,Align,progressBar,duraccion,onclick,onleftclick,onrightclick)
