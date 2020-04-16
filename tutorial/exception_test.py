try:
    print("Do your operation here")
    # if there is any exception then skip this block and execute finally

finally:
    print("Finally block always will be executed")


'''
try:
    print("Try this code first")

except:
    print("If there is any exception then execute this bolock")

else:
    print("If there is no exception then do this operation")
'''


'''
# Try to open this and write in it
# If read and write option not given, exception will occur
try:
    file = open("test.txt", "r+")

    file.write("This is a test file.")

except IOError:
    print("Could not find or write in file")

else:
    print("Written content in the file successfully")
'''