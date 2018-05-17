

from infix import *
from radix import *
import unittest

class Asg2Tests(unittest.TestCase):
    def test_infix_1(self):
        e = '( 1 + 2 ) * 2 * ( 2 + 1 )'
        val = eval_infix(e)        
        self.assertEqual(val, 18.0)
        
        e1 = '6**2+4*3'
        val = eval_infix(e1)
        self.assertEqual(val, 48.0)
        
        e2 = '3+3*3-3/3'
        val = eval_infix(e2)
        self.assertEqual(val, 11.0)
        
    def test_radix_1(self):
        unsortedlst = ['aaa', 'abc', 'aa', 'cc', 'cba', 'zzz']
        sortedlst = radixsort( unsortedlst, len(unsortedlst) )        
        self.assertListEqual(sortedlst,  ['aa', 'aaa', 'abc', 'cba', 'cc', 'zzz'] )  
        
        ulst1 = ['This', 'is', 'a', 'test', 'string']
        slst1 = radixsort( ulst1, len(ulst1))
        self.assertListEqual(slst1, ['This', 'a', 'is', 'string', 'test'])
        
        ulst2 = ['0ab', 'Az', 'a', 'aAa', 'string0']
        slst2 = radixsort( ulst2, len(ulst2))
        self.assertListEqual(slst2, ['0ab', 'Az', 'a', 'aAa', 'string0'])        
        

if __name__ == '__main__':  
    unittest.main()
