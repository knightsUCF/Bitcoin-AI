#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys
import main






class Window(QWidget):
    def __init__(self):

        self.SYMBOL = "USDT_BTC"
        self.UNIT = "day"


        QWidget.__init__(self)


        self.setWindowTitle('Crypto AI')

        layout = QGridLayout()
        self.setLayout(layout)

        self.label_cryptocurrency = QLabel('Cryptocurrency:')
        layout.addWidget(self.label_cryptocurrency)

        radiobutton = QRadioButton("Bitcoin")
        radiobutton.setChecked(True)
        radiobutton.crypto = "Bitcoin"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 1, 0)

        radiobutton = QRadioButton("Ethereum")
        radiobutton.crypto = "Ethereum"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 2, 0)

        radiobutton = QRadioButton("Ripple")
        radiobutton.crypto = "Ripple"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 3, 0)

        radiobutton = QRadioButton("Litecoin")
        radiobutton.crypto = "Litecoin"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 4, 0)

        self.label_timeframe = QLabel('Timeframe:')
        layout.addWidget(self.label_timeframe)

        self.checkbox1 = QCheckBox("Daily")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 6, 0)

        self.checkbox2 = QCheckBox("Hourly")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 7, 0)

        self.checkbox3 = QCheckBox("Minute")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 8, 0)

        self.okay_button = QPushButton("Calculate")
        layout.addWidget(self.okay_button)

        self.result = QLabel('')
        layout.addWidget(self.result)

        self.okay_button.clicked.connect(self.btn_click)



    def on_radio_button_toggled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            print("Selected crypto is %s" % (radiobutton.crypto))

        if radiobutton.crypto is "Bitcoin":
            self.SYMBOL = 'USDT_BTC'
        if radiobutton.crypto is "Litecoin":
            self.SYMBOL = 'USDT_LTC'
        if radiobutton.crypto is "Ethereum":
            self.SYMBOL = 'USDT_ETH'
        if radiobutton.crypto is "Ripple":
            self.SYMBOL = 'USDT_XRP'



    def checkbox_toggled(self):
        selected = []

        if self.checkbox1.isChecked():
            selected.append("Daily")
            self.UNIT = 'day'

        if self.checkbox2.isChecked():
            selected.append("Hourly")
            self.UNIT = 'hour'

        if self.checkbox3.isChecked():
            selected.append("Minute")
            self.UNIT = 'minute'

        print("Selected timeframe: %s" % (" ".join(selected)))



    def btn_click(self):
        # SYMBOL = "USDT_BTC"
        # UNIT = "day"
        COUNT = 15
        PERIOD = 300
        trend = main.main(self.SYMBOL, self.UNIT, COUNT, PERIOD)
        self.result.setText(trend)


        


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())








