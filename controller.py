from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import csv
import sys
from random import *
from PyQt5.QtCore import Qt
from profile import *

id_key = ['12345678']
class Controller(QMainWindow, Ui_MainWindow):
    '''
    Class which allows manipulation of the database and control of the GUI on behalf of the user.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialization of control points for the user to the GUI, establishment of stackedWidget navigation pathing, and detection of special states.
        Defines what methods are passed according to the user-input provided.
        Inherits initialization, positional arguments, and keyword arguments from parent classes QMainWindow and Ui_MainWindow.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui = Ui_MainWindow()
        #stackedWidget pathing
        self.pushButton_detail.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_detail))
        self.pushButton_create.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_detail))
        self.listWidget.itemDoubleClicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_detail))
        #User-input control points
        self.pushButton_search.clicked.connect(self.clicked_search)
        self.pushButton_search_cancel.clicked.connect(self.clicked_search_cancel)
        self.pushButton_create.clicked.connect(self.clicked_create)
        self.pushButton_detail.clicked.connect(self.clicked_detail)
        self.pushButton_delete.clicked.connect(self.clicked_delete)
        self.pushButton_exit.clicked.connect(self.clicked_exit)
        self.pushButton_save.clicked.connect(self.valid_input)  
        self.pushButton_cancel.clicked.connect(self.clicked_cancel)
        self.listWidget.itemDoubleClicked.connect(self.clicked_detail)
        self.lineEdit_search.returnPressed.connect(self.pushButton_search.click)
        #Special states
        self.searching = False
        if self.searching == False:
            self.refresh()


    def clicked_search(self) -> None:
        '''
        Queries matches from the database file's searchable data points against user-input.
        Initializes a special state which discontinues routine listWidget data population in favor of curated population of search result matches.
        '''
        try:
            self.searching = True
            self.query = self.lineEdit_search.text()
            self.search_scan = []
            self.listWidget.clear()
            with open('records.csv', 'r') as rf:
                reader = csv.reader(rf)
                for row_search in reader:
                    s = Profile(*row_search)
                    for searchable_item in s.searchable():
                        if self.query.strip().lower() in searchable_item.strip().lower():
                            self.search_item = QListWidgetItem(s.get_full_name() + s.get_id().rjust(40-len(s.get_full_name()),'-'))
                            self.listWidget.addItem(self.search_item)
                            self.listWidget.setSortingEnabled(True)
                            break
        except Exception as searchError:
            print(searchError)
                    

    def clicked_search_cancel(self) -> None:
        '''
        Determines special state status and accordingly discontinues it. Restores routine listWidget data population with all database items using the refresh() method.
        Clears text input from the search box.
        '''
        try:
            if self.searching == True:
                self.search_scan.clear()
                self.lineEdit_search.setText('')
                self.refresh()
                self.searching = False
            elif self.searching == False:
                self.lineEdit_search.setText('')
        except Exception as searchCancelError:
            print(searchCancelError)
            

    def clicked_create(self):
        '''
        Prepares input form by clearing it.
        Discontinues special states.
        '''
        try:
            self.clear_form()
            if self.searching == True:
                self.clicked_search_cancel()
        except Exception as createError:
            print(createError)
            
        
    def clicked_detail(self) -> None:
        '''
        Determines if user has selected a listWidget item to edit/view in detail.
        If no profile is selected in the listWidget, the clicked_create function is called, displaying a blank form.
        If a profile is selected, the database is read until the selected profile's ID is matched in the database to allow all data points to be populated on the detail form.
        '''
        try:
            self.detail_selection = self.listWidget.currentItem().text()
            if not self.listWidget.selectedItems():
                self.clicked_create()
            else:
                with open('records.csv', 'r') as rf:
                    reader = csv.reader(rf)
                    for row_detail in reader:
                        d = Profile(*row_detail)
                        if d.get_id() == self.detail_selection[-6:]:
                            break
                    self.lineEdit_first_name_create.setText(d.get_first_name())
                    self.lineEdit_last_name_create.setText(d.get_last_name())
                    self.label_id_2.setText(d.get_id())
                    self.lineEdit_primary_phone_1.setText(d.get_primary_phone_1())
                    self.lineEdit_primary_phone_2.setText(d.get_primary_phone_2())
                    self.lineEdit_primary_phone_3.setText(d.get_primary_phone_3())
                    self.lineEdit_other_phone_1.setText(d.get_other_phone_1())
                    self.lineEdit_other_phone_2.setText(d.get_other_phone_2())
                    self.lineEdit_other_phone_3.setText(d.get_other_phone_3())
                    self.lineEdit_address_1.setText(d.get_address_1())
                    self.lineEdit_address_2.setText(d.get_address_2())
                    self.lineEdit_address_3.setText(d.get_address_3())
                    self.lineEdit_address_4.setText(d.get_address_4())
                    self.lineEdit_address_5.setText(d.get_address_5())
                    self.textEdit_notes_create.setPlainText(d.get_notes())

        except Exception as detailError:
            self.clear_form()
            print(detailError)


    def clicked_delete(self) -> None:
        '''
        Determines if user has selected a listWidget item to delete.
        If nothing is selected, an error is outputted instructing the user to select a listWidget item.
        If a profile is selected, the database is read to find the row containing the profile ID.
        After locating, the data row is deleted from the database and the listWidget is refreshed to reflect the removal.
        Special state status is determined to either return to the search inquiry results or the full list of database items.
        '''
        try:
            if not self.listWidget.selectedItems():
                print('No Profile Selected. Please select a profile on the list.')
            else:
                self.delete_scan = []
                self.delete_selection = self.listWidget.currentItem().text()
                with open('records.csv', 'r') as rf:
                    reader = csv.reader(rf)
                    for row_delete in reader:
                        self.delete_scan.append(row_delete)
                        for field_delete in row_delete:
                            if field_delete == self.delete_selection[-6:]:
                                self.delete_scan.remove(row_delete)
                    print('Profile', self.delete_selection[-6:], 'Deleted')

                with open('records.csv', 'w', newline='') as wf:
                    writer = csv.writer(wf)
                    writer.writerows(self.delete_scan)

                if self.searching == False:
                    self.refresh()
                else:
                    self.clicked_search()
        except Exception as deleteError:
            print(deleteError)


    def clicked_exit(self) -> None:
        '''
        Exits application.
        '''
        try:
            QApplication.quit()
        except Exception as exitError:
            print(exitError)

    def valid_input(self) -> None:
        '''
        Method, upon clicking the "Save" button, is called.
        Determines if mandatory data fields are satisfied with input.
        Determines if optional data fields contain allowed input type.
        If input requirements are not met, warning labels are unhidden which advise the user to adjust input.
        If input requirements are met, the clicked_save() function is called and allowed to create the profile or save changes to an existing profile.
        Warning labels are hidden upon satisfaction of input requirements.
        '''
        try:
            if (self.lineEdit_first_name_create.text() == '') or (self.lineEdit_last_name_create.text() == ''):
                self.label_blank_error.setHidden(False)
            else:
                self.label_blank_error.setHidden(True)
            if (self.check_all_letters(self.lineEdit_first_name_create.text()) == False) or (self.check_all_letters(self.lineEdit_last_name_create.text()) == False):
                self.label_error.setHidden(False)
            else:
                self.label_error.setHidden(True)
            if (self.check_all_numbers(self.lineEdit_primary_phone_1.text()) == False) or (self.check_all_numbers(self.lineEdit_primary_phone_2.text()) == False) or (self.check_all_numbers(self.lineEdit_primary_phone_3.text()) == False) or (self.check_all_numbers(self.lineEdit_other_phone_1.text()) == False) or (self.check_all_numbers(self.lineEdit_other_phone_2.text()) == False) or (self.check_all_numbers(self.lineEdit_other_phone_3.text()) == False):
                self.label_phone_error.setHidden(False)
            else:
                self.label_phone_error.setHidden(True) 
            if (self.check_all_letters(self.lineEdit_address_3.text()) == False) or (self.check_all_letters(self.lineEdit_address_4.text()) == False) or (self.check_all_numbers(self.lineEdit_address_5.text()) == False):
                self.label_address_error.setHidden(False)
            else:
                self.label_address_error.setHidden(True)

                    
            if self.label_error.isHidden() and self.label_address_error.isHidden() and self.label_blank_error.isHidden() and self.label_phone_error.isHidden():
                self.stackedWidget.setCurrentWidget(self.page_home)
                self.clicked_save()
        except Exception as inputError:
            print(inputError)


    def check_all_letters(self, text_input) -> bool:
        '''
        Method to read text input to determine if any characters are not alphabetic.
        :return: True if all alphabetic characters. False if any non-alphabetic characters.
        '''
        try:
            if bool(search("[^a-zA-Z]+",text_input)):
                return False
            else:
                return True
        except Exception as checkAllLettersError:
            print(checkAllLettersError)

        
    def check_all_numbers(self, text_input) -> bool:
        '''
        Method to read text input to determine if any characters are not numeric.
        :return: True if all numeric characters. False if any non-numeric characters.
        '''
        try:
            if bool(search("[^0-9]+",text_input)):
                return False
            else:
                return True
        except Exception as checkAllNumbersError:
            print(checkAllNumbersError)


    def clicked_save(self) -> None:
        '''
        Method which decides if it is creating a new database item or editing an existing database item.
        If creating a new item, text input fields are used to create Profile object and append the data to the database.
        If editing an existing database item, text input fields are used to create a Profile object and then search the database for the unique ID, after which the item is deleted from the database and a new item is written to the database.
        '''
        try:
            if self.label_id_2.text() =='n/a':
                p = Profile(self.lineEdit_first_name_create.text(),
                            self.lineEdit_last_name_create.text(),
                            self.id_generate(),
                            self.lineEdit_primary_phone_1.text(),
                            self.lineEdit_primary_phone_2.text(),
                            self.lineEdit_primary_phone_3.text(),
                            self.lineEdit_other_phone_1.text(),
                            self.lineEdit_other_phone_2.text(),
                            self.lineEdit_other_phone_3.text(),
                            self.lineEdit_address_1.text(),
                            self.lineEdit_address_2.text(),
                            self.lineEdit_address_3.text(),
                            self.lineEdit_address_4.text(),
                            self.lineEdit_address_5.text(),
                            self.textEdit_notes_create.toPlainText())

                with open('records.csv', 'a', newline='') as af:
                    appender = csv.writer(af)
                    appender.writerow(p.unpack())

                print('Profile Created')
                            

                if self.searching == False:
                    self.refresh()
                else:
                    self.clicked_search()
            else:
                e = Profile(self.lineEdit_first_name_create.text(),
                            self.lineEdit_last_name_create.text(),
                            self.label_id_2.text(),
                            self.lineEdit_primary_phone_1.text(),
                            self.lineEdit_primary_phone_2.text(),
                            self.lineEdit_primary_phone_3.text(),
                            self.lineEdit_other_phone_1.text(),
                            self.lineEdit_other_phone_2.text(),
                            self.lineEdit_other_phone_3.text(),
                            self.lineEdit_address_1.text(),
                            self.lineEdit_address_2.text(),
                            self.lineEdit_address_3.text(),
                            self.lineEdit_address_4.text(),
                            self.lineEdit_address_5.text(),
                            self.textEdit_notes_create.toPlainText())
                    
                self.create_scan = []
                with open('records.csv', 'r') as rf:
                    reader = csv.reader(rf)
                    self.create_scan.append(e.unpack())
                    for row_create in reader:
                        self.create_scan.append(row_create)
                        for field_create in row_create:
                            if field_create == e.get_id():
                                self.create_scan.remove(row_create)

                                
                with open('records.csv', 'w', newline='') as wf:
                    writer = csv.writer(wf)
                    writer.writerows(self.create_scan)
                print('Profile Saved')
                if self.searching == False:
                    self.refresh()
                else:
                    self.clicked_search()

        except Exception as saveError:
            print(saveError)
            


    def clicked_cancel(self) -> None:
        '''
        Method which is called when the user clicks the "cancel button" on the data entry screen.
        The listWidget items are refreshed if there is no special state.
        Input warning labels are hidden.
        '''
        try:
            if self.searching == False:
                self.refresh()
            self.label_address_error.setHidden(True)
            self.label_error.setHidden(True)
        except Exception as cancelError:
            print(cancelError)


    def id_generate(self) -> int:
        '''
        Method which recursively generates a unique 6-digit ID.
        The ID is added to the id_key list to ensure it is never duplicated in subsequent generations.
        :return: 6 digit unique ID integer.
        '''
        try:
            self.id_gen = randint(100000, 999999)
            if self.id_gen in id_key:
                return self.id_generate()
            else:
                id_key.append(self.id_gen)
                return self.id_gen
        except Exception as idGenerateError:
            print(idGenerateError)


    def refresh(self) -> None:
        '''
        Method to sync database items with listWidget items and delete any invalid entries.
        Upon exception raised by a missing or corrupted database file, the method requests input from the user to decide if it should end the program and await a database file correction, or if it should create a new empty database file.
        '''
        self.listWidget.clear()
        self.refresh_scan = []
        try:
            with open('records.csv', 'r') as rf:
                reader = csv.reader(rf)
                for line in reader:
                    r = Profile(*line)
                    self.refresh_scan.append(line)
                    if r.check_empty():
                        self.refresh_scan.remove(line)
                    if r.get_first_name() == '':
                        self.refresh_scan.remove(line)
                    if r.get_last_name() == '':
                        self.refresh_scan.remove(line)
                    num = len(r.get_full_name())
                    self.item_string = f'{r.get_full_name()}{r.get_id().rjust(42-num,".")}'
                    self.item = QListWidgetItem(self.item_string)
                    self.listWidget.addItem(self.item)
                    self.listWidget.setSortingEnabled(True)
                            
            with open('records.csv', 'w', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerows(self.refresh_scan)
        except Exception as refreshError:
            while True:
                error_input_database = input("Directory either missing or corrupted. Would you like to create a new database? Information from your previous database will NOT be preserved! (y/n): ").strip().lower()
                if error_input_database == 'y':
                    with open('records.csv', 'w'):
                        pass
                    print("Directory file restored. Please restart the application.")
                    break

                elif error_input_database == 'n':
                    print("Program Ended. Please provide a valid csv file in application directory folder.")
                    break
            print(refreshError)

    def clear_form(self):
        '''
        Method which clears GUI user-input form of any data.
        '''
        try:
            self.lineEdit_first_name_create.setText('')
            self.lineEdit_last_name_create.setText('')
            self.lineEdit_first_name_create.setText('')
            self.label_id_2.setText("n/a")
            self.lineEdit_primary_phone_1.setText('')
            self.lineEdit_primary_phone_2.setText('')
            self.lineEdit_primary_phone_3.setText('')
            self.lineEdit_other_phone_1.setText('')
            self.lineEdit_other_phone_2.setText('')
            self.lineEdit_other_phone_3.setText('')
            self.lineEdit_address_1.setText('')
            self.lineEdit_address_2.setText('')
            self.lineEdit_address_3.setText('')
            self.lineEdit_address_4.setText('')
            self.lineEdit_address_5.setText('')
            self.textEdit_notes_create.setPlainText('')
        except Exception as clearFormError:
            print(clearFormError)
