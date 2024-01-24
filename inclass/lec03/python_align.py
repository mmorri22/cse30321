import sys
from ctypes import c_int, c_float, c_char, addressof 

class python_example:

    int_1 = 1
    double_1 = 3.17
    char_1 = 'N'
    list_1 = [1,7,3,-1]
    char_2 = 'D'
    char_3 = 'A'
    double_2 = -22.5
    list_2 = ['Lets', 'Go', 'Irish']
    int_2 = -1000

# Print the Size of python_example
init_example = python_example()
print(sys.getsizeof(init_example))
print('Address of init_example at         : ' + str(hex(id(init_example))))
print('Address of init_example.int_1 at   : ' + str(hex(id(init_example.int_1))))
print('Address of init_example.double_1 at: ' + str(hex(id(init_example.double_1))))
print('Address of init_example.char_1 at  : ' + str(hex(id(init_example.char_1))))
print('Address of init_example.list_1 at  : ' + str(hex(id(init_example.list_1))))
print('Address of init_example.char_2 at  : ' + str(hex(id(init_example.char_2))))
print('Address of init_example.char_3 at  : ' + str(hex(id(init_example.char_3))))
print('Address of init_example.double_2 at: ' + str(hex(id(init_example.double_2))))
print('Address of init_example.list_2 at  : ' + str(hex(id(init_example.list_2))))
print('Address of init_example.int_2 at   : ' + str(hex(id(init_example.int_2))))
print('')

# Fix
class python_example_fix:

    double_1 = 3.17
    double_2 = -22.5
    int_1 = 1
    int_2 = -1000
    list_1 = [1,7,3,-1]
    list_2 = ['Lets', 'Go', 'Irish']
    char_1 = 'N'
    char_2 = 'D'
    char_3 = 'A'

# Print the Size of python_example_fix
fix_example = python_example_fix()
print(sys.getsizeof(fix_example))
print('Address of fix_example at         : ' + str(hex(id(fix_example))))
print('Address of fix_example.double_1 at: ' + str(hex(id(fix_example.double_1))))
print('Address of fix_example.double_2 at: ' + str(hex(id(fix_example.double_2))))
print('Address of fix_example.int_1 at   : ' + str(hex(id(fix_example.int_1))))
print('Address of fix_example.int_2 at   : ' + str(hex(id(fix_example.int_2))))
print('Address of fix_example.list_1 at  : ' + str(hex(id(fix_example.list_1))))
print('Address of fix_example.list_2 at  : ' + str(hex(id(fix_example.list_2))))
print('Address of fix_example.char_1 at  : ' + str(hex(id(fix_example.char_1))))
print('Address of fix_example.char_2 at  : ' + str(hex(id(fix_example.char_2))))
print('Address of fix_example.char_3 at  : ' + str(hex(id(fix_example.char_3))))