from PyQt5.QtCore import Qt
from instr import *
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit)

class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
    def initUI(self):
        self.first_question = QLabel(txt_test1)
        self.second_question = QLabel(txt_test2)
        self.third_question = QLabel(txt_test3)
        self.name = QLabel(txt_name)
        self.edit_name = QLineEdit (txt_hintname)
        self.age = QLabel(txt_age)
        self.edit_age = QLineEdit(txt_hintage)
        self.first_answer = QLineEdit(txt_hinttest1)
        self.second_answer = QLineEdit(txt_hinttest2)
        self.third_answer = QLineEdit(txt_hinttest3)
        self.first_starttest = QPushButton(txt_starttest1)
        self.second_starttest = QPushButton(txt_starttest2)
        self.third_starttest = QPushButton(txt_starttest3)
        self.result = QPushButton(txt_finalwin)
        self.timer = QLabel('00:00:00')
        self.timer.setStyleSheet("font: bold 50px")
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.edit_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.first_question, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.first_starttest, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.first_answer, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.second_question, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.second_starttest, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.second_answer, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.third_question, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.third_starttest, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.third_answer, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.result, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connect(self):
        pass
app = QApplication([])
mw = TextWin()











app.exec()
    