from dotenv import find_dotenv, load_dotenv
import os

_ = load_dotenv(find_dotenv())

standard_prompt = '''Provide a clear and concise answer to the following question. 
Do not include extra explanation or unrelated details.

Question: {question}
Answer:'''


domain_prompt = '''Provide a clear and concise answer to the following question. 
Focus strictly on pizza-related topics. 
Avoid extra explanation or unrelated details.

Question: {question}
Answer:'''


onto_instruction = """You are a specialized model for answering questions using ontology-based knowledge.

Refer to the following Pizza Ontology when responding to questions:

{ontology}
"""

instruction = "You are an advanced model specializing in question answering."

prompt_list = {"standard": {"instruct": instruction, "prompt": standard_prompt},
               "domain": {"instruct": instruction, "prompt": domain_prompt}, 
               "onto": {"instruct": instruction, "prompt":  standard_prompt}}

datasets_path = {
    "rdf": "dataset/pizza.owl",
    "omn": "dataset/manchester.omn",
    "ofn": "dataset/owlfunctional.ofn",
    "owx": "dataset/owlxml.owx",
    "ttl": "dataset/turtle.ttl"
}

models_list = [
    # Small
    "meta-llama/Llama-3.2-1B-Instruct",
    "Qwen/Qwen2.5-0.5B-Instruct",
    
    # Medium
    "meta-llama/Llama-3.1-8B-Instruct",
    "Qwen/Qwen2.5-7B-Instruct",
    
    # Large
    "meta-llama/Llama-3.3-70B-Instruct",
    "Qwen/Qwen2.5-72B-Instruct",
]

huggingface_token = os.environ['HUGGINGFACE_ACCESS_TOKEN']
openai_token = os.environ['OPENAI_KEY']

questions = {
    "1": "What are the three main toppings of an American Pizza?",
    "2": "What is the spiciness of a Pepperoni Topping Pizzas?",
    "3": "Is a MargheritaPizza a VegetarianPizza?",
    "4": "What distinguishes Italian pizza toppings from American pizza toppings?",
    "5": "What is a hot and spicy herb commonly used as a pizza topping?",
    "6": "What is a mild and meaty pizza topping?",
    "7": "Which is a spicy vegetarian pizza?",
    "8": "What are the two types of tomato toppings used in pizza?",
    "9": "Which types of cheese pizzas are typically prepared with a maximum of one topping?",
    "10": "Which are incompatible toppings? (e.g., meat + vegetarian)",
}


# Load the JSON data
with open("dataset/60qas.json", 'r', encoding='utf-8') as f:
    larger_qas = json.load(f)


