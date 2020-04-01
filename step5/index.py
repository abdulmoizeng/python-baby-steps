# File Handling in Python
import os

# File open in write mode
test_file = open('test.txt', 'wb')
# Printing the file mode, in this case : wb > write mode
print(test_file.mode)
# File name
print(test_file.name)
# Writing into the File
test_file.write(bytes('Some thing special\n', 'UTF-8'))
# Closing file
test_file.close()

# File open in read mode
test_file = open('test.txt', 'r+')
# Reading the text file
print(test_file.read())
# Uncomment the line below to remove the file as well.
# os.remove('test.txt')
