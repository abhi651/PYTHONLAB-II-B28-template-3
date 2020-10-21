
""" write a program to copy contents of one list to another list"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def copy(lst):
    pass 
     
# DO NOT TOUCH THE BELOW CODE
class TestCopy(unittest.TestCase):
    
    def test_01(self):
        lst = [1,2,3,4]
        cpy = [1,2,3,4]
        self.assertEqual(copy(lst),cpy)
        
    def test_02(self):
        lst = [-1,-2,-3,-4]
        cpy = [-1,-2,-3,-4]
        self.assertEqual(copy(lst),cpy)

    def test_03(self):
        lst = [0,0,0,0]
        cpy = [0,0,0,0]
        self.assertEqual(copy(lst),cpy)

    def test_04(self):
        lst = [-1,200,0,40000]
        cpy = [-1,200,0,40000]
        self.assertEqual(copy(lst),cpy)
   
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

