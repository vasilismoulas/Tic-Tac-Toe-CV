import unittest
import sys
import os
from ...frontend.ui import Symbol_Table


class TestSymbol_Table(unittest.TestCase):

    def test_symbol_table(self):
        pass
        symbol_table = Symbol_Table()
        #print(type(symbol_table))


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(__file__), '../..'),"\n\n")
    unittest.main()