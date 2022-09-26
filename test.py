import pytest
import string
import random
from faker import Faker
import filecmp
from abc import abstractmethod

import file_tool.file_data_classes as fd
import file_tool.datastructures as ds
import file_tool.readers as rd
import file_tool.tool as tool


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
        letters = letters.replace('"','')
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
        
        if customer_list == [] or customer_list.size()==0:
            self.CUSTOMER_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(0,customer_list.size()-1)
            random_sample = customer_list.return_remove(random_index)
            self.CUSTOMER_CODE = random_sample.CUSTOMER_CODE
    

class RandomCustomer(RandomData,fd.Customer):

    def __init__(self) -> None:
        
        self.CUSTOMER_CODE = RandomString(30).get_string()
        self.FIRST_NAME = RandomString(100).get_string()
        self.LAST_NAME = RandomString(100).get_string()


class RandomInvoice(RandomData,fd.Invoice):

    def __init__(self,fake,customer_list = []) -> None:
        
        if customer_list == [] or customer_list.size() == 0:
            self.CUSTOMER_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(0,customer_list.size()-1)
            self.CUSTOMER_CODE = customer_list[random_index].return_key()
        
        self.INVOICE_CODE = RandomString(30).get_string()
        self.AMOUND = random.uniform(0.0,1000.0)
        self.DATE = fake.date_between(start_date='-30y', end_date='+30y')

class RandomInvoiceItem(RandomData,fd.InvoiceItem):

    def __init__(self,invoice_list = []) -> None:

        if invoice_list == [] or invoice_list.size() == 0:
            self.INVOICE_CODE = RandomString(30).get_string()
        else:
            random_index = random.randint(0,invoice_list.size()-1)
            self.INVOICE_CODE = invoice_list[random_index].return_key()

        self.ITEM_CODE = RandomString(30).get_string()
        self.AMOUND = random.uniform(0.0,1000.0)
        self.QUANTITY = random.randint(1,100)
        

'''
            Test file_data_classes.customers
'''
class TestCustomers:

    @pytest.fixture
    def generate_customers(self):

        customers = []

        for i in range(100):
            customere_code = RandomString(30)
            first_name = RandomString(100)
            last_name = RandomString(100)
            customers.append((customere_code.get_string(),first_name.get_string(),\
                                                        last_name.get_string()))
        
        return customers



    def test_dataclass_customers_init(self,generate_customers):
        for customer in generate_customers:
            customer_object = fd.Customer(customer[0],customer[1],customer[2])
            assert customer_object.CUSTOMER_CODE == customer[0]
            assert customer_object.FIRST_NAME == customer[1]
            assert customer_object.LAST_NAME == customer[2] 



    def test_dataclass_customers_write_in_file(self,generate_customers):
        
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

    def test_dataclass_customers_return_key(self,generate_customers):
        for customer in generate_customers:
            customer_object = fd.Customer(customer[0],customer[1],customer[2])
            assert customer_object.return_key() == customer[0]

'''
            Test file_datat_classes.invoices
'''

class TestInvoices:

    @pytest.fixture
    def generate_invoices(self):

        invoices = []
        fake = Faker()
        for i in range(100):
            customere_code = RandomString(30)
            invoice_code = RandomString(30)
            amound = random.uniform(0.0,1000.0)
            date = fake.date_between(start_date='-30y', end_date='+30y')
            invoices.append((customere_code.get_string(),invoice_code.get_string(),amound,date))
        
        return invoices



    def test_dataclass_invoices_init(self,generate_invoices):
        for invoice in generate_invoices:
            invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
            assert invoice_object.CUSTOMER_CODE == invoice[0]
            assert invoice_object.INVOICE_CODE == invoice[1]
            assert invoice_object.AMOUND == invoice[2] 
            assert invoice_object.DATE == invoice[3]



    def test_dataclass_invoices_write_in_file(self,generate_invoices):
        
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

    def test_dataclass_invoices_return_key(self,generate_invoices):
        for invoice in generate_invoices:
            invoice_object = fd.Invoice(invoice[0],invoice[1],invoice[2],invoice[3])
            assert invoice_object.return_key() == invoice[1]

'''
            Test dataclasses.invoice_items
'''

class TestInvoiceItems:

    @pytest.fixture
    def generate_invoice_items(self):

        items = []

        for i in range(100):
            invoice_code = RandomString(30)
            item_code = RandomString(30)
            amound = random.uniform(0.0,1000.0)
            quantity = random.randint(1,100)
            items.append((invoice_code.get_string(),item_code.get_string(),amound,quantity))
        
        return items



    def test_dataclass_invoice_items_init(self,generate_invoice_items):
        for item in generate_invoice_items:
            item_obect = fd.InvoiceItem(item[0],item[1],item[2],item[3])
            assert item_obect.INVOICE_CODE == item[0]
            assert item_obect.ITEM_CODE == item[1]
            assert item_obect.AMOUND == item[2] 
            assert item_obect.QUANTITY == item[3] 



    def test_dataclass_invoice_items_write_in_file(self,generate_invoice_items):
        
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

    def test_dataclass_invoice_items_return_key(self,generate_invoice_items):
        for item in generate_invoice_items:
            item_object = fd.InvoiceItem(item[0],item[1],item[2],item[3])
            assert item_object.return_key() == item[1]

'''
        Test file_data_classes.sample
'''

class TestSample:

    @pytest.fixture
    def generate_sample(self):

        samples = []

        for i in range(100):
            customer_code = RandomString(30)
            samples.append((customer_code.get_string()))
        
        return samples



    def test_dataclass_sample_init(self,generate_sample):
        for code in generate_sample:
            sample_object = fd.CustomerSampleFile(code[0])
            assert sample_object.CUSTOMER_CODE == code[0]



    def test_dataclass_sample_write_in_file(self,generate_sample):
        
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

    def test_dataclass_sample_return_key(self,generate_sample):
        for code in generate_sample:
            sample_object = fd.CustomerSampleFile(code[0])
            assert sample_object.return_key() == code[0]


'''
                Test datastructures
'''

class TestDatastructures:

    @pytest.fixture
    def generate_all_items(self):

        sample = []
        sample_set = set()

        for i in range(100):
            random_sample = RandomSample()
            while random_sample.return_key() in sample_set:
                random_sample = RandomSample()
            sample.append(random_sample)
            sample_set.add(random_sample.return_key())

        customers = []
        customer_set = set()

        for i in range(100):
            random_customer = RandomCustomer()
            while random_customer.return_key() in customer_set:
                random_customer.CUSTOMER_CODE = RandomString(30).get_string()
            customers.append(random_customer)
            customer_set.add(random_customer.CUSTOMER_CODE)
        
        invoices = []
        invoice_set = set()
        fake = Faker()

        for i in range(100):
            
            random_invoice = RandomInvoice(fake)
            while random_invoice.return_key() in invoice_set:
                random_invoice.INVOICE_CODE = RandomString(30).get_string()
            invoices.append(random_invoice)
            invoice_set.add(random_invoice.return_key())


        items = []
        item_set = set()

        for i in range(100):
            random_item = RandomInvoiceItem()
            while random_item.return_key() in item_set:
                random_item.ITEM_CODE = RandomString(30).get_string()
            items.append(random_item)
            item_set.add(random_item.return_key())



        return sample, customers, invoices, items

    def test_data_list(self, generate_all_items):
        
        for collection in generate_all_items:

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

    def test_data_dict(self, generate_all_items):

        for collection in generate_all_items:
            
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

'''
            Test read classes
'''
class FileGenerationFixture:
    @pytest.fixture
    def generate_files(self):

        customer_size = 5000
        sample_size = 10
        invoice_size = 10000
        item_size = 50000

        customers = ds.DataLists(type(fd.Customer('','','')))
        customer_set = set()

        with open('CUSTOMER.CSV','w') as file:

            file.write('"CUSTOMER_CODE","FIRSTNAME","LASTNAME"\n')
            for i in range(customer_size):
                random_customer = RandomCustomer()
                while random_customer.return_key() in customer_set:
                    random_customer.CUSTOMER_CODE = RandomString(30).get_string()
                customers.append(random_customer)
                customer_set.add(random_customer.return_key())

                random_customer.write_in_file(file)
        
        
        indices = random.sample(range(1,customers.size()),sample_size)
        customer_sample = ds.DataLists(type(fd.Customer('','','')))
        for index in indices:
            customer_sample.append(customers[index])
        
        
        samples = ds.DataLists(type(fd.CustomerSampleFile('')))
        
        with open('CUSTOMER_SAMPLE.CSV','w') as file:

            file.write('"CUSTOMER_CODE"\n')

            for i in range(sample_size):
                random_sample = RandomSample(customer_sample)
                samples.append(random_sample)
                random_sample.write_in_file(file)



        invoices = ds.DataLists(type(fd.Invoice('','','','')))
        invoice_set = set()

        with open('INVOICE.CSV','w') as file:

            file.write('"CUSTOMER_CODE","INVOICE_CODE","AMOUNT","DATE"\n')
            fake = Faker()

            for i in range(invoice_size):
                random_invoice = RandomInvoice(fake,customer_list=customers)
                while random_invoice.return_key() in invoice_set:
                    random_invoice.INVOICE_CODE = RandomString(30).get_string()
                invoices.append(random_invoice)
                invoice_set.add(random_invoice.return_key())

                random_invoice.write_in_file(file)
        

        items = ds.DataLists(type(fd.InvoiceItem('','','','')))
        item_set = set()

        with open('INVOICE_ITEM.CSV','w') as file:

            file.write('"INVOICE_CODE","ITEM_CODE","AMOUNT","QUANTITY"\n')

            for i in range(item_size):
                random_item = RandomInvoiceItem(invoice_list=invoices)
                while random_item.return_key() in item_set:
                    random_item.ITEM_CODE = RandomString(30).get_string()
                items.append(random_item)
                item_set.add(random_item.return_key())

                # print(random_item.ITEM_CODE,random_item.AMOUND)
                random_item.write_in_file(file)
        
        return samples,customers,invoices,items,sample_size

class TestReaders(FileGenerationFixture):
    def test_readers(self,generate_files):

        samples,customers,invoices,items,_ = generate_files


        sample_reader = rd.SampleReader("CUSTOMER_SAMPLE.CSV")
        next_ln = sample_reader.next()
        index = 0

        while next_ln != '':
            params = (samples[index].CUSTOMER_CODE,)
            target = samples[index].make_mycsv_format(params)
            assert  target == next_ln
            assert  target == sample_reader.split_line(next_ln).make_mycsv_format(params)
            next_ln = sample_reader.next()
            index += 1


        customer_reader = rd.CustomerReader("CUSTOMER.CSV")
        next_ln = customer_reader.next()
        index = 0

        while next_ln != '':
            params = (customers[index].CUSTOMER_CODE,customers[index].FIRST_NAME,\
                                                    customers[index].LAST_NAME)
            target = customers[index].make_mycsv_format(params)
            assert  target == next_ln
            assert  target == customer_reader.split_line(next_ln).make_mycsv_format(params)
            next_ln = customer_reader.next()
            index += 1

        
        invoice_reader = rd.InvoiceReader("INVOICE.CSV")
        next_ln = invoice_reader.next()
        index = 0

        while next_ln != '':
            params = (invoices[index].CUSTOMER_CODE,invoices[index].INVOICE_CODE,\
                                invoices[index].AMOUND,invoices[index].DATE)
            target = invoices[index].make_mycsv_format(params)
            assert  target == next_ln
            assert  target == invoice_reader.split_line(next_ln).make_mycsv_format(params)
            next_ln = invoice_reader.next()
            index += 1
        

        item_reader = rd.InvoiceItemReader("INVOICE_ITEM.CSV")
        next_ln = item_reader.next()
        index = 0

        while next_ln != '':
            params = (items[index].INVOICE_CODE,items[index].ITEM_CODE,\
                            items[index].AMOUND,items[index].QUANTITY)
            target = items[index].make_mycsv_format(params)
            assert  target == next_ln
            assert  target == item_reader.split_line(next_ln).make_mycsv_format(params)
            next_ln = item_reader.next()
            index += 1

'''
        Test full tool
'''
class TestFull(FileGenerationFixture):
    
    def test_full_light(self,generate_files):
        
        _,_,_,_,sample_size = generate_files
        tool.run('CUSTOMER_SAMPLE.CSV','CUSTOMER.CSV','INVOICE.CSV','INVOICE_ITEM.CSV')
        
        customer_reader = rd.CustomerReader("CUSTOMERS_TO_TEST.CSV")
        next_ln = customer_reader.next()
        cnt = 0

        while next_ln != '':
            customer = customer_reader.split_line(next_ln)
            next_ln = customer_reader.next()
            cnt += 1
        
        assert cnt == sample_size

        invoice_reader = rd.InvoiceReader("INVOICES_TO_TEST.CSV")
        next_ln = invoice_reader.next()

        while next_ln != '':
            invoice = invoice_reader.split_line(next_ln)
            next_ln = invoice_reader.next()
        

        item_reader = rd.InvoiceItemReader("INVOICE_ITEMS_TO_TEST.CSV")
        next_ln = item_reader.next()

        while next_ln != '':
            customer = item_reader.split_line(next_ln)
            next_ln = item_reader.next()
        

    # def test_full_hard(self,generate_files):
    #     pass

        
