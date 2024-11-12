from Numeric import Numeric

class Seeker(Numeric):
    def __init__(self, Id, value, page_num, paragraph_block_id = None):
        super().__init__(Id, value, page_num, paragraph_block_id)
        
    
class Truther(Numeric):
    def __init__(self, Id, value, page_num, paragraph_block_id = None):
        super().__init__(Id, value, page_num, paragraph_block_id)