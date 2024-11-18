import unittest
from ExcelMaths import ExcelNumber
from ExcelNumberTestCases import test_cases

class TestExcelMaths(unittest.TestCase):
    def test_multiple_initializations(self):
        
        for case in test_cases:
            with self.subTest(s = case.param):
                e_num = ExcelNumber(s = case.param)
                self.assertEqual(e_num.val, case.expected_value, 
                                 f"Value mismatch for {case.param}: {e_num.val} != {case.expected_value}")
                self.assertEqual(e_num.quantity_type, case.expected_quantity_type,
                                 f"Quantity type mismatch for {case.param}: {e_num.quantity_type} != {case.expected_quantity_type}")
                self.assertEqual(e_num.scalar_type, case.expected_scalar_type,
                                 f"Scalar type mismatch for {case.param}: {e_num.scalar_type} != {case.expected_scalar_type}")
                self.assertEqual(e_num.signed_type, case.expected_signed_type,
                                 f"Signed type mismatch for {case.param}: {e_num.signed_type} != {case.expected_signed_type}")                
    
    def test_numbers_equal(self):
        for case in test_cases_equal:
            with self.subTest(a = case.param1, b = case.param2):
                e_num1 = ExcelNumber(s = case.param1)
                e_num2 = ExcelNumber(s = case.param2)
            
                
if __name__ == '__main__':
    unittest.main()