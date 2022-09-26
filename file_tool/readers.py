from abc import ABC, abstractmethod
import sys
import datetime 
import io

if "pytest" in sys.modules:
    import file_tool.file_data_classes as fd
else:
    import file_data_classes as fd

class Reader(ABC):

    OPEN_FILE: io.TextIOWrapper

    def __init__(self,filename) -> None:
        self.OPEN_FILE = open(filename,'r')
        self.OPEN_FILE.readline()

    def next(self) -> str:
        ln =  self.OPEN_FILE.readline()
        # print(ln)
        if ln=='':
            self.OPEN_FILE.close()
        return ln
    
    def split_line(self,full_line) -> list:
        res = []
        argument = ""
        chr = 1
        while chr < len(full_line):
            if full_line[chr] == '"' and (full_line[chr+1]=='\n' or \
                                          (full_line[chr+1]==',' and full_line[chr+2]=='"')):
                res.append(argument)
                argument = ""
                chr+=1
                if full_line[chr]=='\n':
                    break
                chr+=2
                continue
            argument += full_line[chr]
            chr+=1
        # print(res,len(res))
        return res


class SampleReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)

    def split_line(self, full_line) -> fd.CustomerSampleFile:
        return fd.CustomerSampleFile(super().split_line(full_line)[0])


class CustomerReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line) -> fd.Customer:
        customer_code, first_name, last_name = super().split_line(full_line)
        return fd.Customer(customer_code, first_name, last_name)


class InvoiceReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line) -> fd.Invoice:
        customer_code, invoice_code, amound, date = super().split_line(full_line)
        # print(amound)
        # print(float(amound))
        # print(date)
        # print(datetime.datetime.strptime(date,'%Y-%m-%d').date())
        return fd.Invoice(customer_code, invoice_code, float(amound),\
                 datetime.datetime.strptime(date,'%Y-%m-%d').date())


class InvoiceItemReader(Reader):

    def __init__(self, filename) -> None:
        super().__init__(filename)
    
    def split_line(self, full_line) -> fd.InvoiceItem:
        invoice_code, item_code, amound, quantity = super().split_line(full_line)
        return fd.InvoiceItem(invoice_code, item_code, float(amound),int(quantity))



 