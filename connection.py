from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mysql

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
 
        self.bt_con = QtWidgets.QPushButton(self)
        self.bt_con.setGeometry(QtCore.QRect(110, 170, 90, 30))
        self.bt_con.setObjectName("Connection")    
        self.bt_disc = QtWidgets.QPushButton(self)
        self.bt_disc.setGeometry(QtCore.QRect(210, 170, 90, 30))
        self.bt_disc.setObjectName("Connection")
        self.user = QtWidgets.QLineEdit(self)
        self.user.setGeometry(QtCore.QRect(80, 40, 241, 31))
        self.user.setObjectName("user")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 45, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QtCore.QRect(80, 85, 241, 31))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(40, 135, 41, 21))
        self.label_3.setObjectName("label_3")
        self.host = QtWidgets.QLineEdit(self)
        self.host.setGeometry(QtCore.QRect(80, 130, 241, 31))
        self.setWindowTitle('Connection')
        self.host.setObjectName("host")
        self.label.setText("User:")
        self.label_2.setText("Password:")
        self.label_3.setText("Host:")
        self.bt_con.setText("Connect")
        self.bt_disc.setText("Cancel")

        self.bt_con.clicked.connect(self.db_con)
        self.bt_disc.clicked.connect(self.cancel)
        self.username=''
        self.key=''
        self.host_db=''
        self.connection=''

        
    def cancel(self,index):
        self.reject()        
    def db_con(self):
        self.username=self.user.text()
        self.key=self.password.text()
        self.host_db=self.host.text()
        if len(self.username) and len(self.key) and len(self.host_db):
            try:    
                self.connection=mysql.connect(
                user=self.username,
                password=self.key,
                host=self.host_db)
                self.accept()
            except:
                msg= QtWidgets.QMessageBox()
                msg.setWindowTitle('Error')
                msg.setText('Incorrect Connection Parameters')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                x=msg.exec_()
        else: 
            msg= QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Please fill all the fields')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            x=msg.exec_()