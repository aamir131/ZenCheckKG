from Numeric import Numeric

class Seeker(Numeric):
    def __init__(self, Id, value, page_num, parent_id, grandparent_id, closest_layout_block_id):
        super().__init__(Id, value, page_num)
        self.parent_id = parent_id
        self.grandparent_id = grandparent_id
        self.closest_layout_block_id = closest_layout_block_id
        
    
class Truther(Numeric):
    def __init__(self, Id, value, page_num):
        super().__init__(Id, value, page_num)