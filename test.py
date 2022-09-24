import pytest
import string
import random
from faker import Faker

import file_tool.file_data_classes as fd


'''
    In this file automatic testing is being run for the tool
'''

'''
                    Utilities
'''
class RandomString:                                                                             #a class that generates
    string: str                                                                                 #random strings

    def __init__(self,length):                                                                  #generate a string with
        letters = string.ascii_letters+string.punctuation+string.digits                         #given length
        self.string = ''.join(random.choice(letters) for i in range(random.randint(1,length)))  #since there are no specs
                                                                                                #we test with all nonwhitespace
                                                                                                #printables

    def get_string(self):                                                                       #return string
        return self.string

'''
            Test file_data_classes.customers
'''

@pytest.fixture
def generate_customers():

    customers = []

    for i in range(100):
        customere_code = RandomString(random.randint(1,30))
        first_name = RandomString(random.randint(1,100))
        last_name = RandomString(random.randint(1,100))
        customers.append((customere_code.get_string(),first_name.get_string(),last_name.get_string()))
    
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
        customere_code = RandomString(random.randint(1,30))
        invoice_code = RandomString(random.randint(1,30))
        amound = random.uniform(0.0,1000.0)
        date = fake.date_time_between(start_date='-30y', end_date='=30y')
        invoices.append((customere_code.get_string(),invoice_code.get_string(),amound,date))
    
    return invoices



def test_dataclass_customers_init(generate_invoices):
    for invoice in generate_invoices:
        invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
        assert invoice_object.CUSTOMER_CODE == invoice[0]
        assert invoice_object.INVOICE_CODE == invoice[1]
        assert invoice_object.AMOUND == invoice[2] 
        assert invoice_object.DATE == invoice[3]



def test_dataclass_customers_write_in_file(generate_invoices):
    
    with open("tmp.csv",'w') as temp_file:
        for invoice in generate_invoices:
            invoice_object = fd.Customer(invoice[0],invoice[1],invoice[2],invoice[3])
            invoice_object.write_in_file(temp_file)
    
    with open("tmp.csv",'r') as temp_file:
        cnt = 0
        for line in temp_file:

            assert cnt<len(generate_invoices)

            correct_format = '"'+generate_invoices[cnt][0]+'","'\
                                +generate_invoices[cnt][1]+'","'\
                                +generate_invoices[cnt][2]+'","'\
                                +generate_invoices[cnt][3]+'"\n'

            assert line==correct_format
            cnt+=1

def test_dataclass_customers_return_key(generate_invoices):
    for invoice in generate_invoices:
        invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
        assert invoice_object.return_key() == invoice[0]

'''
            Test dataclasses.customers
'''
'''
@pytest.fixture
def generate_customers():

    customars = []

    for i in range(100):
        customare_code = RandomString(random.randint(1,30))
        first_name = RandomString(random.randint(1,100))
        last_name = RandomString(random.randint(1,100))
        customars.append((customare_code.get_string(),first_name.get_string(),last_name.get_string()))
    
    return customars



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