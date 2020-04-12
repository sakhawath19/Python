# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# https://www.geeksforgeeks.org/python-os-path-join-method/

import os
import pandas as pd 
import os.path
import glob
from os import walk

FNAME = "./input/{0}_file_{1}.csv"

def path_test():
    # Path 
    path = "/home"
  
    # Join various path components  
    print(os.path.join(path, "User", "Desktop", "file.txt")) 

    # it will not consider previous string of absolute path
    print(os.path.join("User", "Desktop", path, "file.txt"))

    # It will add '/' at the end of the directory  
    print(os.path.join(path, "User/Public/", "Documents", "")) 

    # Replace slash by backslash
    print(os.path.join(path, "User/Public/", "Documents", "").replace("/", "\\"))


def dirpath_dirnames_filenames():
    f = []
    for (dirpath, dirnames, filenames) in walk("./input"):
        f.extend(filenames)
        break
        
    print(f)

def specific_type_files():
    mylist = [f for f in glob.glob("./input/*.txt")]
    print(mylist)
    # it will return 
    # ['./input\\new_file.txt', './input\\test.txt']

def files_in_path():
    # avoid directories but copy the list of files
    file_list = [f for f in os.listdir() if os.path.isfile(f)]
    print(file_list)

def files_in_dir():
    # it copies all the files and folders name
    files = os.listdir("./input")

    for f in files:
        print(f)

def csv_to_df():
    # formatting the file name is a cool idea. It is easily expandable.
    file_in_folder = FNAME.format("input", 1)
    data_csv = pd.read_csv(file_in_folder)
    
    df = pd.DataFrame(data_csv)
    print(df)


def test_text_file():

    # Python code to illustrate with() alongwith write() 
    with open("./input/new_file.txt", "w+") as f1:  
        f1.write("First line!!!\n") 
        f1.write("Second line \n") 
    
    f2 = open("./input/new_file.txt", "a+")
    f2.write("appended line \n")
    f2.close()

    with open("./input/new_file.txt", "r+") as f3: 
        ln = f3.readlines()
        
        print("File mode",f3.mode)

        for line in ln: 
            print(line)

    # FNAME = "./input/{0}/subj{1}_series{2}_{3}.csv"

if __name__=="__main__":
    # test_text_file()
    # csv_to_df()
    # files_in_dir()
    # files_in_path()
    # specific_type_files()
    # dirpath_dirnames_filenames()
    path_test()
