import sys

if "pytest" in sys.modules:
    import file_tool.file_data_classes as fd                                            #guards tovchange module names
    import file_tool.datastructures as fs                                               #for testing
    import file_tool.readers as rd
else:
    import file_data_classes as fd
    import datastructures as fs
    import readers as rd

class Tool:                                                                             #main class

    CUSTOMER_SAMPLE_DICT: fs.DataDict
    INVOICE_DICT: fs.DataDict


    def __init__(self,file_name) -> None:                                               #init dictionaries
        
        self.CUSTOMER_SAMPLE_DICT = fs.DataDict(type(fd.CustomerSampleFile('')))
        self.INVOICE_DICT = fs.DataDict(type(fd.Invoice('','','','')))
        read_sample = rd.SampleReader(file_name)                           

        next_ln = read_sample.next()                                                    #read sampling
        while next_ln != '':                                                            #add to CUSTOMER_SAMPLE_DICT
            self.CUSTOMER_SAMPLE_DICT.add_to_dictionary(read_sample.split_line(next_ln))
            next_ln = read_sample.next()
    
    def parse_customers(self,file_name) -> None:                                        #read and write customers

        read_customers = rd.CustomerReader(file_name)
        out = open(f"{file_name[:-4]}_TO_TEST.CSV",'w')                                 
        out.write('"CUSTOMER_CODE","FIRST_NAME","LAST_NAME"\n')

        next_ln = read_customers.next()
        while next_ln != '':
            customer = read_customers.split_line(next_ln)
            if self.CUSTOMER_SAMPLE_DICT.contains(customer.return_key()):               #print customers found in sample
                customer.write_in_file(out)
            next_ln = read_customers.next()
    
    def parse_invoices(self,file_name) -> None:                                         #read and write invoices

        read_invoices = rd.InvoiceReader(file_name)
        out = open(f"{file_name[:-4]}_TO_TEST.CSV",'w')
        out.write('"CUSTOMER_CODE","INVOICE_CODE","AMOUND","DATE"\n')

        next_ln = read_invoices.next()
        while next_ln != '':
            invoice = read_invoices.split_line(next_ln)
            if self.CUSTOMER_SAMPLE_DICT.contains(invoice.CUSTOMER_CODE):               #print invoices for customers
                invoice.write_in_file(out)                                              #in sample
                self.INVOICE_DICT.add_to_dictionary(read_invoices.split_line(next_ln))  #save those INVOICE_CODES
            next_ln = read_invoices.next()
        # print(self.INVOICE_DICT.size(),self.INVOICE_DICT)

    def parse_invoice_items(self,file_name) -> None:                                    #read and write invoice items

        read_items = rd.InvoiceItemReader(file_name)
        out = open("INVOICE_ITEMS_TO_TEST.CSV",'w')
        out.write('"INVOICE_CODE","ITEM_CODE","AMOUND","QUANTITY"\n')

        next_ln = read_items.next()
        while next_ln != '':
            item = read_items.split_line(next_ln)
            if self.INVOICE_DICT.contains(item.INVOICE_CODE):                           #write items whos invoices are
                item.write_in_file(out)                                                 #found
            next_ln = read_items.next()
                
                


def run(file1,file2,file3,file4):                                                       #run tool
    solve = Tool(file1)
    solve.parse_customers(file2)
    solve.parse_invoices(file3)
    solve.parse_invoice_items(file4)

if __name__ == '__main__':
    run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])