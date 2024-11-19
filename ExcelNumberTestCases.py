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

equality_checks = [
    # Percentages
    ("0.5%", "0.5"),  # Percentage value matches its non-percentage equivalent
    ("0.5", "0.51%"),  # Percentage value matches its non-percentage equivalent
    ("-0.5%", "(0.5%)"),  # Negative percentage matches parentheses
    ("(0.5%)", "-0.5%"),  # Parentheses imply negative

    # Scalars and rounding
    ("3m", "3000k"),  # 3 million matches 3000k
    ("3m", "3000"),  # 3 million matches 3000
    ("0.075bn", "(75m)"),  # 0.075 billion matches negative 75 million
    ("(75m)", "-0.075bn"),  # Parentheses imply negative
    ("(75m)", "0.075bn"),  # Parentheses imply negative
    ("1.5b", "1500m"),  # 1.5 billion matches 1500 million
    ("0.0001b", "0.1m"),  # 0.0001 billion matches 0.1 million
    ("(0.0001b)", "-0.1m"),  # Negative equivalence with scalars

    # Rounding with precision
    ("0.075bn", "0.08bn"),  # Rounds to 0.08bn
    ("0.075bn", "0.1bn"),  # Also rounds to 0.1bn
    ("0.10bn", "0.103bn"),  # Precision-specific match
    ("0.10bn", "0.104bn"),  # Precision-specific match

    # Signed numbers
    ("5", "+5"),  # Unsigned matches positive
    ("5", "-5"),  # Unsigned matches negative
    ("+5", "5"),  # Positive matches unsigned
    ("-5", "5"),  # Negative matches unsigned
    ("(5)", "-5"),  # Parentheses imply negative

    # Currency types
    ("£2", "2"),  # Pound matches numeric
    ("$2", "2"),  # Dollar matches numeric
    ("€2", "2"),  # Euro matches numeric

    # Mixed examples
    ("£1.5m", "1.5m"),  # Currency matches numeric
    ("(£1.5m)", "-1.5m"),  # Negative pound matches negative numeric
    ("0.5k", "500"),  # Scalar matches its numeric equivalent
    ("0.075bn", "(75m)"),  # Rounding with scalar and sign consistency
    ("1.000b", "1000m"),  # Precision-based match for billion to million
    ("(1.000b)", "-1000m"),  # Negative scalar match,
    ("3m", "3001k"),
    ("0.01", "1%"),
    ("3m", "3001k"),  # Slightly off in thousands
    ("3m", "2999"),  # Slight mismatch in base numbers
    ("0.10bn", "0.1011bn"),
    ("0.10bn", "0.103bn"),
    ("0.5k", "501"),  # Scalar and numeric mismatch
    ("(0)", "0.1"),  # Parentheses zero vs a small value
]

neq_checks = [
    # Percentages
    ("1%", "0.02"),  # 1% vs 0.02 (Mismatch)
    ("50%", "0.51"),  # 50% vs 0.51 (Mismatch)
    ("(0.5%)", "0.6%"),  # -0.5% vs 0.6% (Mismatch)

    # Scalars and rounding
    ("0.075bn", "0.074bn"),  # Slightly off in billions
    ("0.100bn", "0.101bn"), 

    # Signed numbers
    ("+5", "-5"),  # Explicit positive vs explicit negative
    ("+5", "(5)"),  # Explicit positive vs implicit negative
    ("+5", "-5.01"),  # Explicit positive vs slightly different negative

    # Currency types
    ("£2", "$2"),  # Different currencies
    ("€2", "£2"),  # Different currencies
    ("£1.5m", "$1.5m"),  # Mismatched currencies with scalars

    # Mixed examples
    ("1.000b", "999m"),  # Slightly off in large numbers
    ("1.5b", "1.5m"),  # Billion vs million
    ("(0.0001b)", "0.2m"),  # Scalar mismatch in small values

    # Edge cases
    ("£0", "$0"),  # Zero with different currencies
    ("(0)", "+0"),  # Negative zero vs explicit positive zero
    ("(5)", "+5"),  # Negative parentheses vs explicit positive
]


neq_checks += [
    # Percentages
    ("1%", "0.02"),  # 1% vs 0.02 (Mismatch)
    ("50%", "0.51"),  # 50% vs 0.51 (Mismatch)
    ("(0.5%)", "0.6%"),  # -0.5% vs 0.6% (Mismatch)

    # Scalars and rounding
    ("0.075bn", "0.074bn"),  # Slightly off in billions
    ("0.100bn", "0.1011bn"),  # Too precise to match 0.100bn
    ("0.10bn", "0.109bn"),  # 0.109bn rounds to 0.11bn, not 0.10bn
    ("0.10bn", "0.105bn"),  # 0.105bn rounds to 0.11bn, not 0.10bn
    ("1.000b", "1.001b"),  # Rounding mismatch at 3 decimal places
    ("1.000b", "1.002b"),  # Cannot reconcile values even when rounded

    # Signed numbers
    ("+5", "-5"),  # Explicit positive vs explicit negative
    ("+5", "(5)"),  # Explicit positive vs implicit negative
    ("+5", "-5.01"),  # Explicit positive vs slightly different negative

    # Currency types
    ("£2", "$2"),  # Different currencies
    ("€2", "£2"),  # Different currencies
    ("£1.5m", "$1.5m"),  # Mismatched currencies with scalars

    # Mixed examples
    ("1.000b", "999m"),  # Slightly off in large numbers
    ("1.5b", "1.5m"),  # Billion vs million
    ("(0.0001b)", "0.2m"),  # Scalar mismatch in small values

    # Edge cases
    ("£0", "$0"),  # Zero with different currencies
    ("(0)", "+0"),  # Negative zero vs explicit positive zero
    ("(5)", "+5"),  # Negative parentheses vs explicit positive
]
