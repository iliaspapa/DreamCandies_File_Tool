# DreamCandies_File_Tool

<h1><b><center>Main Tool</center></b></h1>

<h2>How to use</h2>

Go to folder "file_tool"
>run python tool.py <path\to\CUSTOMER_SAMPLE.CSV> <path\to\CUSTOMER.CSV> <path\to\INVOICE.CSV> <path\to\INVOICE_ITEM.CSV>

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