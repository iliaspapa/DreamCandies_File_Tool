from abc import ABC, abstractmethod
import datetime 
import io

import file_tool.file_data_classes as fd




class Reader(ABC):

    OPEN_FILE: io.TextIOWrapper

    def __init__(self,filename) -> None:
        self.OPEN_FILE = open(filename,'r')

    def next(self) -> str:
        ln =  self.OPEN_FILE.readline()
        if ln=='':
            self.OPEN_FILE.close()
        return ln
    
    def split_line(self,full_line):
        res = []
        argument = ""
        for chr in range(1,len(full_line)):
            if full_line[chr] == '"' and (full_line[chr+1]==',' or full_line[chr+1]=='\n'):
                res.append(argument)
                argument = ""
                chr+=1
                if full_line[chr]=='\n':
                    break
                continue
            argument += full_line[chr]
        return res


class CustomerSampleFile(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)

    def split_line(self, full_line):
        return super().split_line(full_line)[0]


class CustomerReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line):
        customer_code, first_name, last_name = super().split_line(full_line)
        return fd.Customer(customer_code, first_name, last_name)


class InvoiceReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line):
        customer_code, invoice_code, amound, date = super().split_line(full_line)
        return fd.Customer(customer_code, invoice_code, float(amound), datetime.date(date))


class InvoiceItemReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line):
        invoice_code, item_code, amound, quantity = super().split_line(full_line)
        return fd.Customer(invoice_code, item_code, float(amound),int(quantity))



 