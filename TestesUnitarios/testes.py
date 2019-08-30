import unittest

class TextAnalysisTests(unittest.TestCase):
    """Testes"""
    
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        print("tearDown")
        
    def testA(self):
        print("teste A")
        
    def testB(self):
        self.assertEqual(1, 2)

    @unittest.skip("WIP")
    def testC(self):
        self.assertEqual(1, 2)
        
        
if __name__ == '__main__' :
    unittest.main()