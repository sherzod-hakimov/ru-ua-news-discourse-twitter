from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
import torch

from src.utils import file_utils


# Model from https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

class SentimentAnalyzer:
    def __init__(self):


        CACHE_DIR = 'hf_cache'

        model_name = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name,  cache_dir=CACHE_DIR, device_map="auto")
        self.config = AutoConfig.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir=CACHE_DIR, device_map="auto")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def process(self, input_text:str):

        encoded_input = self.tokenizer(input_text, return_tensors='pt').input_ids.to(self.device)
        output = self.model(encoded_input)
        scores = output[0][0].cpu().detach().numpy()
        scores = self.softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        max_prob = 0
        max_label = ''
        for i in range(scores.shape[0]):
            label = self.config.id2label[ranking[i]]
            prob = np.round(scores[ranking[i]], 4)

            if prob > max_prob:
                max_prob = prob
                max_label = label
        return max_label, max_prob

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()