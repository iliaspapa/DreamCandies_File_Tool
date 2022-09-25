import pytest
import string
import random
from faker import Faker
import filecmp
from abc import abstractmethod

import file_tool.file_data_classes as fd
import file_tool.datastructures as ds


'''
    In this file automatic testing is being run for the tool
'''

'''
                    Utilities
'''
class RandomString:                                                                             #a class that generates
    string: str                                                                                 #random strings

    def __init__(self,length):                                                                  #generate a string with
        letters = string.ascii_letters+string.punctuation+string.digits                         #given max length
        self.string = ''.join(random.choice(letters) for i in range(random.randint(1,length)))  #since there are no specs
                                                                                                #we test with all nonwhitespace
                                                                                                #printables

    def get_string(self):                                                                       #return string
        return self.string

class RandomData(fd.Data):

    @abstractmethod
    def __init__(self) -> None:
        pass

class RandomSample(RandomData,fd.CustomerSampleFile):

    def __init__(self,customer_list=[]) -> None:
        
        if customer_list == []:
            self.CUSTOMER_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(1,len(customer_list)-1)
            random_sample = customer_list.return_remove(random_index)
            self.CUSTOMER_CODE = random_sample.CUSTOMER_CODE
    

class RandomCustomer(RandomData,fd.Customer):

    def __init__(self) -> None:
        
        self.CUSTOMER_CODE = RandomString(30).get_string()
        self.FIRST_NAME = RandomString(100).get_string()
        self.LAST_NAME = RandomString(100).get_string()


class RandomInvoice(RandomData,fd.Invoice):

    def __init__(self,fake,customer_list = []) -> None:
        
        if customer_list == []:
            self.CUSTOMER_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(1,len(customer_list)-1)
            self.CUSTOMER_CODE = customer_list[random_index].CUSTOMER_CODE
        
        self.INVOICE_CODE = RandomString(30).get_string()
        self.AMOUND = random.uniform(0.0,1000.0)
        self.DATE = fake.date_time_between(start_date='-30y', end_date='+30y')

class RandomInvoiceItem(RandomData,fd.InvoiceItem):

    def __init__(self,invoice_list = []) -> None:

        if invoice_list == []:
            self.INVOICE_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(1,len(invoice_list)-1)
            self.INVOICE_CODE = invoice_list[random_index]

        self.ITEM_CODE = RandomString(30).get_string()
        self.AMOUND = random.uniform(0.0,1000.0)
        self.QUANTITY = random.randint(1,100)
        

'''
            Test file_data_classes.customers
'''

@pytest.fixture
def generate_customers():

    customers = []

    for i in range(100):
        customere_code = RandomString(30)
        first_name = RandomString(100)
        last_name = RandomString(100)
        customers.append((customere_code.get_string(),first_name.get_string(),\
                                                      last_name.get_string()))
    
    return customers



def test_dataclass_customers_init(generate_customers):
    for customer in generate_customers:
        customer_object = fd.Customer(customer[0],customer[1],customer[2])
        assert customer_object.CUSTOMER_CODE == customer[0]
        assert customer_object.FIRST_NAME == customer[1]
        assert customer_object.LAST_NAME == customer[2] 



def test_dataclass_customers_write_in_file(generate_customers):
    
    with open("tmp.csv",'w') as temp_file:
        for customer in generate_customers:
            customer_object = fd.Customer(customer[0],customer[1],customer[2])
            customer_object.write_in_file(temp_file)
    
    with open("tmp.csv",'r') as temp_file:
        cnt = 0
        for line in temp_file:

            assert cnt<len(generate_customers)

            correct_format = '"'+generate_customers[cnt][0]+'","'\
                                +generate_customers[cnt][1]+'","'\
                                +generate_customers[cnt][2]+'"\n'

            assert line==correct_format
            cnt+=1

def test_dataclass_customers_return_key(generate_customers):
    for customer in generate_customers:
        customer_object = fd.Customer(customer[0],customer[1],customer[2])
        assert customer_object.return_key() == customer[0]

'''
            Test file_datat_classes.invoices
'''

@pytest.fixture
def generate_invoices():

    invoices = []
    fake = Faker()
    for i in range(100):
        customere_code = RandomString(30)
        invoice_code = RandomString(30)
        amound = random.uniform(0.0,1000.0)
        date = fake.date_time_between(start_date='-30y', end_date='+30y')
        invoices.append((customere_code.get_string(),invoice_code.get_string(),amound,date))
    
    return invoices



def test_dataclass_invoices_init(generate_invoices):
    for invoice in generate_invoices:
        invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
        assert invoice_object.CUSTOMER_CODE == invoice[0]
        assert invoice_object.INVOICE_CODE == invoice[1]
        assert invoice_object.AMOUND == invoice[2] 
        assert invoice_object.DATE == invoice[3]



def test_dataclass_invoices_write_in_file(generate_invoices):
    
    with open("tmp.csv",'w') as temp_file:
        for invoice in generate_invoices:
            invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
            invoice_object.write_in_file(temp_file)
    
    with open("tmp.csv",'r') as temp_file:
        cnt = 0
        for line in temp_file:

            assert cnt<len(generate_invoices)

            correct_format = '"'+generate_invoices[cnt][0]+'","'\
                                +generate_invoices[cnt][1]+'","'\
                                +str(generate_invoices[cnt][2])+'","'\
                                +str(generate_invoices[cnt][3])+'"\n'

            assert line==correct_format
            cnt+=1

def test_dataclass_invoices_return_key(generate_invoices):
    for invoice in generate_invoices:
        invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
        assert invoice_object.return_key() == invoice[1]

'''
            Test dataclasses.invoice_items
'''

@pytest.fixture
def generate_invoice_items():

    items = []

    for i in range(100):
        invoice_code = RandomString(30)
        item_code = RandomString(30)
        amound = random.uniform(0.0,1000.0)
        quantity = random.randint(1,100)
        items.append((invoice_code.get_string(),item_code.get_string(),amound,quantity))
    
    return items



def test_dataclass_invoice_items_init(generate_invoice_items):
    for item in generate_invoice_items:
        item_obect = fd.InvoiceItem(item[0],item[1],item[2],item[3])
        assert item_obect.INVOICE_CODE == item[0]
        assert item_obect.ITEM_CODE == item[1]
        assert item_obect.AMOUND == item[2] 
        assert item_obect.QUANTITY == item[3] 



def test_dataclass_invoice_items_write_in_file(generate_invoice_items):
    
    with open("tmp.csv",'w') as temp_file:
        for item in generate_invoice_items:
            item_object = fd.InvoiceItem(item[0],item[1],item[2],item[3])
            item_object.write_in_file(temp_file)
    
    with open("tmp.csv",'r') as temp_file:
        cnt = 0
        for line in temp_file:

            assert cnt<len(generate_invoice_items)

            correct_format = '"'+generate_invoice_items[cnt][0]+'","'\
                                +generate_invoice_items[cnt][1]+'","'\
                                +str(generate_invoice_items[cnt][2])+'","'\
                                +str(generate_invoice_items[cnt][3])+'"\n'

            assert line==correct_format
            cnt+=1

def test_dataclass_invoice_items_return_key(generate_invoice_items):
    for item in generate_invoice_items:
        item_object = fd.InvoiceItem(item[0],item[1],item[2],item[3])
        assert item_object.return_key() == item[1]

'''
        Test file_data_classes.sample
'''

@pytest.fixture
def generate_sample():

    samples = []

    for i in range(100):
        customer_code = RandomString(30)
        samples.append((customer_code.get_string()))
    
    return samples



def test_dataclass_sample_init(generate_sample):
    for code in generate_sample:
        sample_object = fd.CustomerSampleFile(code[0])
        assert sample_object.CUSTOMER_CODE == code[0]



def test_dataclass_sample_write_in_file(generate_sample):
    
    with open("tmp.csv",'w') as temp_file:
        for code in generate_sample:
            sample_object = fd.CustomerSampleFile(code[0])
            sample_object.write_in_file(temp_file)
    
    with open("tmp.csv",'r') as temp_file:
        cnt = 0
        for line in temp_file:

            assert cnt<len(generate_sample)

            correct_format = '"'+generate_sample[cnt][0]+'"\n'

            assert line==correct_format
            cnt+=1

def test_dataclass_sample_return_key(generate_sample):
    for code in generate_sample:
        sample_object = fd.CustomerSampleFile(code[0])
        assert sample_object.return_key() == code[0]


'''
                Test datastructures
'''

@pytest.fixture
def generate_customers_and_invoice_items():

    sample = []
    sample_set = set()

    for i in range(10000):
        random_sample = RandomSample()
        while random_sample.return_key() in sample_set:
            random_sample = RandomSample()
        sample.append(random_sample)
        sample_set.add(random_sample.return_key())

    customers = []
    customer_set = set()

    for i in range(10000):
        random_customer = RandomCustomer()
        while random_customer.return_key() in customer_set:
            random_customer.CUSTOMER_CODE = RandomString(30).get_string()
        customers.append(random_customer)
        customer_set.add(random_customer.CUSTOMER_CODE)
    
    invoices = []
    invoice_set = set()
    fake = Faker()

    for i in range(10000):
        
        random_invoice = RandomInvoice(fake)
        while random_invoice.return_key() in invoice_set:
            random_invoice.INVOICE_CODE = RandomString(30).get_string()
        invoices.append(random_invoice)
        invoice_set.add(random_invoice.return_key())


    items = []
    item_set = set()

    for i in range(10000):
        random_item = RandomInvoiceItem()
        while random_item.return_key() in item_set:
            random_item.ITEM_CODE = RandomString(30).get_string()
        items.append(random_item)
        item_set.add(random_item.return_key())



    return sample, customers, invoices, items

def test_data_list(generate_customers_and_invoice_items):
    
    for collection in generate_customers_and_invoice_items:

        dl = ds.DataLists(type(collection[0]))
        for entry in collection:
            dl.append(entry)
        
        dl_result = dl.return_list()
        assert dl_result == collection
        
        with open("tmp1.csv",'w') as temp_file:
            dl.write_in_file(temp_file)
        
        with open("tmp2.csv",'w') as temp_file:
            for entry in collection:
                entry.write_in_file(temp_file)
        
        assert filecmp.cmp("tmp1.csv","tmp2.csv")

def test_data_dict(generate_customers_and_invoice_items):

    for collection in generate_customers_and_invoice_items:
        
        dd = ds.DataDict(type(collection[0]))
        for entry in collection:
            dd.add_to_dictionary(entry)
        
        dd_result = dd.return_list()
        assert dd_result == collection
        
        dd2 = ds.DataDict(type(collection[0]))
        for entry in collection:
            dd2[entry.return_key()] = entry
        
        dd2_result = dd2.return_list()
        assert dd2_result == collection

        for entry in collection:
            assert dd.contains(entry.return_key())

        with open("tmp1.csv",'w') as temp_file:
            dd.write_in_file(temp_file)
        
        with open("tmp2.csv",'w') as temp_file:
            for entry in collection:
                entry.write_in_file(temp_file)
        
        assert filecmp.cmp("tmp1.csv","tmp2.csv")


# @pytest.fixture
# def generate_sample_file():
#     with open('CUSTOMER_CODE.CSV','w') as file:
#         for i in range(1000):

