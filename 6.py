from array import *
from binascii import *

Int_Array = array('i', [1, 2, 3, 4, 5, 6])
print('\nA1 : ', Int_Array)
Bytes_array = Int_Array.tobytes()
print('Array of bytes: ', hexlify(Bytes_array))