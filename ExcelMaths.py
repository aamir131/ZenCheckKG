from enum import Enum
class ExcelNumber:
    
    class ScalarType(Enum):
        K = 3
        M = 6
        B = 9
        Unclear = 0
    
    class Signed(Enum):
        Negative = "-"
        Positive = "+"
        Unclear = ""
        
    class QuantityType(Enum):
        Pound = "£"
        Dollar = "$"
        Percentage = "%"
        Unclear = ""
        Euros = "€"

    def __init__(self, s: str):
        if len(s) == 0: raise TypeError("Empty String Passed to ExcelNumber Type")
        s = s.lower().replace("bn", "b").replace(",", "").replace(" ", "")
        self.quantity_type: ExcelNumber.QuantityType = ExcelNumber.QuantityType.Unclear
        self.signed_type: ExcelNumber.Signed = ExcelNumber.Signed.Unclear
        self.scalar_type: ExcelNumber.ScalarType = ExcelNumber.ScalarType.Unclear
        self.val = None
        
        match s:
            case _ if s[0] == "(" and s[-1] == ")":
                self.signed_type = ExcelNumber.Signed.Negative
                self.initialise_absolutes(s[1:-1])
            case _ if s[0] in ExcelNumber.Signed:
                self.signed_type = ExcelNumber.Signed(s[0])
                self.initialise_absolutes(s[1:])
            case _ if (s[0] in ExcelNumber.QuantityType or s[0].isdigit()) and all((i.isdigit() or i == ".") for i in s[1:-1]) and (s[-1] in "kmb%" or s[-1].isdigit()):
                self.initialise_absolutes(s)
            case _:
                raise TypeError("Did not match any case")

    def initialise_absolutes(self, s: str):
        if s[0] in ExcelNumber.QuantityType:
            self.quantity_type = ExcelNumber.QuantityType(s[0])
            s = s[1:]
        elif s[-1] == "%":
            self.quantity_type = ExcelNumber.QuantityType.Percentage
            s = s[:-1]
        
        if s[-1] in "kmb":
            self.scalar_type = ExcelNumber.ScalarType(" kmb".find(s[-1]) * 3)
            s = s[:-1]
        if any((not i.isdigit() and i != ".") for i in s): raise TypeError("Should be of type number")
        self.val = s

    def tree_equal_str(a: str, b: str):
        if a == b: return True
        if "." not in a + b: return False
        if "." in a and (len(a) - a.find(".") >= len(b) - b.find(".") or "." not in b):
            numbers_after_dot = len(a) - a.find(".") - 1
            tree = ([f'%.{i}f' % round(float(a)+0.0000000000001, i) for i in range(numbers_after_dot, 0, -1)] + [str(int(round(float(a)+0.000000000001, 0)))])
            return b in tree
        return ExcelNumber.tree_equal_str(b, a)
        
    def percentage_equal(self, other):
        p_type = ExcelNumber.QuantityType.Percentage
        if self.quantity_type.value == p_type and other.quantity_type.value == p_type:
            return ExcelNumber.tree_equal_str(self.val, other.val)
        
        b, a = (self.val, other.val) if self.quantity_type == p_type else (other.val, self.val)
        return any(ExcelNumber.tree_equal_str(a, x) for x in [b, ExcelNumber.divide_by_exp(b, 2)])
        
    def divide_by_exp(val: str, exp: int) -> str:
        if exp == 0: return val
        if not "." in val:
            if exp < len(val):
                return val[:-exp] + "." +val[-exp:]
            return "0." + "0" * (exp - len(val)) + val
        return ExcelNumber.divide_by_exp(val.replace(".", ""), exp + len(val) - val.find(".") - 1)
        
    def __eq__(self, other) -> bool:
        if len({self.quantity_type, other.quantity_type} - {ExcelNumber.QuantityType.Unclear}) > 1:
            return False
        if len({self.signed_type, other.signed_type} - {ExcelNumber.Signed.Unclear}) > 1:
            return False
        
        if {ExcelNumber.QuantityType.Percentage} <= {self.quantity_type, other.quantity_type}:
            return self.percentage_equal(other)
        
        return self.scalars_equal(other)
        
    def scalars_equal(self, other):
        s = ExcelNumber.divide_by_exp(self.val, 9 - self.scalar_type.value)
        o = ExcelNumber.divide_by_exp(other.val, 9 - other.scalar_type.value)
        if self.scalar_type.value != 0 and other.scalar_type.value != 0: return ExcelNumber.tree_equal_str(s, o)
        if self.scalar_type.value == 0 and other.scalar_type.value == 0:
            k1 = [ExcelNumber.divide_by_exp(self.val, 3 * i) for i in range(0, 4)]
            k2 = [ExcelNumber.divide_by_exp(other.val, 3 * i) for i in range(0, 4)]
            return any(ExcelNumber.tree_equal_str(i, j) for i in k1 for j in k2)
        if self.scalar_type.value == 0:
            return any(ExcelNumber.tree_equal_str(o, ExcelNumber.divide_by_exp(self.val, 3*i)) for i in range(4))
        return other == self