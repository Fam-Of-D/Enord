#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
a = QApplication(sys.argv)
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Set window size.
w.resize(1000, 1000)
 
# Set window title
w.setWindowTitle("Wha wha WHY HELLER!!!!!")

# Add a button
btn = QPushButton('!!!   Heller @_o!', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(100, 80)
 

btn = QPushButton('Where wHy Whem?Q!?!?!!', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(40, 50)


btn = QPushButton(' BALL Is Life ? ', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(225, 80)

btn = QPushButton('VIRAAAAAAAAAAAAAAAJJJJJJJJJJJJ', w)
btn.setToolTip('Click to quit!')
btn.clicked.connect(exit)
btn.resize(btn.sizeHint())
btn.move(20, 80)


# Show window
w.show()
 
sys.exit(a.exec_())