import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.player1 = True
        self.player2 = False
        self.turnText = QtWidgets.QLabel("1st player's turn")
        self.resetButton = QtWidgets.QPushButton("Reset")
        self.button1 = QtWidgets.QPushButton("1")
        self.button2 = QtWidgets.QPushButton("2")
        self.button3 = QtWidgets.QPushButton("3")
        self.button4 = QtWidgets.QPushButton("4")
        self.button5 = QtWidgets.QPushButton("5")
        self.button6 = QtWidgets.QPushButton("6")
        self.button7 = QtWidgets.QPushButton("7")
        self.button8 = QtWidgets.QPushButton("8")
        self.button9 = QtWidgets.QPushButton("9")
        
        hLayout0 = QtWidgets.QHBoxLayout()
        hLayout1 = QtWidgets.QHBoxLayout()
        hLayout2 = QtWidgets.QHBoxLayout()
        hLayout3 = QtWidgets.QHBoxLayout()

        hLayout0.addWidget(self.turnText)
        hLayout0.addWidget(self.resetButton)
        hLayout1.addWidget(self.button1)
        hLayout1.addWidget(self.button2)
        hLayout1.addWidget(self.button3)
        hLayout2.addWidget(self.button4)
        hLayout2.addWidget(self.button5)
        hLayout2.addWidget(self.button6)
        hLayout3.addWidget(self.button7)
        hLayout3.addWidget(self.button8)
        hLayout3.addWidget(self.button9)
        self.turnText.setFixedSize(250,100)
        self.resetButton.setFixedSize(100,100)
        self.button1.setFixedSize(100,100)
        self.button2.setFixedSize(100,100)
        self.button3.setFixedSize(100,100)
        self.button4.setFixedSize(100,100)
        self.button5.setFixedSize(100,100)
        self.button6.setFixedSize(100,100)
        self.button7.setFixedSize(100,100)
        self.button8.setFixedSize(100,100)
        self.button9.setFixedSize(100,100)
        font = QFont()
        fontText = QFont()
        font.setPointSize(20)
        fontText.setPointSize(20)
        self.turnText.setFont(fontText)
        self.resetButton.setFont(font)
        self.button1.setFont(font)
        self.button2.setFont(font)
        self.button3.setFont(font)
        self.button4.setFont(font)
        self.button5.setFont(font)
        self.button6.setFont(font)
        self.button7.setFont(font)
        self.button8.setFont(font)
        self.button9.setFont(font)
        
        vLayout = QtWidgets.QVBoxLayout()
        vLayout.addLayout(hLayout0)
        vLayout.addLayout(hLayout1)
        vLayout.addStretch()
        vLayout.addLayout(hLayout2)
        vLayout.addStretch()
        vLayout.addLayout(hLayout3)

        self.setWindowTitle("XOX")

        self.setLayout(vLayout)
        self.show()

        self.button1.clicked.connect(lambda: self.Xox(self.button1))
        self.button2.clicked.connect(lambda: self.Xox(self.button2))
        self.button3.clicked.connect(lambda: self.Xox(self.button3))
        self.button4.clicked.connect(lambda: self.Xox(self.button4))
        self.button5.clicked.connect(lambda: self.Xox(self.button5))
        self.button6.clicked.connect(lambda: self.Xox(self.button6))
        self.button7.clicked.connect(lambda: self.Xox(self.button7))
        self.button8.clicked.connect(lambda: self.Xox(self.button8))
        self.button9.clicked.connect(lambda: self.Xox(self.button9))
        self.resetButton.clicked.connect(self.Reset)
    def won(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)
        self.button5.setEnabled(False)
        self.button6.setEnabled(False)
        self.button7.setEnabled(False)
        self.button8.setEnabled(False)
        self.button9.setEnabled(False)
    def Xox(self, button):
        if(self.player1):
            button.setText("X")
            button.setEnabled(False)
            self.turnText.setText("2nd player's turn")
            self.player1 = False
            self.player2 = True
            if (not self.button1.isEnabled() and not self.button2.isEnabled() and not self.button3.isEnabled() and not self.button4.isEnabled() and not self.button5.isEnabled() and not self.button6.isEnabled() and not self.button7.isEnabled() and not self.button8.isEnabled() and not self.button9.isEnabled()):
                self.turnText.setText("Draw")
            if (self.button1.text() == "X" and self.button2.text() == "X" and self.button3.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button4.text() == "X" and self.button5.text() == "X" and self.button6.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button7.text() == "X" and self.button8.text() == "X" and self.button9.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button1.text() == "X" and self.button4.text() == "X" and self.button7.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button2.text() == "X" and self.button5.text() == "X" and self.button8.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button3.text() == "X" and self.button6.text() == "X" and self.button9.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button1.text() == "X" and self.button5.text() == "X" and self.button9.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
            if (self.button3.text() == "X" and self.button5.text() == "X" and self.button7.text() == "X"):
                self.turnText.setText("Player 1 won")
                self.won()
        else:
            button.setText("O")
            button.setEnabled(False)
            self.turnText.setText("1st player's turn")
            self.player1 = True
            self.player2 = False
            if (not self.button1.isEnabled() and not self.button2.isEnabled() and not self.button3.isEnabled() and not self.button4.isEnabled() and not self.button5.isEnabled() and not self.button6.isEnabled() and not self.button7.isEnabled() and not self.button8.isEnabled() and not self.button9.isEnabled()):
                self.turnText.setText("Draw")
            if (self.button1.text() == "O" and self.button2.text() == "O" and self.button3.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button4.text() == "O" and self.button5.text() == "O" and self.button6.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button7.text() == "O" and self.button8.text() == "O" and self.button9.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button1.text() == "O" and self.button4.text() == "O" and self.button7.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button2.text() == "O" and self.button5.text() == "O" and self.button8.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button3.text() == "O" and self.button6.text() == "O" and self.button9.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button1.text() == "O" and self.button5.text() == "O" and self.button9.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
            if (self.button3.text() == "O" and self.button5.text() == "O" and self.button7.text() == "O"):
                self.turnText.setText("Player 2 won")
                self.won()
    def Reset(self):
        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)
        self.button4.setEnabled(True)
        self.button5.setEnabled(True)
        self.button6.setEnabled(True)
        self.button7.setEnabled(True)
        self.button8.setEnabled(True)
        self.button9.setEnabled(True)
        self.button1.setText("1")
        self.button2.setText("2")
        self.button3.setText("3")
        self.button4.setText("4")
        self.button5.setText("5")
        self.button6.setText("6")
        self.button7.setText("7")
        self.button8.setText("8")
        self.button9.setText("9")
        self.player1 = True
        self.player2 = False
        self.turnText.setText("1st player's turn")

app = QtWidgets.QApplication(sys.argv)

window = Window()

window.setGeometry(500,250,500,500)

sys.exit(app.exec_())
