import unittest
from dom import Dom
class TestDom(unittest.TestCase):
    def setUp(self):
        self.c = Dom()
        self.c.attrs = {'id':[11],'class':['me','us'],'target':['_top']}
        self.c.data = 'abcd'
        print('setup')
    def test_basics(self):
        c = self.c
        self.assertEqual('abcd',c.getData())
        self.assertEqual(False,c.hasAttrs({'id':[111]}))
        self.assertEqual(True,c.hasAttrs({'id':[11]}))
        self.assertEqual(False,c.hasAttrs({'class':['me','uss']}))
        self.assertEqual(True,c.hasAttrs({'target':[]}))
def main():
    unittest.main()

if __name__ == '__main__':
    main()
