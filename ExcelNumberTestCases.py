from ExcelMaths import ExcelNumber
from typing import List

class ExcelNumberTestCase:
    
    def __init__(
        self,
        param: str,
        expected_value: str,
        expected_quantity_type: ExcelNumber.QuantityType, 
        expected_scalar_type: ExcelNumber.ScalarType,
        expected_signed_type: ExcelNumber.Signed
        ):
        self.param = param
        self.expected_value = expected_value
        self.expected_quantity_type = expected_quantity_type
        self.expected_scalar_type = expected_scalar_type
        self.expected_signed_type = expected_signed_type
        
test_cases : List[ExcelNumberTestCase] = [
    # Basic numbers without any symbols
    ExcelNumberTestCase("1", "1" ,ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("11m", "11" ,ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("11k", "11",ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("118b", "118", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Unclear),
    
    # Numbers with currency symbols
    ExcelNumberTestCase("£118b", "118", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("$11k", "11", ExcelNumber.QuantityType.Dollar, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("(£11k)", "11", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Negative),
    
    # Signed numbers
    ExcelNumberTestCase("+£118b", "118", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("-£118b", "118", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(118k)", "118", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Negative),
    
    # Percentages
    ExcelNumberTestCase("11%", "11", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("+11%", "11", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("(11%)", "11", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    
    # Decimal numbers
    ExcelNumberTestCase("1.23", "1.23", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("1.23m", "1.23", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("+1.23m", "1.23", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("($1.23m)", "1.23", ExcelNumber.QuantityType.Dollar, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Negative),
    
    # Edge cases
    ExcelNumberTestCase("0", "0", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("0k", "0", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("(0)", "0", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(0%)", "0", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    
    # Invalid or unclear cases
    #ExcelNumberTestCase("", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Empty string (should raise error)
    #ExcelNumberTestCase("abc", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Invalid input
    #ExcelNumberTestCase("£abc", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Invalid number
]

test_cases += [
    # Basic numbers
    ExcelNumberTestCase("100", "100", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("0.99", "0.99", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("-100", "100", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("+100", "100", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Positive),

    # Numbers with signs and scalar types
    ExcelNumberTestCase("+1k", "1", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("-1.5m", "1.5", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(2.75b)", "2.75", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Negative),

    # Numbers with currency and scalar types
    ExcelNumberTestCase("£123m", "123", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("€500k", "500", ExcelNumber.QuantityType.Euros, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Unclear),  # Assuming Euro isn't supported yet
    ExcelNumberTestCase("+$999b", "999", ExcelNumber.QuantityType.Dollar, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Positive),

    # Percentages
    ExcelNumberTestCase("0.5%", "0.5", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("-50%", "50", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(25%)", "25", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),

    # Decimal and edge combinations
    ExcelNumberTestCase("123.456", "123.456", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("1.5b", "1.5", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("(0.0001k)", "0.0001", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Negative),

    # Edge cases
    ExcelNumberTestCase("(£0)", "0", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(0%)", "0", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),

    # Large numbers
    ExcelNumberTestCase("999999k", "999999", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("123456789m", "123456789", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("-999999b", "999999", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Negative),

    # Invalid cases (commented out as they should raise errors)
    # ExcelNumberTestCase("", "", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Empty string
    # ExcelNumberTestCase("abc", "", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Invalid input
    # ExcelNumberTestCase("£1.2.3", "", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Invalid number with multiple decimals
    # ExcelNumberTestCase("£%", "", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Unclear),  # Invalid symbol combination
]

test_cases += [
    # Combinations of signed numbers and scalars with currency symbols
    ExcelNumberTestCase("+£1.23m", "1.23", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("-$999.999k", "999.999", ExcelNumber.QuantityType.Dollar, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("(€0.0001b)", "0.0001", ExcelNumber.QuantityType.Euros, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Negative),

    # Percentages with scalars and signs
    ExcelNumberTestCase("(50.05%)", "50.05", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),

    # Complex currency combinations
    ExcelNumberTestCase("($123.456m)", "123.456", ExcelNumber.QuantityType.Dollar, ExcelNumber.ScalarType.M, ExcelNumber.Signed.Negative),
    ExcelNumberTestCase("£999.999b", "999.999", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Unclear),
    ExcelNumberTestCase("+£1k", "1", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("+£1.1k", "1.1", ExcelNumber.QuantityType.Pound, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Positive),
    ExcelNumberTestCase("+€1.1k", "1.1", ExcelNumber.QuantityType.Euros, ExcelNumber.ScalarType.K, ExcelNumber.Signed.Positive),

    # Large and small edge cases
    ExcelNumberTestCase("(0.00000001b)", "0.00000001", ExcelNumber.QuantityType.Unclear, ExcelNumber.ScalarType.B, ExcelNumber.Signed.Negative),

    # Numbers with scalars and percentages combined
    ExcelNumberTestCase("(0.5%)", "0.5", ExcelNumber.QuantityType.Percentage, ExcelNumber.ScalarType.Unclear, ExcelNumber.Signed.Negative),
]
