from typing import List
from SeekerTruther import Seeker, Truther

class KnowledgeGraph:
    def __init__(self, is_seeker, is_truth, textract_obj):
        self.is_seeker, self.is_truth = is_seeker, is_truth
        self.seekers: List[Seeker] = []
        self.truths: List[Truther] = []

        self.nodes = {} # amazon textract id: textract dictionary object
        
        self.fill_knowledge_graph(textract_obj)
        self.extract_seekers()
        self.extract_truths()
        
    def fill_knowledge_graph(self, textract_obj):
        # loops over each page in the textract_obj
        child_parent = [] # tuple of (child, parent)
        for block in textract_obj:
            self.nodes[block['Id']] = block
            if not 'Relationships' in block:
                continue
            for rel in block['Relationships']: 
                if rel['Type'] == 'CHILD':
                    for child in rel['Ids']: child_parent.append((child, block['Id']))
                elif rel['Type'] == 'PARENT':
                    for child in rel['Ids']: child_parent.append((block['Id'], child))
        
        for child, parent in child_parent:
            self.nodes[child]['ParentId'] = parent 

    def add_features_to_seekers(self, fulfill_feature_func):
        # loops over each seeker Node, and then compute the missing feature using the fulfill_feature_func
        for seeker in self.seekers:
            fulfill_feature_func(seeker)
    
    def extract_seekers(self):
        for nodeId, node in self.nodes.items():
            if  self.is_seeker(node, self):
                parentId = node['ParentId'] if 'ParentId' in node else None
                grandparentId = self.nodes[parentId]['ParentId'] if parentId != None and 'ParentId' in self.nodes[parentId] else None
                closest_layout_text_id = nodeId
                while self.nodes[closest_layout_text_id]['BlockType'] != "LAYOUT_TEXT" and 'ParentId' in self.nodes[closest_layout_text_id]:
                    closest_layout_text_id = self.nodes[closest_layout_text_id]['ParentId']
                self.seekers.append(Seeker(node['Id'], node['Text'], node['Page'], 
                                           parentId, grandparentId, closest_layout_text_id))
    
    def extract_truths(self):
        for nodeId, node in self.nodes.items():
            if self.is_truth(node, self):
                child_val = self.nodes[node['Relationships'][0]['Ids'][0]]
                self.truths.append(Truther(node['Id'], child_val['Text'], child_val['Page']))
    
    def calculate_probabilities(self, attribute_list, labels):
        for seeker, truths in labels.items():
            labels[seeker] = set(truths)
        
        attribute_probabilities = {}
        for seeker in self.seekers:
            for truther in self.truths:
                if not seeker.Id in labels: continue
                idx = sum(2 ** i if attribute(seeker, truther, self.nodes) else 0 for i, attribute in enumerate(attribute_list))
                if idx not in attribute_probabilities: attribute_probabilities[idx] = [0.0, 0.0]
                attribute_probabilities[idx][truther.Id in labels[seeker.Id]] += 1.0
        
        for idx in attribute_probabilities:
            attribute_probabilities[idx] = attribute_probabilities[idx][1] / sum(attribute_probabilities[idx]) 
        return attribute_probabilities