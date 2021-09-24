from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
import webbrowser
import sys
import os

class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi()
        
        self.characters = {
            'x': '*', '÷': '/', '^': '**', '²√': 'sqrt'
            }
        
        self.show()

    def setupUi(self):
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap("Files\icon.ico"))

        self.setGeometry(500, 250, 310, 360)
        self.setFixedSize(310, 360)
        self.setWindowIcon(window_icon)
        self.setWindowTitle("Calculator")


        monitor_font = QtGui.QFont()
        monitor_font.setFamily("Consolas")
        monitor_font.setPointSize(11)
        monitor_font.setBold(True)
        monitor_font.setWeight(75)
        self.text = ''
        self.monitor = QtWidgets.QLineEdit(self)
        self.monitor.setGeometry(20, 40, 271, 41)
        self.monitor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.monitor.setReadOnly(True)
        self.monitor.setFont(monitor_font)

        
        buttons_frame = QtWidgets.QFrame(self)
        buttons_frame.setGeometry(20, 110, 270, 230)
        buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        btn_0 = QtWidgets.QPushButton(buttons_frame)
        btn_0.setGeometry(70, 200, 60, 30)
        btn_0.setText("0")
        btn_0.clicked.connect(lambda: self.update('0'))
        btn_0.setShortcut('0')
        
        btn_1 = QtWidgets.QPushButton(buttons_frame)
        btn_1.setGeometry(0, 160, 60, 30)
        btn_1.setText("1")
        btn_1.clicked.connect(lambda: self.update('1'))
        btn_1.setShortcut('1')
        
        btn_2 = QtWidgets.QPushButton(buttons_frame)
        btn_2.setGeometry(70, 160, 60, 30)
        btn_2.setText("2")
        btn_2.clicked.connect(lambda: self.update('2'))
        btn_2.setShortcut('2')
        
        btn_3 = QtWidgets.QPushButton(buttons_frame)
        btn_3.setGeometry(140, 160, 60, 30)
        btn_3.setText("3")
        btn_3.clicked.connect(lambda: self.update('3'))
        btn_3.setShortcut('3')
        
        btn_4 = QtWidgets.QPushButton(buttons_frame)
        btn_4.setGeometry(0, 120, 60, 30)
        btn_4.setText("4")
        btn_4.clicked.connect(lambda: self.update('4'))
        btn_4.setShortcut('4')

        btn_5 = QtWidgets.QPushButton(buttons_frame)
        btn_5.setGeometry(70, 120, 60, 30)
        btn_5.setText("5")
        btn_5.clicked.connect(lambda: self.update('5'))
        btn_5.setShortcut('5')
        
        btn_6 = QtWidgets.QPushButton(buttons_frame)
        btn_6.setGeometry(140, 120, 60, 30)
        btn_6.setText("6")
        btn_6.clicked.connect(lambda: self.update('6'))
        btn_6.setShortcut('6')
        
        btn_7 = QtWidgets.QPushButton(buttons_frame)
        btn_7.setGeometry(0, 80, 60, 30)
        btn_7.setText("7")
        btn_7.clicked.connect(lambda: self.update('7'))
        btn_7.setShortcut('7')
        
        btn_8 = QtWidgets.QPushButton(buttons_frame)
        btn_8.setGeometry(70, 80, 60, 30)
        btn_8.setText("8")
        btn_8.clicked.connect(lambda: self.update('8'))
        btn_8.setShortcut('8')
        
        btn_9 = QtWidgets.QPushButton(buttons_frame)
        btn_9.setGeometry(140, 80, 60, 30)
        btn_9.setText("9")
        btn_9.clicked.connect(lambda: self.update('9'))
        btn_9.setShortcut('9')
        
        btn_minus = QtWidgets.QPushButton(buttons_frame)
        btn_minus.setGeometry(210, 200, 60, 30)
        btn_minus.setText("-")
        btn_minus.clicked.connect(lambda: self.update('-'))
        btn_minus.setShortcut('-')
        
        btn_plus = QtWidgets.QPushButton(buttons_frame)
        btn_plus.setGeometry(210, 160, 60, 30)
        btn_plus.setText("+")
        btn_plus.clicked.connect(lambda: self.update('+'))
        btn_plus.setShortcut('+')
        
        btn_division = QtWidgets.QPushButton(buttons_frame)
        btn_division.setGeometry(210, 120, 60, 30)
        btn_division.setText("÷")
        btn_division.clicked.connect(lambda: self.update('÷'))
        btn_division.setShortcut('/')

        btn_mul = QtWidgets.QPushButton(buttons_frame)
        btn_mul.setGeometry(210, 80, 60, 30)
        btn_mul.setText("x")
        btn_mul.clicked.connect(lambda: self.update('x'))
        btn_mul.setShortcut('*')
        
        btn_root = QtWidgets.QPushButton(buttons_frame)
        btn_root.setGeometry(210, 40, 60, 30)
        btn_root.setText("²√")
        btn_root.clicked.connect(lambda: self.update('²√('))
        
        btn_square = QtWidgets.QPushButton(buttons_frame)
        btn_square.setGeometry(140, 40, 60, 30)
        btn_square.setText("x²")
        btn_square.clicked.connect(lambda: self.update('^(2)'))
        
        btn_pow = QtWidgets.QPushButton(buttons_frame)
        btn_pow.setGeometry(70, 40, 60, 30)
        btn_pow.setText("xʸ")
        btn_pow.clicked.connect(lambda: self.update('^('))
        btn_pow.setShortcut('^')
        
        btn_round = QtWidgets.QPushButton(buttons_frame)
        btn_round.setGeometry(0, 40, 60, 30)
        btn_round.setText("R")
        btn_round.clicked.connect(self.round_number)
        btn_round.setShortcut('r')

        backspace_icon = QtGui.QIcon()
        backspace_icon.addPixmap(QtGui.QPixmap(r"Files\backspace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        btn_backspace = QtWidgets.QPushButton(buttons_frame)
        btn_backspace.setGeometry(QtCore.QRect(210, 0, 60, 30))
        btn_backspace.setIcon(backspace_icon)
        btn_backspace.clicked.connect(self.backspace)
        btn_backspace.setShortcut('backspace')
        
        btn_clear = QtWidgets.QPushButton(buttons_frame)
        btn_clear.setGeometry(140, 0, 60, 30)
        btn_clear.setText("C")
        btn_clear.clicked.connect(self.clear_monitor)
        btn_clear.setShortcut('c')
        
        btn_parenthesesC = QtWidgets.QPushButton(buttons_frame)
        btn_parenthesesC.setGeometry(70, 0, 60, 30)
        btn_parenthesesC.setText(")")
        btn_parenthesesC.clicked.connect(lambda: self.update(')'))
        btn_parenthesesC.setShortcut(')')
        
        btn_parenthesesO = QtWidgets.QPushButton(buttons_frame)
        btn_parenthesesO.setGeometry(0, 0, 60, 30)
        btn_parenthesesO.setText("(")
        btn_parenthesesO.clicked.connect(lambda: self.update('('))
        btn_parenthesesO.setShortcut('(')
        
        btn_dot = QtWidgets.QPushButton(buttons_frame)
        btn_dot.setGeometry(140, 200, 60, 30)
        btn_dot.setText(".")
        btn_dot.clicked.connect(lambda: self.update('.'))
        btn_dot.setShortcut('.')
        
        btn_equal = QtWidgets.QPushButton(buttons_frame)
        btn_equal.setGeometry(0, 200, 60, 30)
        btn_equal.setText("=")
        btn_equal.clicked.connect(self.calculate)
        btn_equal.setShortcut('return')
        
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(154, 154, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        
        self.history_lbl = QtWidgets.QLabel(self)
        self.history_lbl.setGeometry(24, 42, 250, 15)
        self.history_lbl.setPalette(palette)

        self.init_menu()
        
    def calculate(self):
        error = 'ERROR: '
        try:
            self.text = self.text.lstrip(error)
            history = self.text
            
            for key, value in self.characters.items():
                self.text = self.text.replace(key, value)
            
            self.text = str(eval(self.text))
            self.history_lbl.setText(history)
            self.monitor.setText(self.text)
        
        except:
            if not self.text.startswith(error):
                self.text = error + history
                self.monitor.setText(self.text)
        
    def update(self, text):
        self.text += text
        self.monitor.setText(self.text)
        
    def backspace(self):
        self.text = self.text[:-1]
        self.monitor.setText(self.text)
        
    def round_number(self):
        self.text = str(round(eval(self.text)))
        self.monitor.setText(self.text)
        
    def clear_monitor(self):
        self.text = ''
        self.monitor.clear()
        self.history_lbl.setText('')

    def init_menu(self):
        aboutAction = QtWidgets.QAction('About us', self)
        aboutAction.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, 'About us', about_msg))
        
        menu = self.menuBar()
        menu.addAction(aboutAction)


about_msg = '''\nThis program made by Sina.f\t\n
GitHub: sina-programer
Telegram: sina_programer
Instagram: sina.programer\t\n'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()

    sys.exit(app.exec_())
