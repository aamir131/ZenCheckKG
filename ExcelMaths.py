from enum import Enum
class ExcelNumber:
    
    class ScalarType(Enum):
        K = 3
        M = 6
        B = 9
        N = 0
    
    class Signed(Enum):
        Negative = "-"
        Positive = "+"
        Unclear = ""
        
    class QuantityType(Enum):
        Pounds = "£"
        Dollar = "$"
        Percentage = "%"
        Unclear = ""
    
    def tree_equal(self, other):
        if other.n == self.n: return True
        if "." not in self.n and "." not in other.n: return False
        if "." in self.n and (len(self.n) - self.n.find(".") >= len(other.n) - other.n.find(".") or "." not in other.n):
            numbers_after_dot = len(self.n) - self.n.find(".") - 1
            tree = ([f'%.{i}f' % round(float(self.n)+0.0000000000001, i) for i in range(numbers_after_dot, 0, -1)] + [str(int(round(float(self.n)+0.000000000001, 0)))])
            return other.n in tree
        return other == self
    
    def initialise_absolutes(self, s: str):
        print(s[0])
        if s[0] in ExcelNumber.QuantityType:
            print("in here")
            self.quantity_type = ExcelNumber.QuantityType[s[0]]
            s = s[1:]
        if s[-1] in "kmb":
            print("over here", " kmb".find(s[-1]) * 3, s[-1])
            self.scalar_val = ExcelNumber.ScalarType[s[-1].find(" kmb") * 3]
            s = s[:-2]
        if any(not i.isdigit() for i in s): raise TypeError("Should be of type number")
        self.val = s
        
    def __init__(self, s: str):
        if len(s) == 0: raise TypeError("Empty String Passed to ExcelNumber Type")
        s = s.lower().replace("bn", "b")
        print(s)
        self.quantity_type: ExcelNumber.QuantityType = ExcelNumber.QuantityType.Unclear
        self.signed_type: ExcelNumber.Signed = ExcelNumber.Signed.Unclear
        self.val = ""
        
        match s:
            case _ if s[0] == "(" and s[-1] == ")":
                self.signed_type = ExcelNumber.Signed.Negative
                self.initialise_absolutes(s[1:-1])
            case _ if s[0] in ExcelNumber.Signed:
                self.signed_type = ExcelNumber.Signed[s[0]]
                self.initialise_absolutes(s[1:])
            case _ if all(i.isdigit() for i in s[:-1]) and (s[-1] in "kmb" or s[-1].isdigit()):
                self.initialise_absolutes(s)
            case _:
                raise TypeError("Did not match any case")

    # TODO: consider the case when they are both not of type percentage
    def percentage_equal(self, other):
        p_type = ExcelNumber.QuantityType.Percentage
        if self.QuantityType.value == p_type and other.quantity_type.value == p_type:
            return ExcelNumber(self.val) == ExcelNumber(other.val)
        
        if self.QuantityType.value == p_type:
            return ExcelNumber(other.val) in [ExcelNumber(ExcelNumber.divide_by_exp(self.val, 2)), 
                                              ExcelNumber(self.val)]
        return False
        
    def divide_by_exp(val: str, exp: int):
        if exp == 0: return val
        if not "." in val:
            if exp < len(val):
                return val[:-exp] + "." +val[-exp:]
            return "0." + "0" * (exp - len(val)) + val
        if "." in val:
            return ExcelNumber.divide_by_exp(val.replace(".", ""), exp + len(val) - val.find(".") - 1)
        
    def __eq__(self, other) -> bool:
        if self.QuantityType == ExcelNumber.QuantityType.Percentage:
            return self.percentage_equal(other)
        if self.QuantityType != other.QuantityType: return False
        
        if self.Signed.value != ExcelNumber.Signed.Unclear and other.Signed.value != ExcelNumber.Signed.Unclear:
            if self.Signed != other.Signed:
                return False
        
        return ExcelNumber.scalars_equal(other)
        
    def scalars_equal(self, other):
        s = ExcelNumber(ExcelNumber.divide_by_exp(self.val, 9 - self.scalar_val.value))
        o = ExcelNumber(ExcelNumber.divide_by_exp(other.val, 9 - other.scalar_val.value)) 
        if self.scalar_val.value != 0 and other.scalar_val.value != 0: return s == o
        if self.scalar_val.value == 0 and other.scalar_val.value == 0:
            k1 = [ExcelNumber(ExcelNumber.divide_by_exp(self.val, 3 * i)) for i in range(0, 4)]
            k2 = [ExcelNumber(ExcelNumber.divide_by_exp(other.val, 3 * i)) for i in range(0, 4)]
            return any(i==j for i in k1 for j in k2)
        if self.scalar_val.value == 0:
            return any(o==ExcelNumber(ExcelNumber.divide_by_exp(self.val, 3*i)) for i in range(4))
        return other == self