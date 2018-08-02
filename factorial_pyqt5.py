import sys
from PyQt5.QtWidgets import (QApplication,QVBoxLayout,QHBoxLayout,QWidget,
                             QGridLayout,QPushButton,QLineEdit,QLabel)


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n-1)
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.inputLine = QLineEdit()
        self.outputLine = QLineEdit()
        self.outputLine.setReadOnly(True)

        self.calcButton = QPushButton("calc")
        self.calcButton.clicked.connect(self.calc)
        lineLayout = QGridLayout()
        lineLayout.addWidget(QLabel("num"),0,0)
        lineLayout.addWidget(self.inputLine,0,1)
        lineLayout.addWidget(QLabel("result"),1,0)
        lineLayout.addWidget(self.outputLine,1,1)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("factorial")
        self.show()
    def calc(self):
        n = int(self.inputLine.text())
        r = factorial(n)
        self.outputLine.setText(str(r))


app = QApplication(sys.argv)
main_window = MainWindow()

sys.exit(app.exec_())