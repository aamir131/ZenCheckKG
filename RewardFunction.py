from itertools import chain, combinations

class RewardFunction:
    def __init__(self, calculated_probabilities):
        self.calculated_probabilities = calculated_probabilities

    def __call__(self, attribute_list):
        if sum(2**i for i in attribute_list) in self.calculated_probabilities:
            return self.calculated_probabilities[sum(2**i for i in attribute_list)]
        
        power_set = chain.from_iterable(combinations(attribute_list, r) for r in range(len(attribute_list)+1))
        
        m = 0
        for attribute_sublist in power_set:
            k = self.calculated_probabilities[sum(2**i for i in attribute_sublist)] 
            if k in self.calculated_probabilities:
                m = max(m, self.calculated_probabilities[k])
        return m