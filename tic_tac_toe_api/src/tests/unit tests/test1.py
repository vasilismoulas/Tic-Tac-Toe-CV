import unittest
import sys
import os
from frontend.ui.symbol_table import Symbol_Table

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))



class TestSymbol_Table(unittest.TestCase):

    def test_symbol_table(self):
        pass
        symbol_table = Symbol_Table()
        #print(type(symbol_table))


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(__file__), '../..'),"\n\n")
    unittest.main()