################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################


'''
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



from ui_main import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #self.ui.label.setText()
 
        self.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


'''
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtWidgets, uic  
from PyQt5 import QtCore



class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()


        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        for child in self.findChildren(QWidget):
            shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
            child.setGraphicsEffect(shadow)

        uic.loadUi('main.ui', self)
        self.show()



        self.button = self.findChild(QtWidgets.QPushButton, 'close')
        self.button.clicked.connect(self.exit) 

        self.web = self.findChild(QtWidgets.QPushButton, 'web')
        self.web.setVerticalScrollBarEnabled(False)

    def exit(self):
        sys.exit()



    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = Ui()

    app.exec_()

