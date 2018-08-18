import os
# **********                  Filing             **************
# File open in write mode
test_file = open('test.txt', 'wb')
print(test_file.mode)
print(test_file.name)
test_file.write(bytes('Some thing special\n', 'UTF-8'))
test_file.close()
test_file = open('test.txt', 'r+')
print(test_file.read())
os.remove('test.txt')
# File open in read mode

# *****************                     ***********************
