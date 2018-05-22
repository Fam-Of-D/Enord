import sys
#from PyQt4.QtGui import *
from PyQt4 import QtGui 



class Window(QtGui.QMainWindow):
        def __init__ (self) :
            super (Window, self) .__init__()
            self.setGeometry(50 , 50 , 500 , 300 )
            self.setWindowTitle("Aeronyde!")
            self.setWindowIcon(QtGui.QIcon('roar AF'))

            self.show ()


            extractAction = QtGui.Application ("Go nigga no" , self)
            extractAction.setShortcut ("corey")
            extractAction.setStatusTip('leave the app')
            extractAction.triggered.connect (self.close_application)

            self.statusBar()

            mainMenu = self.menuBar ()
            fileMenu = mainMenu.addMenu ('&File')
            fileMenu.addAction(extractAction)

"""
            self.home ()


        def home (self) :
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
            btn.move(0, 100)

"""


            #mainMenu   =