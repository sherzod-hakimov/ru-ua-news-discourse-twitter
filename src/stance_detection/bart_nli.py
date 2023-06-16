from transformers import AutoModelForSequenceClassification, AutoTokenizer
from src.utils import file_utils
import torch

'''
Model from: https://huggingface.co/facebook/bart-large-mnli
'''

class BARTStanceDetector:
    def __init__(self):

        CACHE_DIR = 'hf_cache'

        self.model = AutoModelForSequenceClassification.from_pretrained('facebook/bart-large-mnli', cache_dir=CACHE_DIR, device_map="auto")
        self.tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-mnli', cache_dir=CACHE_DIR, device_map="auto")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def process(self, premise, hypothesis):

        x = self.tokenizer.encode(premise, hypothesis, return_tensors='pt',
                             truncation_strategy='only_first')
        logits = self.model(x)[0]
        entail_contradiction_logits = logits[:, [0, 2]]
        probs = entail_contradiction_logits.softmax(dim=1)
        contra_prob = round(probs[:, 0].item(), 4)
        entail_prob = round(probs[:, 1].item(), 4)
        return contra_prob, entail_prob