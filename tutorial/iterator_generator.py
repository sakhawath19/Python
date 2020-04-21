# https://stackoverflow.com/questions/17444679/reading-a-huge-csv-file
import pandas as pd 

# A simple generator function
def simple_fun():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


def from_loop():
    for n in range(4):
        yield n


# Creating a generator that will generate the data row by row
def beerDataGenerator():
    file = "./creditcard.csv"
    for row in open(file, encoding="ISO-8859-1"):
        yield row

# Reading file with pandas and chunksize
def read_file():
    for chunk in pd.read_csv("./creditcard.csv", chunksize=10000): #it will take 10000 row at a time 
        pass
        
    

if __name__ == "__main__":
    
    for item in simple_fun():
        print("item from simple function:", item) 

    for item in from_loop():
        print("item from loop:", item)

    # for data in beerDataGenerator():
    #     print("Row:", data)

    read_file()

    ###
