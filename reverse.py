
""" write a program to copy the contents from one array to another array in reverse order"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def reverse(lst):
    pass
     
# DO NOT TOUCH THE BELOW CODE
class TestReverse(unittest.TestCase):
    
    def test_01(self):
        lst = [1,2,3,4]
        rev = [4,3,2,1]
        self.assertEqual(reverse(lst),rev)

    def test_02(self):
        lst = [-1,-2,-3,-4]
        rev = [-4,-3,-2,-1]
        self.assertEqual(reverse(lst),rev)  

    def test_03(self):
        lst = [0,0,0,0]
        rev = [0,0,0,0]
        self.assertEqual(reverse(lst),rev)  

    def test_04(self):
        lst = [100,-2,0,40000]
        rev = [40000,0,-2,100]
        self.assertEqual(reverse(lst),rev)    
            
if __name__ == '__main__':
    unittest.main(verbosity=2)

