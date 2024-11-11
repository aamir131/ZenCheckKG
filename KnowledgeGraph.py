from SeekerTruther import Seeker, Truther

class KnowledgeGraph:
    def __init__(self, is_seeker, is_truth, textract_obj):
        self.is_seeker, self.is_truth = is_seeker, is_truth
        self.seekers, self.truths = [], []

        self.nodes = {} # amazon textract id: textract dictionary object
        
        self.fill_knowledge_graph(textract_obj)
        self.extract_seekers()
        self.extract_truths()
        
    def fill_knowledge_graph(self, textract_obj):
        # loops over each page in the textract_obj
        child_parent = [] # tuple of (child, parent)
        for block in textract_obj:
            self.nodes[block['Id']] = block
            for rel in block['Relationships']:
                if rel['Type'] == 'CHILD':
                    child_parent.append((rel['Ids'][0], block['Id']))
                elif rel['Type'] == 'PARENT':
                    child_parent.append((block['Id'], rel['Ids'][0]))
        
        for child, parent in child_parent:
            self.nodes[child]['ParentId'] = parent 

    def add_features_to_seekers(self, fulfill_feature_func):
        # loops over each seeker Node, and then compute the missing feature using the fulfill_feature_func
        for seeker in self.seekers:
            fulfill_feature_func(seeker)
    
    def extract_seekers(self):
        for node in self.nodes:
            if node['BlockType'] == 'WORD':
                if self.is_seeker(node):
                    self.seekers.append(Seeker(node['Id'] ,node['Text'], node['Page']))
    
    def extract_truths(self):
        for node in self.nodes:
            if node['BlockType'] == 'WORD':
                if self.is_truth(node):
                    self.truths.append(Truther(node['Id'] ,node['Text'], node['Page']))
    
    def calculate_probabilities(self, attribute_list, labels):
        for seeker, truths in labels:
            labels[seeker] = set(truths)
        
        attribute_probabilities = {}
        for seeker in self.seekers:
            for truther in self.truths:
                idx = sum(2 ** i if attribute(seeker, truther, self.nodes) else 0 for i, attribute in enumerate(attribute_list))
                if idx not in attribute_probabilities: attribute_probabilities[idx] = [0, 0]
                attribute_probabilities[idx][truther in labels[seeker]] += 1
        
        for idx in attribute_probabilities:
            attribute_probabilities[idx] = attribute_probabilities[idx][1] / sum(attribute_probabilities[idx]) 
        return attribute_probabilities