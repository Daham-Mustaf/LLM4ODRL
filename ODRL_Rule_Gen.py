from langchain.prompts import PromptTemplate
from util import(initialize_language_model,
                setup_llm_chain,
                measure_token_length,
                get_pdf_path,
                load_odrl_template_PDF,
                save_odrl_from_template,
                extract_text_from_pdf,
                save_refined_odrl,
                set_openai_api_key) 
from constants import(APIKEY)
from correction_report import odrl_corrector, SET_CORRECTION_REPORT
from file_paths import RULE_TEMPLATE, USE_CASE_DESCRIPTIONS
import os


os.environ["OPENAI_API_KEY"] = APIKEY

# set_openai_api_key()

# Constants

SET_CORRECTION_REPORT
# SET_USE_CASE_DESCRIPTIONS ={
#     "use_case_10": """The Münzkabinett Museum must pay a fee of 500 euros for the digitization of the 'Todestag' artwork.""",
#     "use_case_11": """The Münzkabinett does not charge fees for the provision of data when the purpose is the enhancement of reputation or marketing promotion.""",
#     "use_case_12": """The Münzkabinett Museum seeks permission where purpose is an instance of ArchiveEvent."""
# }

# # Use case descriptions for rules
# USE_CASE_10_DESCRIPTION = "The Münzkabinett Museum must pay a fee of 500 euros for the digitization of the 'Todestag' artwork."
# USE_CASE_11_DESCRIPTION = "The Münzkabinett does not charge fees for the provision of data when the purpose is the enhancement of reputation or marketing promotion."
# USE_CASE_12_DESCRIPTION = "The Münzkabinett Museum seeks permission where purpose is an instance of ArchiveEvent."


def setup_prompt_template(odrl_ontology, rule_description):
    return  PromptTemplate(template="""Generate a comprehensive ODRL Rule for \n {rule_description} based on
                                    ODRL Classes and Instructions given in the file \n odrl_ontology = {odrl_ontology}.
                                     \n Give output in well formatted as ttl""",
                                     input_variables=["odrl_ontology","rule_description"])

def odrl_set_generator(odrl_ontology, rule_description, LLMmodel):
    # gpt-3.5-turbo
    # Initialize the language model
    llm = initialize_language_model(LLMmodel)
    prompt_template = setup_prompt_template(odrl_ontology, rule_description)
    
    chain = setup_llm_chain(llm, prompt_template)
    res = chain.run({"odrl_ontology": odrl_ontology, "rule_description": rule_description})
    # print(res)
    return res

def process_all_use_cases(LLMmodel):
    """Process all use cases and save the generated ODRL sets."""
    # Load set context
    pdf_path = RULE_TEMPLATE
    set_context = load_odrl_template_PDF(pdf_path)

    # Generate ODRL set for each use case
    for use_case, info in USE_CASE_DESCRIPTIONS.items():
            if info['type'] == "Rule":
                odrl_agreement = odrl_set_generator(set_context, info["description"], LLMmodel)
                print("Processing", use_case, " with ", LLMmodel )
                print(odrl_agreement)
                save_odrl_from_template(odrl_agreement, f"{use_case}_{info['type']}_{LLMmodel}")


def process_all_use_cases_with_self_correction(LLMmodel):
    """Process all use cases, generate ODRL sets, apply self-correction, and save the results."""
    # Load set context
    pdf_path = RULE_TEMPLATE
    set_context = load_odrl_template_PDF(pdf_path)
    
    # Generate ODRL set for each use case
    for use_case, info in USE_CASE_DESCRIPTIONS.items():
            if info['type'] == "Rule":
                # Generate the initial ODRL set
                odrl_set = odrl_set_generator(set_context, info["description"], LLMmodel)
                print(f"Original ODRL set for {use_case}:")
                print(odrl_set)
                save_odrl_from_template(odrl_set, f"{use_case}_{info['type']}_{LLMmodel}")
                # Apply the self-correction mechanism
                refined_odrl = odrl_corrector(info["description"], odrl_set, SET_CORRECTION_REPORT, LLMmodel)
                print(f"Refined ODRL set for {use_case}:")
                print(refined_odrl)
                save_refined_odrl(refined_odrl, f"{use_case}_Refined_{info['type']}_{LLMmodel}")



if __name__ == "__main__":
    # for all cases:
    model_gpt_3 ="gpt-3.5-turbo"
    model_gpt_4 = "gpt-4"
    model_gpto = "gpt-4o"

    # process_all_use_cases(model_gpt_3)
    process_all_use_cases_with_self_correction(model_gpto)
  

    
    # # run a single case
    # pdf_path = get_pdf_path(SET_TEMPLATE)
    # set = load_odrl_ontology_PDF(pdf_path)
    # odrl_set = odrl_set_generator(set, USE_CASE_10_DESCRIPTION, model_gpt_3)
    # print( odrl_set)
    # save_odrl_from_template(odrl_set, "use_case_10_Rule")


# # print(rule)

# odrl_rule = odrl_rule_generator(rule, use_case_9)
# print( odrl_rule)
# save_odrl_from_template(odrl_rule, "utest")
# pdf_text = extract_text_from_pdf(pdf_path)

# # Measure the token length using the specified language model (here, "gpt-4")
# token_length = measure_token_length(pdf_text, model_name="gpt-4")
# print(f"Token length: {token_length}")