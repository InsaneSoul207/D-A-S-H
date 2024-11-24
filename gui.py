from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ALPHA ASSISTANT")
        MainWindow.resize(1200, 1000)
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = MainWindow.geometry()
        MainWindow.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: transparent;")

        self.content_frame = QtWidgets.QFrame(self.centralwidget)
        self.content_frame.setGeometry(QtCore.QRect(100, 50, 1000, 800))
        self.content_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(25, 25, 25, 200); 
                border-radius: 20px;
            }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.content_frame)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)

        self.title_label = QtWidgets.QLabel(self.content_frame)
        self.title_label.setStyleSheet("""
            QLabel {
                font: 24pt "Impact"; 
                color: white;
                border-bottom: 2px solid #0077b3; 
            }
        """)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setText("ALPHA ASSISTANT")
        self.verticalLayout.addWidget(self.title_label)
        self.subheading_label = QtWidgets.QLabel(self.content_frame)
        self.subheading_label.setStyleSheet("""
            QLabel {
                font: 12pt "Impact"; 
                color: white;
                padding-bottom: 10px;
                border-bottom: 2px solid #0077b3;
            }
        """)
        self.subheading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subheading_label.setText("Advanced Language Processing And Human-like Asisstant.")
        self.verticalLayout.addWidget(self.subheading_label)
        self.terminal_output = QtWidgets.QTextEdit(self.content_frame)
        self.terminal_output.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 100);  
                color: white;
                font: 12pt "Consolas"; 
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.terminal_output.setReadOnly(True)
        self.verticalLayout.addWidget(self.terminal_output)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QtWidgets.QPushButton(self.content_frame)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton.setIcon(QtGui.QIcon("run_icon.png")) 
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #0077b3; 
                color: white;
                font: bold 14pt "Arial";
                border-radius: 10px;
                border: none; 
            }
            QPushButton:hover {
                background-color: #009; 
            }
        """)
        self.pushButton.setText("Run")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.content_frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setIcon(QtGui.QIcon("exit_icon.png")) 
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #d9534f; 
                color: white;
                font: bold 14pt "Arial";
                border-radius: 10px;
                border: none; 
            }
            QPushButton:hover {
                background-color: #c9302c; 
            }
        """)
        self.pushButton_2.setText("Exit")
        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
