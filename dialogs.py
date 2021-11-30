from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import sys


class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        if sys.platform == 'win32':
            import winsound
            winsound.MessageBeep()

        self.setupUi()

    def setupUi(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Files/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(300, 100)
        self.setWindowTitle("About us")

        description = QtWidgets.QLabel(self)
        description.setGeometry(75, 10, 150, 30)
        description.setAlignment(QtCore.Qt.AlignCenter)
        description.setText("This program made by Sina.f")

        horizontalLayoutWidget = QtWidgets.QWidget(self)
        horizontalLayoutWidget.setGeometry(15, 50, 270, 40)
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(12)

        btn_github = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_github.setText("GitHub")
        btn_github.clicked.connect(lambda: webbrowser.open('https://github.com/sina-programer'))

        btn_instagram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_instagram.setText("Instagram")
        btn_instagram.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/sina.programer'))

        btn_telegram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_telegram.setText("Telegram")
        btn_telegram.clicked.connect(lambda: webbrowser.open('https://t.me/sina_programer'))

        horizontalLayout.addWidget(btn_github)
        horizontalLayout.addWidget(btn_instagram)
        horizontalLayout.addWidget(btn_telegram)
