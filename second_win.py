from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from instr import *
from final_win import *
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel,QLineEdit,)

class TestWin(QWidget):
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
        self.text_timer = QLabel('00:00:00')
        self.text_timer.setStyleSheet("font: bold 50px")
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
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
        self.result.clicked.connect(self.next_win)
        self.first_starttest.clicked.connect(self.timer_test)
        self.first_starttest.clicked.connect(self.timer_test)
        self.second_starttest.clicked.connect(self.timer_sits)
        self.third_starttest.clicked.connect(self.timer_final)

    def next_win(self):
        self.hide()
        self.fw = WinThree()
    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')
