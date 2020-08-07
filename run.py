# https://huggingface.co/transformers/task_summary.html (section about named entity recognition)

import sys
import fileinput
import torch
import torch.nn.functional as F

from transformers import AutoTokenizer, AutoModelForTokenClassification

def load_model(model_id):
    print(f"loading model {model_id} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_id) 			
    model = AutoModelForTokenClassification.from_pretrained(model_id)
    print(f"loading model completed")

    return model, tokenizer


def get_tokens(sequence):
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(sequence)))
    inputs = tokenizer.encode(sequence, return_tensors="pt")

    return tokens, inputs


def get_model_output(model, inputs):
    outputs = model(inputs)[0]

    return outputs


def print_result(tokens, outputs, label_list):
    print("result")

    predictions = torch.argmax(outputs, dim=2)
    predictions = predictions[0].numpy()

    for i in range(len(tokens)):
        pred_i = predictions[i]
        prob_i = F.softmax(outputs[0][i], dim=0).detach().numpy()
        print(f"{tokens[i]:10} {pred_i} {label_list[pred_i]:6} {prob_i[pred_i]:5.3f}")


label_list = [
"B-LOC",  # location start
"B-MISC", # misc start
"B-ORG",  # organisation start 
"B-PER",  # person start
"I-LOC",  # location
"I-MISC", # misc
"I-ORG",  # organisatino
"I_PER",  # person
"O"       # Outside of a named entity
]

#  https://huggingface.co/wietsedv/bert-base-multilingual-cased-finetuned-conll2002-ner
model_id = "wietsedv/bert-base-multilingual-cased-finetuned-conll2002-ner"
model, tokenizer = load_model(model_id)

print("enter a sentence and press enter")

for line in fileinput.input():
    sequence = line.rstrip()

    tokens, inputs = get_tokens(sequence)
    outputs = get_model_output(model, inputs)

    print_result(tokens, outputs, label_list)

    print("enter a sentence and press enter (or ctrl-d to exit the script)")
