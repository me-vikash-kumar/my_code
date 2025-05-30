glossary ={'type casting':'the process of converting the value of one data type to another data type',
           'regex':'a sequence of characters that forms a search pattern',
           'list comprehension':'an elegant way to define and create lists based on existing lists',
           'error handling':'the process of responding to and recovering from errors in computer programs',
           'implicit type conversion':'the automatic conversion of values from one data type to another data type',
           'explicit type conversion':'the conversion of values from one data type to another data type with the help of type() function',
            'pandas':'a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,\n built on top of the Python programming language'
        
           }

for  key,value in glossary.items():
    print(f'>>{key.title()}:\n \t {value}')