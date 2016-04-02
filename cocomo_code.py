from PyQt4 import QtGui  
import sys  
import cocomo 
import math 
import os  


class CocomoApp(QtGui.QMainWindow, cocomo.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.a = self.b = self.c = self.d = 0
        self.setupUi(self)  
        self.values()
        self.pushButton.clicked.connect(self.calculate)  
                                                            
    def values(self):
        if self.radioButton.isChecked() == False : 
            self.a = 2.4
            self.b = 1.05
            self.c = 2.5
            self.d = 0.38

        if self.radioButton_2.isChecked() == False : 
            self.a = 3.0
            self.b = 1.12
            self.c = 2.5
            self.d = 0.35

        if self.radioButton_3.isChecked() == False : 
            self.a = 3.6
            self.b = 1.20
            self.c = 2.5
            self.d = 0.32

    def calculate(self):
        loc = long(self.textEdit.toPlainText())
        effort = self.a * math.pow(loc, self.b)
        dtime = self.c * math.pow(effort, self.d)
        staff = effort/dtime
        self.label_6.setText(str(round(effort)) + " person-months")
        self.label_6.setStyleSheet('color: green') 
        self.label_7.setText(str(round(dtime)) + " months")
        self.label_7.setStyleSheet('color: green')
        self.label_8.setText(str(round(staff)) + " person")
        self.label_8.setStyleSheet('color: green')


def main():
    app = QtGui.QApplication(sys.argv)  
    form = CocomoApp()  
    form.show()  
    sys.exit(app.exec_())  


if __name__ == '__main__':  
    main()  