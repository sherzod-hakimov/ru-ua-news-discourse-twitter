from transformers import T5ForConditionalGeneration, AutoTokenizer, AutoConfig
import torch
import textwrap
import pandas as pd
import re
from torch.utils.data import Dataset, DataLoader
import argparse
from tqdm import tqdm
import jsonlines
import json
import os
from accelerate import infer_auto_device_map, init_empty_weights

parser = argparse.ArgumentParser(
                    prog='Filter using Google FLAN T5 models',
                    description='Filter using Google FLAN T5 models')
parser.add_argument('-b', '--batch_size', type=int, default=512) 
args = parser.parse_args()

class MyDataset(Dataset):
    def __init__(self, list_of_tweets):
        self.data = list_of_tweets
        self.question = 'Is the following tweet related to Russia-Ukraine conflict?'

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]["en_text"]

        input_string =  "Answer the following yes/no question by reasoning step-by-step. " + \
                    "Question: %s "%(self.question) + \
                    "Tweet: %s"%(re.sub(r'<[A-Z_]+\d*>'," ", text))

        return str(self.data[idx]["tweet_id"]), input_string


# set up a simple generation function
def generate_completion(input_string, max_length=100):
    inputs = tokenizer(input_string, return_tensors="pt", padding=True).input_ids.to("cuda")
    outputs = model.generate(inputs, 
                             temperature = 0.5,
                            max_length=max_length)

    answers = []
    for inp, output in zip(input_string, outputs):
        wrapped_text = textwrap.fill(tokenizer.decode(output, skip_special_tokens=True), width=100)
        wrapped_text = re.sub(r'\s+', ' ', wrapped_text)
        answers.append(wrapped_text)

    return answers



CACHE_DIR = 'hf_cache'


## loading the model in 8-bit format
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", device_map="auto", load_in_8bit=True, cache_dir=CACHE_DIR)                                                                 
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xl", cache_dir=CACHE_DIR)



## Read jsonl tweets
all_texts = []
with jsonlines.open("input_dataset.jsonl") as fr:
    for line in fr:
        all_texts.append(line)


## Make dataloader
text_dataset = MyDataset(all_texts)
text_loader = DataLoader(text_dataset, batch_size=args.batch_size, num_workers=16)

q_answers = {}
        
for batch in tqdm(text_loader):
    twt_ids, proc_texts = batch
    answers = generate_completion(proc_texts)

    for twt_id, answer in zip(twt_ids, answers):
        q_answers[twt_id] = answer

json.dump(q_answers, open("filtered_dataset.jsonl", "w"))


