import config
import scripts
from tqdm.notebook import tqdm
import pandas as pd

for model_id in config.models_list:
    model = scripts.load_pipeline(model_id = model_id, token=config.huggingface_token)

    inference = {"id": [qa['Q#'] for qa in config.larger_qas], 
                 "question": [qa['Question'] for qa in config.larger_qas], 
                 "category": [qa['Category'] for qa in config.larger_qas], 
                 "standard-answer": [], "standard-eval": [],
                 "domain-answer": [], "domain-eval":[]}
    
    for onto_type in list(config.datasets_path.keys()):
        inference[f'{onto_type}-onto-answer'] = []
        inference[f'{onto_type}-onto-eval'] = []
        
    print(f"working on: {model_id}")
    for subject, prompting in tqdm(config.prompt_list.items()):
        
        if subject == "onto":
            for onto_type, onto_path in config.datasets_path.items():
                ontology = scripts.load_ontology(onto_path)
                instruction = prompting['instruct'].format(ontology=ontology)
                for item in tqdm(config.larger_qas):
                    question = item['Question']
                    prompt = prompting['prompt'].format(question=question)
                    answer = scripts.query_llm(model, instruction, prompt)['content']
                    inference[f'{onto_type}-{subject}-answer'].append(answer)
                    inference[f'{onto_type}-{subject}-eval'].append(1)
        else:
            instruction = prompting['instruct']
            for item in tqdm(config.larger_qas):
                question = item['Question']
                prompt = prompting['prompt'].format(question=question)
                answer = scripts.query_llm(model, instruction, prompt)['content']
                inference[f'{subject}-answer'].append(answer)
                inference[f'{subject}-eval'].append(1)
                
    df = pd.DataFrame(inference)
    df.to_csv(f"results/60-qs/{model_id.split('/')[-1]}.csv", index=False)