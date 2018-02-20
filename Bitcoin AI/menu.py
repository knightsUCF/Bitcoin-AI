
'''

import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout)


class Window(QWidget):


    def __init__(self):
        super().__init__()
        self.init_ui()
        self.settings = {} # add new data with .update({1:2})



    def init_ui(self):
        self.label_cryptocurrency = QLabel('Cryptocurrency:')
        cryptos = QVBoxLayout()
        cryptos.addWidget(self.label_cryptocurrency)
        self.btc = QRadioButton('Bitcoin')
        self.eth = QRadioButton('Ethereum')
        self.xrp = QRadioButton('Ripple')
        self.ltc = QRadioButton('Litecoin')
        cryptos.addWidget(self.btc)
        cryptos.addWidget(self.eth)
        cryptos.addWidget(self.xrp)
        cryptos.addWidget(self.ltc)
        
        self.label_timeframes = QLabel('Timeframe:')
        timeframes = QVBoxLayout()
        timeframes.addWidget(self.label_timeframes)
        self.day = QRadioButton('day')
        self.hour = QRadioButton('hour')
        self.minute = QRadioButton('minute')
        self.second = QRadioButton('second')
        timeframes.addWidget(self.day)
        timeframes.addWidget(self.hour)
        timeframes.addWidget(self.minute)
        timeframes.addWidget(self.second)
    
        
        




        self.setLayout(cryptos)
        self.setLayout(timeframes)

        self.show()






        

'''

'''
        
        self.lbl_1 = QLabel('Cryptocurrency: ')

        self.btc = QRadioButton('Bitcoin')
        self.eth = QRadioButton('Ethereum')
        self.xrp = QRadioButton('Ripple')
        self.ltc = QRadioButton('Litecoin')

        self.lbl_2 = QLabel('Timeframe for prediction: ')

        self.second = QRadioButton('second')
        self.minute = QRadioButton('minute')
        self.hour = QRadioButton('hour')
        self.day = QRadioButton('day')
        self.week = QRadioButton('week')
        self.month = QRadioButton('month')
        self.year = QRadioButton('year')


        self.btn = QPushButton('Select')


        # layout1 = QVBoxLayout()

        


        

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        win = QHBoxLayout()

        vbox.addWidget(self.lbl_1)
        vbox.addWidget(self.btc)
        vbox.addWidget(self.eth)
        vbox.addWidget(self.xrp)
        vbox.addWidget(self.ltc)

        # layout2 = QVBoxLayout()

        vbox.addWidget(self.lbl_2)
        vbox.addWidget(self.second)
        vbox.addWidget(self.minute)
        vbox.addWidget(self.hour)
        vbox.addWidget(self.day)
        vbox.addWidget(self.week)
        vbox.addWidget(self.month)
        vbox.addWidget(self.year)


        vbox.addWidget(self.btn)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)

        

        

        # self.setLayout(layout1)
        self.setWindowTitle('Cryptocurrency AI')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))

        # self.widgetList.append(win)
        self.show()

        '''
        '''

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('So its cats for you')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

'''

#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Brazil")
        radiobutton.setChecked(True)
        radiobutton.country = "Brazil"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Argentina")
        radiobutton.country = "Argentina"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Ecuador")
        radiobutton.country = "Ecuador"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 2)

    def on_radio_button_toggled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            print("Selected country is %s" % (radiobutton.country))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())




# '''

import sys
from PyQt4 import QtCore, QtGui

class Class1(QtGui.QMainWindow):
    def __init__(self):
        super(Class1, self).__init__()
        self.func()

    def func(self):
        layout=QtGui.QHBoxLayout()  # layout for the central widget
        widget=QtGui.QWidget(self)  # central widget
        widget.setLayout(layout)

        number_group=QtGui.QButtonGroup(widget) # Number group
        r0=QtGui.QRadioButton("0")
        number_group.addButton(r0)
        r1=QtGui.QRadioButton("1")
        number_group.addButton(r1)
        layout.addWidget(r0)
        layout.addWidget(r1)

        letter_group=QtGui.QButtonGroup(widget) # Letter group
        ra=QtGui.QRadioButton("a")
        letter_group.addButton(ra)
        rb=QtGui.QRadioButton("b")
        letter_group.addButton(rb)
        layout.addWidget(ra)
        layout.addWidget(rb)

        # assign the widget to the main window
        self.setCentralWidget(widget)
        self.show()





def main():
    app = QtGui.QApplication(sys.argv)
    mw = Class1()
    mw.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
'''



