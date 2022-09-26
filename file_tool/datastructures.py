from sys import exit
import sys
from abc import ABC, abstractmethod

if "pytest" in sys.modules:                                                         #guards tovchange module names
    import file_tool.file_data_classes as fd                                        #for testing
else:
    import file_data_classes as fd


class DataCollections(ABC):                                                         #Abstruct class for datacollections
                                                                                    #intended for strict typing
        DATA_TYPE: type                              

        def __init__(self,data_type) -> None:                                       #initialize values
            self.DATA_TYPE = data_type
        
        @abstractmethod
        def return_list(self) -> list:                                              # return a list fo the data
            pass

        @abstractmethod
        def write_in_file(self,open_file) -> None:                                  #write their data in a file
            pass

        @abstractmethod
        def size(self) -> int:                                                      #return size of datastructure
            pass



class DataLists(DataCollections):                                                   #lists of Data

    LIST: list

    def __init__(self, data_type) -> None:

         super().__init__(data_type)
         self.LIST = []
    
    def append(self,new_entry) -> None:                                             #add an item to the end of the list

        if not issubclass(type(new_entry), self.DATA_TYPE):                         #type error
            exit(f"wrong type of data it should be type {self.DATA_TYPE} not \
                                                          {type(new_entry)}")
        self.LIST.append(new_entry)
    
    def __getitem__(self,index):                                                    #operator [] read
        
        if index>=len(self.LIST):                                                   #out_of_range_error
            exit("List index out of range")
        else:
            return self.LIST[index]

    def return_remove(self,index):                                                  #return an element and remove it

        if index>=len(self.LIST):                                                   #out_of_range_error
            exit("List index out of range")
        else:
            ret = self.LIST[index]
            self.LIST.remove(ret)
            return ret

    def return_list(self) -> list:          
         return self.LIST

    def write_in_file(self, open_file) -> None:
         for i in self.LIST:
            i.write_in_file(open_file)

    def size(self) -> int:
        return len(self.LIST)



class DataDict(DataCollections):                                                    #dict of data
    
    DICTIONARY: dict

    def __init__(self, data_type) -> None:

         super().__init__(data_type)
         self.DICTIONARY = {}

    def add_to_dictionary(self, new_entry) -> None:                                 #insert key value per

        if not issubclass(type(new_entry), self.DATA_TYPE):                         #type_error
            exit(f"wrong type of data it should be type {self.DATA_TYPE} not \
                                                          {type(new_entry)}")
        self.DICTIONARY[new_entry.return_key()] = new_entry

    def __getitem__(self, key):                                                     #operator [] read

        if type(key)!=type(""):                                                     #key type_error
            exit(f"key must be a string not a {type(key)}")
        
        if key not in self.DICTIONARY:                                              #not found
            exit(f"key {key} not in the dictionary")
        
        return self.DICTIONARY[key]

    def __setitem__(self, key, value):                                              #operator [] write
        
        if type(key)!=type(""):                                                     #key type_error
            exit(f"key must be a string not a {type(key)}")
        
        self.add_to_dictionary(value)
    
    def contains(self,key):                                                         #check if key is in dict
        return key in self.DICTIONARY

    def return_list(self) -> list:
        return list(self.DICTIONARY.values())
    
    def write_in_file(self, open_file) -> None:
        for i in self.DICTIONARY.values():
            i.write_in_file(open_file)
    
    def size(self) -> int:
        return len(self.DICTIONARY)
        

        
        