from sys import exit
from abc import ABC, abstractmethod


import file_tool.file_data_classes as fd


class DataCollections(ABC):

        DATA_TYPE: type

        def __init__(self,data_type) -> None:
            self.DATA_TYPE = data_type
        
        @abstractmethod
        def return_list(self) -> list:
            pass

        @abstractmethod
        def write_in_file(self,open_file) -> None:                                  #write their data in a file
            pass



class DataLists(DataCollections):

    LIST: list

    def __init__(self, data_type) -> None:

         super().__init__(data_type)
         self.LIST = []
    
    def append(self,new_entry) -> None:

        if type(new_entry) != self.DATA_TYPE:
            exit(f"wrong type of data it should be type {self.DATA_TYPE} not \
                                                          {type(new_entry)}")
        self.LIST.append(new_entry)

    def return_list(self) -> list:
         return self.LIST

    def write_in_file(self, open_file) -> None:
         for i in self.LIST:
            i.write_in_file(open_file)



class DataDict(DataCollections):
    
    DICTIONARY: dict

    def __init__(self, data_type) -> None:

         super().__init__(data_type)
         self.DICTIONARY = {}

    def add_to_dictionary(self, new_entry) -> None:

        if type(new_entry) != self.DATA_TYPE:
            exit(f"wrong type of data it should be type {self.DATA_TYPE} not \
                                                          {type(new_entry)}")
        self.DICTIONARY[new_entry.return_key()] = new_entry

    def __getitem__(self, key):

        if type(key)!=type(""):
            exit(f"key must be a string not a {type(key)}")
        
        if key not in self.DICTIONARY:
            exit(f"key {key} not in the dictionary")
        
        return self.DICTIONARY[key]

    def __setitem__(self, key, value):
        
        if type(key)!=type(""):
            exit(f"key must be a string not a {type(key)}")
        
        self.add_to_dictionary(value)
    
    def return_list(self) -> list:
        return list(self.DICTIONARY.values())
    
    def write_in_file(self, open_file) -> None:
        for i in self.DICTIONARY.values():
            i.write_in_file(open_file)
        

        
        