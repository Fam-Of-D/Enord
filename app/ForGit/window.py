import sys
from PyQt4.QtGui import * , QtCore

class Window (QtGui.QMainWindow) :
    def __init__ (self) :
        super (Window, self) .__init__()
        self.setGeometry(50 , 50 , 500 , 300 )
        self.setWindowTitle("Aeronyde!")
        self.setWindowIcon(QtGui.QIcon('roar AF'))

    self.show()


app =QtGui.QApplication (sys.argv)
GUI = Window()
sys.exit (app.exec_())
