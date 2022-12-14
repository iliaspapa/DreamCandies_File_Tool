from dataclasses import dataclass
from abc import ABC, abstractmethod
import datetime



'''
    This file has all datafile classes
    It includes an abstract class Data that to be used as a template for all data classes
    It also includes all the data classes that inherit from the Data class
'''


@dataclass
class Data(ABC):                                                                #abstact class that acts as a template
                                                                                #classes must implement the following

    def __init__(self) -> None:                                                 #init data
        # return (re.escape(i) for i in list_of_params)
        pass

    @abstractmethod
    def write_in_file(self,open_file) -> None:                                  #write their data in a file
        pass
    
    @abstractmethod
    def return_key(self) -> str:                                                #return a key to be placed in a dictionary
        pass

    def make_mycsv_format(self,list_of_params) -> str:                          #return data in a printable format
        result = ""
        for i in list_of_params:
            result+='"'+str(i)+'",'
        return result[:-1]+'\n'                                                 #don't return last ,


@dataclass
class CustomerSampleFile(Data):                                                 #data for CUSTOMER_SAMPLE.CSV

    CUSTOMER_CODE: str

    def __init__(self,customer_code) -> None:
        self.CUSTOMER_CODE = customer_code

    def write_in_file(self, open_file) -> None:    
        open_file.write(super().make_mycsv_format((self.CUSTOMER_CODE,)))

    def return_key(self) -> str:
        return self.CUSTOMER_CODE
    


@dataclass
class Customer(Data):                                                           #data for CUSTOMER.CSV

    CUSTOMER_CODE: str
    FIRST_NAME: str
    LAST_NAME: str

    def __init__(self,customer_code,first_name,last_name) -> None:

        self.CUSTOMER_CODE = customer_code
        self.FIRST_NAME = first_name
        self.LAST_NAME = last_name
        super().__init__()                                                      #if Data.__init__() ever does something
        

    def write_in_file(self,open_file) -> None:

        # if '"' in self.CUSTOMER_CODE or '"' in self.FIRST_NAME or '"' in self.LAST_NAME :
        #     print(self.CUSTOMER_CODE,self.FIRST_NAME,self.LAST_NAME)
        #     exit(-1)
            
        open_file.write(super().make_mycsv_format((self.CUSTOMER_CODE,
                                                   self.FIRST_NAME,
                                                   self.LAST_NAME)))
    
    def return_key(self) -> str:
        return self.CUSTOMER_CODE
        

@dataclass
class Invoice(Data):                                                            #data for INVOICE.CSV

    CUSTOMER_CODE: str
    INVOICE_CODE: str
    AMOUND: float
    DATE: datetime.date

    def __init__(self,customer_code,invoice_code,amound,date) -> None:

        self.CUSTOMER_CODE = customer_code
        self.INVOICE_CODE = invoice_code
        self.AMOUND = amound
        self.DATE = date
        super().__init__()                                                      #if Data.__init__() ever does something

    def write_in_file(self,open_file) -> None:

        open_file.write(super().make_mycsv_format((self.CUSTOMER_CODE,
                                                   self.INVOICE_CODE,
                                                   self.AMOUND,
                                                   self.DATE)))

    def return_key(self) -> str:
        return self.INVOICE_CODE


@dataclass
class InvoiceItem(Data):                                                        #data for INVOICE_ITEM.CSV

    INVOICE_CODE: str
    ITEM_CODE: str
    AMOUND: float
    QUANTITY: int

    def __init__(self,invoice_code,item_code,amound,quantity) -> None:

        self.ITEM_CODE = item_code
        self.INVOICE_CODE = invoice_code
        self.AMOUND = amound
        self.QUANTITY = quantity
        super().__init__()                                                      #if Data.__init__() ever does something

    

    def write_in_file(self,open_file) -> None:
        # print(self.AMOUND)
        # if float(self.AMOUND):
        #     pass
        open_file.write(super().make_mycsv_format((self.INVOICE_CODE,
                                                   self.ITEM_CODE,
                                                   self.AMOUND,
                                                   self.QUANTITY)))

    def return_key(self) -> str:
        return self.ITEM_CODE
