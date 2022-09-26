# DreamCandies_File_Tool

## - Main Tool
## - Automated Testing of tool
<br><br>
<h1><b><center>Main Tool</center></b></h1>

<h2>How to use</h2>

To install requirements:

run:
>pip install -r requirements.txt

To run tool:

 go to folder "file_tool" and run:
>python tool.py <path\to\CUSTOMER_SAMPLE.CSV> <path\to\CUSTOMER.CSV> <path\to\INVOICE.CSV> <path\to\INVOICE_ITEM.CSV>

Results will be in the "CUSTOMERS_TO_TEST.CSV", "INVOICES_TO_TEST.CSV" and "INVOICE_ITEMS_TO_TEST.CSV" files

<h2>Project stracture</h2>

<h3> File Data Classes </h3>


file: "file_data_classes.py"

classes: Data(template), CustomerSamleFile, Customer, Invoice, InvoiceItem

- Date: This is an abstruct class that guides what methods should be implimented, and provides some helper code.
    - \_\_init__ (method): template with no functionality.
    - write_in_file (method): template with no functionality. 
    ### <a name="write_in_file_item"></a>
    - return_key (method): template with no functionality.
    ### <a name="return_key_item"></a>
    - make_mycsv_format (method): takes a list of parameters and returns them in the csv format that database files are.
- CustomerSampleFile (inherits: Data): This class creates items extracted from the Customer_Sample file and performs basic operations.
    - CUSTOMER_CODE (attribute:str).
    - \_\_init__ (method): initialises attibute(s).
    - write_in_file (method): writes in a given open file classes data formated by Data.make_mycsv_format.
    - return_key (method): returns a proposed key if item is to be put in a dictionary
- Customer (inherits: Data): This class creates items extracted from the Customer file and performs basic operations.
    - CUSTOMER_CODE (attribute:str).
    - FIRST_NAME (attribute:str).
    - LAST_NAME (attribute:str).
    - \_\_init__ (method): initialises attibute(s).
    - write_in_file (method): writes in a given open file classes data formated by Data.make_mycsv_format.
    - return_key (method): returns a proposed key if item is to be put in a dictionary
- Invoice (inherits: Data): This class creates items extracted from the Invoice file and performs basic operations.
    - CUSTOMER_CODE (attribute:str).
    - INVOICE_CODE (attribute:str).
    - AMOUND (attribute:float).
    - DATE (attribute:date).
    - \_\_init__ (method): initialises attibute(s).
    - write_in_file (method): writes in a given open file classes data formated by Data.make_mycsv_format.
    - return_key (method): returns a proposed key if item is to be put in a dictionary
- InvoiceItem (inherits: Data): This class creates items extracted from the Customer_Sample file and performs basic operations.
    - INVOICE_CODE (attribute:str).
    - ITEM_CODE (attribute:str).
    - AMOUND (attribute:float).
    - QUANTITY (attribute:int).
    - \_\_init__ (method): initialises attibute(s).
    - write_in_file (method): writes in a given open file classes data formated by Data.make_mycsv_format.
    - return_key (method): returns a proposed key if item is to be put in a dictionary

<h3> Datastructurs </h3>


file: "datastructures.py"

classes: DataCollections(template), DataLists, DataDict

- DataCollections: This is an abstruct class that guides what methods should be implimented, and provides some helper code. It is intended to provide containers with a specific datatype.
    - DATA_TYPE (attribute:type): Saves the type of the data in the container.
    - \_\_init__ (method): gets and saves the datatype to be held in the container
    - return_list (method): template with no functionality.
    - write_in_file (method): template with no functionality.
    - size (method): template with no functionality.
- DataLists (inherits: DataCollections): This class implements a list of items that have a specific type. The methods implemented are what are used so far.
    - LIST (attribute:list).
    - append (method): places a new item on the end of the list.
    - \_\_getitem__ (operator [] read): returns an item at a given index.
    - return_remove (method): returns an item at a given index and removes it.
    - return_list (method): returns container as a simple list.
    - write_in_file (method): calls the [write_in_file method for any object](#write_in_file_item) in the container.
    - size (method): returns the size of the container.
- DataDict (inherits: DataCollections): This class implements a dictionary of items that have a specific type. The methods implemented are what are used so far.
    - DICTIONARY (attribute:dict).
    - add_to_dictionary (method): gets an [appropriate key](#return_key_item).
    - \_\_getitem__ (operator [] read): returns an item at a given key.
    - \_\_setitem__ (operator [] write): see add_to_dictionary
    - contains (method): returns True if key is in dictionary.
    - return_list (method): returns container as a simple list.
    - write_in_file (method): calls the [write_in_file method for any object](#write_in_file_item) in the container.
    - size (method): returns the size of the container.


<h3> Read Classes </h3>


file: "readers.py"

classes: Reader(template), SamleReader, CustomerReader, InvoiceReader, InvoiceItemReader

- Reader: This is a template class that implements most of the functionality of reading as strings and formating afterwards, csv file such as the ones given. 
    - OPEN_FILE (attribute:io.TextIOWrapper): This is the opened file.
    - \_\_init__ (method): gets a filename and opens the file.
    - next (method): returns the next line as a string. Also closes the file at the end.
    - split_line: gets a string such as the one returned by Reader.next() and splits it to return actual contents in a list of strings.
- SampleReader (inherits: Reader): This class extends Reader for data in the Customer_Sample file.
    - \_\_init__ (method): calls Reader.\_\_init__()
    - split_line (method): calls Reader.split_line() to get a list of strings and returns a CustomerSampleFile object.
- CustomareReader (inherits: Reader): This class extends Reader for data in the Customer file.
    - \_\_init__ (method): calls Reader.\_\_init__()
    - split_line (method): calls Reader.split_line() to get a list of strings and returns a Customer object.
- InvoiceReader (inherits: Reader): This class extends Reader for data in the Invoice file.
    - \_\_init__ (method): calls Reader.\_\_init__()
    - split_line (method): calls Reader.split_line() to get a list of strings and returns a Invoice object.
- InvoiceItem (inherits: Reader): This class extends Reader for data in the Invoice_Item file.
    - \_\_init__ (method): calls Reader.\_\_init__()
    - split_line (method): calls Reader.split_line() to get a list of strings and returns a InvoiceItem object.


<h3> Tool Class </h3>


file: "tool.py"

classes: Tool

- Tool: This class implements the main algorithm of the tool. It reads all the files, extracts relevant data and creates the output files.
    - CUSTOMER_SAMPLE_DICT (attribute: DataDict): holds all the data from Customer_Samples.
    - INVOICE_DICT (attribute: DataDict): holds all the relevant data for invoices.
    - \_\_init__ (method): initalizes the dictionaries, gets the filename and reads the Customer_Sample file, and saves all the data from it.
    - parse_customers (method): Gets the filename for the Customers file, parses the file and prints in the file all data for the customers found on the CUSTOMER_SAMPLE_DICT.
    - parse_invoices (method): Gets the filename for the Invoice file, parses the file and prints in the file all data for the invoices of customers found on the CUSTOMER_SAMPLE_DICT. Also, saves all data from those invoices.
    - parse_invoice_items (method): Gets the filename for the Invoice_Items file, parses the file and prints in the file all data for the items of invoices found on the INVOICE_DICT.
<br><br>
<h1><center>Automated Testing of Tool</center></h1>

<h2>How to use</h2>

To install requirements:

run:
>pip install -r requirements.txt

To run tests:

run:
>pytest -v test.py

<h2>Test stracture</h2>

file: "test.py"

<h3> Utility Classes </h3>

classes: RandomString, RandomData(template), RandomSample, RandomCustomer, RandomInvoice, RandomInvoiceItem

- RandomString: This class generates random strings up to a given lenght.
    - \_\_init__ (method): Generates the string.
    - get_string (method): Returns it as a string.
- RandomData (inherits: file_data_classes.Data): This is an abstruct class that guides what methods should be implimented.
     - \_\_init__ (method): template with no functionality.
- RandomSample (inherits:RandomData,file_data_classes.CustomerSampleFile): This class implements random Customer_Sample objects.
    - \_\_init__ (method): Generate Sample either randomly or from a list of Customers.
- RandomCustomer (inherits:RandomData,file_data_classes.Customer): This class implements random Customer objects.
<a name="generate_from_list"></a>
    - \_\_init__ (method): Generate Customer randomly.
- RandomInvoice (inherits:RandomData,file_data_classes.Invoice): This class implements random Invoice objects.
    - \_\_init__ (method): Generate Invoice either randomly or from a list of Customers.
- RandomInvoiceItem (inherits:RandomData,file_data_classes.InvoiceItem): This class implements random invoice_item objects.
    - \_\_init__ (method): Generate invoice_item either randomly or from a list of Invoices.

<h3> Test Data classes </h3>

classes: TestCustomers, TestInvoices, TestInvoiceItems, TestSamples

- TestCustomers: This class conducts testing for the file_data_classes.Customer class.
    - generate_customers (fixture): generates a list of 100 customer data
    - test_dataclass_customer_init (test): tests file_data_classes.Customer.\_\_init__()
    - test_dataclass_customer_write_in_file (test): tests file_data_classes.Customer.write_in_file()
    - test_dataclass_customer_return_key (test): tests file_data_classes.Customer.return_key()
- TestInvoices: This class conducts testing for the file_data_classes.Invoice class.
    - generate_invoices (fixture): generates a list of 100 invoice data
    - test_dataclass_invoice_init (test): tests file_data_classes.Invoice.\_\_init__()
    - test_dataclass_invoice_write_in_file (test): tests file_data_classes.Invoice.write_in_file()
    - test_dataclass_invoice_return_key (test): tests file_data_classes.Invoice.return_key()
- TestInvoiceItems: This class conducts testing for the file_data_classes.InvoiceItems class.
    - generate_invoice_items (fixture): generates a list of 100 invoice item data
    - test_dataclass_invoice_item_init (test): tests file_data_classes.InvoiceItems.\_\_init__()
    - test_dataclass_invoice_items_write_in_file (test): tests file_data_classes.InvoiceItem.write_in_file()
    - test_dataclass_invoice_item_return_key (test): tests file_data_classes.InvoiceItem.return_key()
- TestSample: This class conducts testing for the file_data_classes.CustomerSampleFile class.
    - generate_sample (fixture): generates a list of 100 sample data
    - test_dataclass_sample_init (test): tests file_data_classes.CustomersampleFile.\_\_init__()
    - test_dataclass_sample_write_in_file (test): tests file_data_classes.CustomerSampleFile.write_in_file()
    - test_dataclass_samples_return_key (test): tests file_data_classes.CustomerSampleFile.return_key()

<h3> Test Datastructure Class</h3>

class: TestDatastructure 

- TestDatastructure: This classconducts testing of the datastructure classes.
    - generate_all_items (fixture): generates 100 items for each class with non-repeating "primary keys"
    - test_data_list (test): tests file_data_classes.DataList class.
    - test_data_dict (test): tests file_data_classes.DataDict class.

<h3> Main Tool Classes </h3>

classes: FileGenerationFixture, TestReaders, Testfull

- FileGenerationFixture: sets size for its file, and generates all files that would be needed. Also all files are consistent with eachother. This is avhieved using the [generate from list](#generate_from_lists) featurs of the RandomData classes. WARNING: full size tests might be very slow and generate 400MB in data.
    - generate_files (fixture): the functiton that implements the above.
- TestReaders: tests the readers classes using the generated files.
    - test_reader (test): the functiton that implements the above.
- TestFull: This class conducts end-to-end testing of the tool.
    - test_full_light: call the full tool on the files generated and check that result file exist and have no major errors. Note: this does not fully check if results are correct.