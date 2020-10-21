
""" write a program to to remove duplicate elements from an array"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def duplicate(lst):
    pass
     
# DO NOT TOUCH THE BELOW CODE
class TestDuplicate(unittest.TestCase):
    
    def test_01(self):
        lst = [1,1,2,3,3,3,4,4,4,4]
        dup = [1,2,3,4]
        self.assertEqual(duplicate(lst),dup)

    def test_02(self):
        lst = [0,0,0,0,0,0,0]
        dup = [0]
        self.assertEqual(duplicate(lst),dup) 

    def test_03(self):
        lst = [1,-1,2,2,-2,3,3,3,-3,4,4,4,4,0,0,0,0]
        dup = [1,-1,2,-2,3,-3,4,0]
        self.assertEqual(duplicate(lst),dup)

    def test_04(self):
        lst = [-1,-1,-1,-1,-1,-1,-1]
        dup = [-1]
        self.assertEqual(duplicate(lst),dup)       
               
if __name__ == '__main__':
    unittest.main(verbosity=2)

