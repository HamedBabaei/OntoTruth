import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from transformers import BitsAndBytesConfig
import torch


def load_pipeline(model_id, token):
    tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,                
        bnb_4bit_use_double_quant=True,   
        bnb_4bit_quant_type='nf4',         
        bnb_4bit_compute_dtype=torch.float16,  
        llm_int8_enable_fp32_cpu_offload=True   
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        quantization_config=quant_config,
        trust_remote_code=True,  
        token=token
    )
    text_gen_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device_map="auto"
    )
    return text_gen_pipeline

def query_llm(pipeline, instruction, prompt, max_new_tokens=50):
    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": prompt},
    ]
    outputs = pipeline(
        messages,
        max_new_tokens=max_new_tokens,
        pad_token_id=pipeline.tokenizer.pad_token_id
    )
    return outputs[0]["generated_text"][-1]

import re

def remove_html_comments(text):
    # This removes everything from <!-- to -->, including across multiple lines
    return re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

def collapse_blank_lines(text):
    return re.sub(r'\n\s*\n+', '\n\n', text)


    
def remove_extra_blank_lines(lines):
    cleaned_lines = [line for line in lines if line.strip() != '' or line.strip() != '    ']
    return remove_html_comments(collapse_blank_lines(' '.join(cleaned_lines)))


def load_ontology(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        ontology= file.read()
    return remove_extra_blank_lines(ontology)

