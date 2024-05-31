from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.graphs import RdfGraph

from util import save_odrl_to_ttl, load_ontology
from file_paths import USE_CASE_DESCRIPTIONS, ODRL_ONTOLOGY_PATH

import os
import constants
os.environ["OPENAI_API_KEY"] = constants.APIKEY

def odrl_generator( policy, LLM_model):
    llm = ChatOpenAI(temperature=0.7, model=LLM_model, verbose=True)

   
    # .get_schema
    odrl_ontology = load_ontology(ODRL_ONTOLOGY_PATH)
    odrl_ontology.load_schema()
    # print(graph.get_schema)
    policy_description = policy

    prompt_template = PromptTemplate(template="""Generate a comprehensive ODRL policy for \n {policy_description} From ODRL ontology 
                                     \n odrl_ontology = {odrl_ontology}
                                     \n Give output in well formatted as ttl""",
                                     input_variables=["odrl_ontology","policy_description"])
    
    chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)
    res = chain.run({"odrl_ontology":odrl_ontology, "policy_description":policy_description})
    # print(res)
    return res


def process_all_use_cases(model):
     for use_case, info in USE_CASE_DESCRIPTIONS.items():
            print(f"Processing {use_case} ({info['type']}) with model {model}...")
            odrl_policy = odrl_generator(info["description"], model)
            filename = f"{use_case}_{info['type']}_{model}"
            save_odrl_to_ttl(odrl_policy, filename)
            print(f"Saved ODRL policy to {filename}")

if __name__ == "__main__":
    # Define models
    models = ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]
    gpt_3 = "gpt-3.5-turbo"
    gpt_4 =  "gpt-4"
    gpt_4o ="gpt-4o"
    # Call the function to process all use cases with each model
    process_all_use_cases(gpt_4o)

 
# odrl_policy = odrl_generator(" ", use_case_1)
# print(odrl_policy)
# save_odrl_to_ttl(odrl_policy, "use_case_1_ODRL_from_ontology")

