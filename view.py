from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    '''
    Class which defines and displays all GUI elements
    '''
    def setupUi(self, MainWindow):
        '''
        Method which defines properties of GUI window
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 570)
        self.setStyleSheet("background-color: #777a68;")
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 400, 570))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_home.sizePolicy().hasHeightForWidth())
        self.page_home.setSizePolicy(sizePolicy)
        self.page_home.setObjectName("page_home")


#Home Page
        
        #Logo
        self.widget_logo = QtWidgets.QWidget(self.page_home)
        self.widget_logo.setGeometry(QtCore.QRect(10, 500, 291, 51))
        self.widget_logo.setObjectName("widget_logo")
        self.widget_logo.setStyleSheet("border-image: url(images/logo.png);")
        #Delete button
        self.pushButton_delete = QtWidgets.QPushButton(self.page_home)
        self.pushButton_delete.setGeometry(QtCore.QRect(10, 440, 41, 41))
        self.pushButton_delete.setText("")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setStyleSheet("border-image: url(images/trash.png);")

        #Search button
        self.pushButton_search = QtWidgets.QPushButton(self.page_home)
        self.pushButton_search.setGeometry(QtCore.QRect(300, 2, 91, 31))
        self.pushButton_search.setText("")
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.setStyleSheet("border-image: url(images/search.png);")
        
        #Search cancel button
        self.pushButton_search_cancel = QtWidgets.QPushButton(self.page_home)
        self.pushButton_search_cancel.setGeometry(QtCore.QRect(265, 2, 31, 31))
        self.pushButton_search_cancel.setText("")
        self.pushButton_search_cancel.setObjectName("pushButton_search_cancel")
        self.pushButton_search_cancel.setStyleSheet("border-image: url(images/search_cancel.png);")
        

        #Search input field
        self.lineEdit_search = QtWidgets.QLineEdit(self.page_home)
        self.lineEdit_search.setGeometry(QtCore.QRect(10, 9, 245, 21))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setStyleSheet("background-color: white;")
        self.lineEdit_search.setPlaceholderText("Search by First/Last Name or ID")
        self.lineEdit_search.setMaxLength(30)

        #DETAIL button
        self.pushButton_detail = QtWidgets.QPushButton(self.page_home)
        self.pushButton_detail.setGeometry(QtCore.QRect(60, 440, 331, 41))
        self.pushButton_detail.setText("")
        self.pushButton_detail.setObjectName("pushButton_detail")
        self.pushButton_detail.setStyleSheet("border-image: url(images/detail.png);")

        #Column header image
        self.header = QtWidgets.QWidget(self.page_home)
        self.header.setGeometry(QtCore.QRect(10, 43, 381, 20))
        self.header.setObjectName("label_phone_hyphen_2")
        self.header.setStyleSheet("border-image: url(images/header.png);")
        
        #List widget
        self.listWidget = QtWidgets.QListWidget(self.page_home)
        self.listWidget.setGeometry(QtCore.QRect(10, 65, 381, 315))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: white; font: 8pt Courier")

        #Exit button
        self.pushButton_exit = QtWidgets.QPushButton(self.page_home)
        self.pushButton_exit.setGeometry(QtCore.QRect(320, 510, 71, 31))
        self.pushButton_exit.setText("")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setStyleSheet("border-image: url(images/exit.png);")

        #Create button
        self.pushButton_create = QtWidgets.QPushButton(self.page_home)
        self.pushButton_create.setGeometry(QtCore.QRect(10, 390, 381, 41))
        self.pushButton_create.setText("")
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_create.setStyleSheet("border-image: url(images/create.png);")

        #Stacked Widget
        self.stackedWidget.addWidget(self.page_home)
        self.page_detail = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_detail.sizePolicy().hasHeightForWidth())
        self.page_detail.setSizePolicy(sizePolicy)
        self.page_detail.setObjectName("page_detail")

        
#Details Page
        
    #LABELS
        
        #Phone decorators
        self.label_paran1 = QtWidgets.QLabel(self.page_detail)
        self.label_paran1.setGeometry(QtCore.QRect(90, 100, 21, 16))
        self.label_paran1.setObjectName("label_paran1")
        self.label_paran2 = QtWidgets.QLabel(self.page_detail)
        self.label_paran2.setGeometry(QtCore.QRect(140, 100, 16, 16))
        self.label_paran2.setObjectName("label_paran2")
        self.label_phone_hyphen = QtWidgets.QLabel(self.page_detail)
        self.label_phone_hyphen.setGeometry(QtCore.QRect(190, 100, 16, 16))
        self.label_phone_hyphen.setObjectName("label_phone_hyphen")
        self.label_paran1_2 = QtWidgets.QLabel(self.page_detail)
        self.label_paran1_2.setGeometry(QtCore.QRect(90, 130, 21, 16))
        self.label_paran1_2.setObjectName("label_paran1_2")
        self.label_phone_hyphen_2 = QtWidgets.QLabel(self.page_detail)
        self.label_phone_hyphen_2.setGeometry(QtCore.QRect(190, 130, 16, 16))
        self.label_phone_hyphen_2.setObjectName("label_phone_hyphen_2")
        self.label_paran2_2 = QtWidgets.QLabel(self.page_detail)
        self.label_paran2_2.setGeometry(QtCore.QRect(140, 130, 16, 16))
        self.label_paran2_2.setObjectName("label_paran2_2")
        #Name
        self.label_first_name_create = QtWidgets.QLabel(self.page_detail)
        self.label_first_name_create.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_first_name_create.setObjectName("label_first_name_create")
        self.label_first_name_asterisk = QtWidgets.QLabel(self.page_detail)
        self.label_first_name_asterisk.setGeometry(QtCore.QRect(61, 20, 61, 16))
        self.label_first_name_asterisk.setObjectName("label_first_name_asterisk")
        self.label_first_name_asterisk.setStyleSheet("color: yellow;")
        self.label_last_name_create = QtWidgets.QLabel(self.page_detail)
        self.label_last_name_create.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_last_name_create.setObjectName("label_last_name_create")
        self.label_last_name_asterisk = QtWidgets.QLabel(self.page_detail)
        self.label_last_name_asterisk.setGeometry(QtCore.QRect(61, 50, 61, 16))
        self.label_last_name_asterisk.setObjectName("label_last_name_asterisk")
        self.label_last_name_asterisk.setStyleSheet("color: yellow;")
        #Required
        self.label_requirements = QtWidgets.QLabel(self.page_detail)
        self.label_requirements.setGeometry(QtCore.QRect(290, 40, 70, 20))
        self.label_requirements.setObjectName("label_last_name_asterisk")
        self.label_requirements.setStyleSheet("color:  yellow;")
        #Phone
        self.label_phone_primary_create = QtWidgets.QLabel(self.page_detail)
        self.label_phone_primary_create.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_phone_primary_create.setObjectName("label_phone_primary_create")
        self.label_phone_other_create = QtWidgets.QLabel(self.page_detail)
        self.label_phone_other_create.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_phone_other_create.setObjectName("label_phone_other_create")
        #Address
        self.label_address_1_create = QtWidgets.QLabel(self.page_detail)
        self.label_address_1_create.setGeometry(QtCore.QRect(10, 180, 47, 13))
        self.label_address_1_create.setObjectName("label_address_1_create")
        self.label_address_2_create = QtWidgets.QLabel(self.page_detail)
        self.label_address_2_create.setGeometry(QtCore.QRect(10, 210, 47, 13))
        self.label_address_2_create.setObjectName("label_address_2_create")
        self.label_address_3_create = QtWidgets.QLabel(self.page_detail)
        self.label_address_3_create.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.label_address_3_create.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_address_3_create.setObjectName("label_address_3_create")
        #Notes
        self.label_notes_create = QtWidgets.QLabel(self.page_detail)
        self.label_notes_create.setGeometry(QtCore.QRect(10, 300, 47, 13))
        self.label_notes_create.setObjectName("label_notes_create")
        #Name Error Warning
        self.label_error = QtWidgets.QLabel(self.page_detail)
        self.label_error.setGeometry(QtCore.QRect(100, 70, 200, 20))
        self.label_error.setObjectName("label_error")
        self.label_error.setStyleSheet("color: yellow;")
        self.label_error.setHidden(True)
        #Blank Error Warning
        self.label_blank_error = QtWidgets.QLabel(self.page_detail)
        self.label_blank_error.setGeometry(QtCore.QRect(75, 70, 220, 20))
        self.label_blank_error.setObjectName("label_error")
        self.label_blank_error.setStyleSheet("color: yellow;")
        self.label_blank_error.setHidden(True)
        #Phone Error Warning
        self.label_phone_error = QtWidgets.QLabel(self.page_detail)
        self.label_phone_error.setGeometry(QtCore.QRect(100, 140, 200, 40))
        self.label_phone_error.setObjectName("label_error")
        self.label_phone_error.setStyleSheet("color: yellow;")
        self.label_phone_error.setHidden(True)
        #Address Error Warning
        self.label_address_error = QtWidgets.QLabel(self.page_detail)
        self.label_address_error.setGeometry(QtCore.QRect(100, 257, 200, 40))
        self.label_address_error.setObjectName("label_error")
        self.label_address_error.setStyleSheet("color: yellow;")
        self.label_address_error.setHidden(True)
        #Unique ID
        self.label_id_1 = QtWidgets.QLabel(self.page_detail)
        self.label_id_1.setGeometry(QtCore.QRect(290, 20, 21, 16))
        self.label_id_1.setObjectName("label_id_1")
        self.label_id_2 = QtWidgets.QLabel(self.page_detail)
        self.label_id_2.setGeometry(QtCore.QRect(310, 20, 47, 13))
        self.label_id_2.setObjectName("label_id_2")

    #BUTTONS
        
        #NOTES
        self.textEdit_notes_create = QtWidgets.QTextEdit(self.page_detail)
        self.textEdit_notes_create.setGeometry(QtCore.QRect(10, 320, 381, 161))
        self.textEdit_notes_create.setObjectName("textEdit_notes_create")
        self.textEdit_notes_create.setStyleSheet("background-color: white;")
        #SAVE
        self.pushButton_save = QtWidgets.QPushButton(self.page_detail)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 500, 111, 41))
        self.pushButton_save.setObjectName("pushButton_save")
        #CANCEL
        self.pushButton_cancel = QtWidgets.QPushButton(self.page_detail)
        self.pushButton_cancel.setGeometry(QtCore.QRect(280, 500, 111, 41))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))


    #INPUT FIELDS
        
        #first name
        self.lineEdit_first_name_create = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_first_name_create.setGeometry(QtCore.QRect(80, 20, 181, 20))
        self.lineEdit_first_name_create.setObjectName("lineEdit_first_name_create")
        self.lineEdit_first_name_create.setStyleSheet("background-color: white;")
        self.lineEdit_first_name_create.setMaxLength(16)
        #last name
        self.lineEdit_last_name_create = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_last_name_create.setGeometry(QtCore.QRect(80, 50, 181, 20))
        self.lineEdit_last_name_create.setObjectName("lineEdit_last_name_create")
        self.lineEdit_last_name_create.setStyleSheet("background-color: white;")
        self.lineEdit_last_name_create.setMaxLength(16)
        #primary phone 1
        self.lineEdit_primary_phone_1 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_primary_phone_1.setGeometry(QtCore.QRect(100, 100, 31, 20))
        self.lineEdit_primary_phone_1.setObjectName("lineEdit_primary_phone_1")
        self.lineEdit_primary_phone_1.setStyleSheet("background-color: white;")
        self.lineEdit_primary_phone_1.setMaxLength(3)
        #primary phone 2
        self.lineEdit_primary_phone_2 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_primary_phone_2.setGeometry(QtCore.QRect(150, 100, 31, 20))
        self.lineEdit_primary_phone_2.setObjectName("lineEdit_primary_phone_2")
        self.lineEdit_primary_phone_2.setStyleSheet("background-color: white;")
        self.lineEdit_primary_phone_2.setMaxLength(3)
        #primary phone 3
        self.lineEdit_primary_phone_3 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_primary_phone_3.setGeometry(QtCore.QRect(200, 100, 61, 20))
        self.lineEdit_primary_phone_3.setObjectName("lineEdit_primary_phone_3")
        self.lineEdit_primary_phone_3.setStyleSheet("background-color: white;")
        self.lineEdit_primary_phone_3.setMaxLength(4)
        #other phone 1
        self.lineEdit_other_phone_1 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_other_phone_1.setGeometry(QtCore.QRect(100, 130, 31, 20))
        self.lineEdit_other_phone_1.setObjectName("lineEdit_other_phone_1")
        self.lineEdit_other_phone_1.setStyleSheet("background-color: white;")
        self.lineEdit_other_phone_1.setMaxLength(3)
        #other phone 2
        self.lineEdit_other_phone_2 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_other_phone_2.setGeometry(QtCore.QRect(150, 130, 31, 20))
        self.lineEdit_other_phone_2.setObjectName("lineEdit_other_phone_2")
        self.lineEdit_other_phone_2.setStyleSheet("background-color: white;")
        self.lineEdit_other_phone_2.setMaxLength(3)
        #other phone 3
        self.lineEdit_other_phone_3 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_other_phone_3.setGeometry(QtCore.QRect(200, 130, 61, 20))
        self.lineEdit_other_phone_3.setObjectName("lineEdit_other_phone_3")
        self.lineEdit_other_phone_3.setStyleSheet("background-color: white;")
        self.lineEdit_other_phone_3.setMaxLength(4)
        #address 1
        self.lineEdit_address_1 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_address_1.setGeometry(QtCore.QRect(60, 180, 251, 20))
        self.lineEdit_address_1.setObjectName("lineEdit_address_1")
        self.lineEdit_address_1.setStyleSheet("background-color: white;")
        #address 2
        self.lineEdit_address_2 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_address_2.setGeometry(QtCore.QRect(70, 210, 241, 20))
        self.lineEdit_address_2.setObjectName("lineEdit_address_2")
        self.lineEdit_address_2.setStyleSheet("background-color: white;")
        #address 3
        self.lineEdit_address_3 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_address_3.setGeometry(QtCore.QRect(90, 240, 121, 20))
        self.lineEdit_address_3.setObjectName("lineEdit_address_3")
        self.lineEdit_address_3.setStyleSheet("background-color: white;")
        #address 4
        self.lineEdit_address_4 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_address_4.setGeometry(QtCore.QRect(220, 240, 31, 20))
        self.lineEdit_address_4.setObjectName("lineEdit_address_4")
        self.lineEdit_address_4.setStyleSheet("background-color: white;")
        self.lineEdit_address_4.setMaxLength(2)
        #address 5
        self.lineEdit_address_5 = QtWidgets.QLineEdit(self.page_detail)
        self.lineEdit_address_5.setGeometry(QtCore.QRect(260, 240, 51, 20))
        self.lineEdit_address_5.setObjectName("lineEdit_address_5")
        self.lineEdit_address_5.setStyleSheet("background-color: white;")
        self.lineEdit_address_5.setMaxLength(5)
        
        self.stackedWidget.addWidget(self.page_detail)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        '''
        Method which provides all text information to be utilized by GUI elements.
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DSS"))
        self.label_first_name_create.setText(_translate("MainWindow", "First Name:"))
        self.label_last_name_create.setText(_translate("MainWindow", "Last Name:"))
        self.label_phone_primary_create.setText(_translate("MainWindow", "Primary Phone:"))
        self.label_phone_other_create.setText(_translate("MainWindow", "Other Phone:"))
        self.label_address_1_create.setText(_translate("MainWindow", "Address:"))
        self.label_address_2_create.setText(_translate("MainWindow", "Address 2"))
        self.label_address_3_create.setText(_translate("MainWindow", "City, State, Zip"))
        self.label_notes_create.setText(_translate("MainWindow", "Notes:"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_paran1.setText(_translate("MainWindow", "("))
        self.label_paran2.setText(_translate("MainWindow", ")"))
        self.label_phone_hyphen.setText(_translate("MainWindow", "-"))
        self.label_paran2_2.setText(_translate("MainWindow", ")"))
        self.label_paran1_2.setText(_translate("MainWindow", "("))
        self.label_phone_hyphen_2.setText(_translate("MainWindow", "-"))
        self.label_id_1.setText(_translate("MainWindow", "ID:"))
        self.label_id_2.setText(_translate("MainWindow", "12345678"))
        self.label_error.setText(_translate("MainWindow", "Name Error: Enter Letters Only"))
        self.label_blank_error.setText(_translate("MainWindow", "Name Error: First and Last Name Required"))
        self.label_phone_error.setText(_translate("MainWindow", "Phone Error: Enter Numbers Only"))
        self.label_first_name_asterisk.setText(_translate("MainWindow", "*"))
        self.label_last_name_asterisk.setText(_translate("MainWindow", "*"))
        self.label_requirements.setText(_translate("MainWindow", "* - Required"))
        self.label_address_error.setText(_translate("MainWindow", "Address Error: Enter Letters in City/State \n& Numbers in ZipCode"))

        

        
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
