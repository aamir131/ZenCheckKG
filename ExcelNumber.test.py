import unittest
from ExcelMaths import ExcelNumber
from ExcelNumberTestCases import test_cases, equality_checks, neq_checks

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
        for case in equality_checks:
            with self.subTest(a = case[0], b = case[1]):
                e_num1 = ExcelNumber(s = case[0])
                e_num2 = ExcelNumber(s = case[1])
                self.assertTrue(e_num1 == e_num2)
                
    def test_numbers_not_equal(self):
        for case in neq_checks:
            with self.subTest(a = case[0], b = case[1]):
                e_num1 = ExcelNumber(s = case[0])
                e_num2 = ExcelNumber(s = case[1])
                self.assertFalse(e_num1 == e_num2)
            
                
if __name__ == '__main__':
    unittest.main()