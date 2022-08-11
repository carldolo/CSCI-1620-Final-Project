from re import *

class Profile:
    '''
    A class which accepts, maintains, and outputs all relevant data for app profile creation and manipulation.
    '''

    
    def __init__(self, fn: str, ln: str, uid: int='', pp1: int='', pp2: int='', pp3: int='', op1: int='', op2: int='', op3: int='', a1='', a2='', a3: str='', a4: str='', a5: int='', notes=''):
        '''
        Establishes a profile object with all mandatory and optional input data
        :param fn: Individual's first name.
        :param ln: Individual's last name.
        :param uid: Individual's unique 6-digit ID which is generated upon creation or retrieved from the database.
        :param pp1: Primary phone number area code.
        :param pp2: Primary phone number middle three digits.
        :param pp3: Primary phone number last four digits.
        :param op1: Other/alternate phone number area code.
        :param op2: Other/alternate phone number first three digits.
        :param op3: Other/alternate phone number last four digits.
        :param a1: Address line 1.
        :param a2: Address line 2.
        :param a3: Address City
        :param a4: Address State abbreviation
        :param a5: Address zip code
        '''
        self.__first_name = fn
        self.__last_name = ln
        self.__id = uid
        self.__primary_phone_1 = pp1
        self.__primary_phone_2 = pp2
        self.__primary_phone_3 = pp3
        self.__other_phone_1 = op1
        self.__other_phone_2 = op2
        self.__other_phone_3 = op3
        self.__address_1 = a1
        self.__address_2 = a2
        self.__address_3 = a3
        self.__address_4 = a4
        self.__address_5 = a5
        self.__notes = notes
        
        
    #Getters
    def get_full_name(self) -> str:
        '''
        Method to access a person's full name.
        :return: Individual's first name concatenated with their last name.
        '''
        return f'{self.__first_name} {self.__last_name}'

    def get_first_name(self) -> str:
        '''
        Method to access a person's first name.
        :return: Individual's first name.
        '''
        return self.__first_name

    def get_last_name(self) -> str:
        '''
        Method to access a person's last name.
        :return: Individual's last name.
        '''
        return self.__last_name

    def get_id(self) -> int:
        '''
        Method to access a profile's unique ID.
        :return: Individual's ID.
        '''
        return self.__id

    def get_full_primary_phone(self) -> str:
        '''
        Method to access a person's full primary phone number.
        :return: Individual's three primary phone number fields concatenated together.
        '''
        return f'({self.__primary_phone_1}){self.__primary_phone_2}-{self.__primary_phone_3}'

    def get_primary_phone_1(self) -> int:
        '''
        Method to access a person's primary phone number area code.
        :return: Individual's primary phone number area code.
        '''
        return self.__primary_phone_1
    
    def get_primary_phone_2(self) -> int:
        '''
        Method to access a person's primary phone number middle three digits.
        :return: Individual's primary phone number middle three digits.
        '''
        return self.__primary_phone_2

    def get_primary_phone_3(self) -> int:
        '''
        Method to access a person's primary phone number last four digits.
        :return: Individual's primary phone number last four digits.
        '''
        return self.__primary_phone_3

    def get_full_other_phone(self) -> str:
        '''
        Method to access a person's full other/alternate phone number.
        :return: Individual's three other/alternate phone number fields concatenated together.
        '''
        return f'({self.__other_phone_1}){self.__other_phone_2}-{self.__other_phone_3}'

    def get_other_phone_1(self) -> int:
        '''
        Method to access a person's other/alternate phone number area code.
        :return: Individual's other/alternate phone number area code.
        '''
        return self.__other_phone_1

    def get_other_phone_2(self) -> int:
        '''
        Method to access a person's other/alternate phone number middle three digits.
        :return: Individual's other/alternate phone number middle three digits.
        '''
        return self.__other_phone_2

    def get_other_phone_3(self) -> int:
        '''
        Method to access a person's other/alternate phone number last four digits.
        :return: Individual's other/alternate phone number last four digits.
        '''
        return self.__other_phone_3

    def get_full_address(self) -> str:
        '''
        Method to access a person's full address.
        :return: Individual's five address field concatenated together.
        '''
        return f'{self.__address_1} {self.__address_2} {self.__address_3}, {self.__address_4} {self.__address_5}'

    def get_address_1(self) -> str:
        '''
        Method to access a person's street address.
        :return: Individual's street address.
        '''
        return self.__address_1

    def get_address_2(self) -> str:
        '''
        Method to access a person's second address line.
        :return: Individual's second address line.
        '''
        return self.__address_2

    def get_address_3(self) -> str:
        '''
        Method to access a person's city.
        :return: Individual's city.
        '''
        return self.__address_3

    def get_address_4(self) -> str:
        '''
        Method to access a person's state abbreviation.
        :return: Individual's state abbreviation.
        '''
        return self.__address_4

    def get_address_5(self) -> int:
        '''
        Method to access a person's zip code.
        :return: Individual's zip code.
        '''
        return self.__address_5

    def get_notes(self) -> str:
        '''
        Method to access a profile's special notation.
        :return: Profile's special notation.
        '''
        return self.__notes


    #Setters
    def set_first_name(self, x: str):
        '''
        Method to edit a profile's first name.
        :param x: Individual's new first name.
        '''
        self.__first_name = x

    def set_last_name(self, x: str):
        '''
        Method to edit a profile's last name.
        :param x: Individual's new last name.
        '''
        self.__last_name = x

    def set_id(self, x: int):
        '''
        Method to edit a profile's unique id.
        :param x: Individual's new unique id.
        '''
        self.__id = x

    def set_primary_phone_1(self, x: int):
        '''
        Method to edit a profile's primary phone area code.
        :param x: Individual's new primary phone area code.
        '''
        self.__primary_phone_1 = x
    
    def set_primary_phone_2(self, x: int):
        '''
        Method to edit a profile's primary phone middle three digits.
        :param x: Individual's new primary phone middle three digits.
        '''
        self.__primary_phone_2 = x

    def set_primary_phone_3(self, x: int):
        '''
        Method to edit a profile's primary phone last four digits.
        :param x: Individual's new primary phone last four digits.
        '''
        self.__primary_phone_3 = x

    def set_other_phone_1(self, x: int):
        '''
        Method to edit a profile's other/alternate phone area code.
        :param x: Individual's new other/alternate phone area code.
        '''
        self.__other_phone_1 = x

    def set_other_phone_2(self, x: int):
        '''
        Method to edit a profile's other/alternate phone middle three digits.
        :param x: Individual's new other/alternate phone middle three digits.
        '''
        self.__other_phone_2 = x

    def set_other_phone_3(self, x: int):
        '''
        Method to edit a profile's other/alternate phone last four digits.
        :param x: Individual's new other/alternate phone last four digits.
        '''
        self.__other_phone_3 = x

    def set_address_1(self, x: str):
        '''
        Method to edit a profile's street address.
        :param x: Individual's new street address.
        '''
        self.__address_1 = x

    def set_address_2(self, x: str):
        '''
        Method to edit a profile's second address line.
        :param x: Individual's new second address line.
        '''
        self.__address_2 = x

    def set_address_3(self, x: str):
        '''
        Method to edit a profile's city.
        :param x: Individual's new city.
        '''
        self.__address_3 = x

    def set_address_4(self, x: str):
        '''
        Method to edit a profile's state abbreviation.
        :param x: Individual's new state abbreviation.
        '''
        self.__address_4 = x

    def set_address_5(self, x: int):
        '''
        Method to edit a profile's zip code.
        :param x: Individual's new zip code.
        '''
        self.__address_5 = x

    def set_notes(self, x: str):
        '''
        Method to edit a profile's special notation.
        :param x: Profile's new special notation.
        '''
        self.__notes = x

    #Unique Methods
    def unpack(self) -> list:
        '''
        Method to export all class initialization data points as a list.
        :return: List of all object data points, including blank entries.
        '''
        return [self.get_first_name(),
                self.get_last_name(),
                self.get_id(),
                self.get_primary_phone_1(),
                self.get_primary_phone_2(),
                self.get_primary_phone_3(),
                self.get_other_phone_1(),
                self.get_other_phone_2(),
                self.get_other_phone_3(),
                self.get_address_1(),
                self.get_address_2(),
                self.get_address_3(),
                self.get_address_4(),
                self.get_address_5(),
                self.get_notes()]

    def searchable(self) -> list:
        '''
        Method to provide searchable class data points.
        :return: List of all object data points which should be searchable by the user-entered input.
        '''
        return [self.get_first_name(),
                self.get_last_name(),
                self.get_id()]

    def check_empty(self) -> bool:
        '''
        Method to test if a database entry has a valid unique id. Typically used to identify entries deficient of information so they may be purged and avoid database read errors.
        '''
        if self.__id != '':
            return False
        else:
            return True
