import unittest
from unittest.mock import patch
import act_001

class TestDemanaNom(unittest.TestCase):

    @patch('builtins.input', return_value='Joan')
    def test_demana_nom_joan(self, mock_input):
        self.assertEqual(act_001.demanaNom(), 'Joan')

    @patch('builtins.input', return_value='Anna')
    def test_demana_nom_anna(self, mock_input):
        self.assertEqual(act_001.demanaNom(), 'Anna')

if __name__ == '__main__':
    unittest.main()
