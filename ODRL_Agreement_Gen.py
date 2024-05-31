from langchain.prompts import PromptTemplate
from util import (initialize_language_model,
                   setup_llm_chain, 
                   measure_token_length,
                    save_odrl_from_template, extract_text_from_pdf, load_odrl_template_PDF, set_openai_api_key, save_refined_odrl)
from file_paths import AGREEMENT_TEMPLATE, USE_CASE_DESCRIPTIONS

from correction_report import odrl_corrector, AGREEMENT_CORRECTION_REPORT
# Set the OpenAI API key
set_openai_api_key()

# Constants
AGREEMENT_TEMPLATE
USE_CASE_DESCRIPTIONS


def generate_odrl_agreement_prompt(odrl_context, agreement_description):
    """Generate a prompt template for ODRL agreement generation."""
    return PromptTemplate(template="""Generate a comprehensive ODRL policy for \n {agreement_description} based on
                                    ODRL Classes and Instructions given in the file \n odrl_ontology = {odrl_context}.
                                     \n Give output in well formatted as ttl""",
                                     input_variables=["agreement_description","odrl_context"])

def generate_odrl_agreement(odrl_agreement_template, agreement_description, LLMmodel):
    """Generate ODRL agreement based on the provided context and description."""
    llm = initialize_language_model(LLMmodel)
    prompt_template = generate_odrl_agreement_prompt(odrl_agreement_template, agreement_description)
    chain = setup_llm_chain(llm, prompt_template)
    res = chain.run({"odrl_context": odrl_agreement_template, "agreement_description": agreement_description})
    return res



def process_all_use_cases(LLMmodel):
    """Process all use cases and save the generated ODRL agreements."""
    # Load agreement context
    pdf_path = AGREEMENT_TEMPLATE
    agreement_context = load_odrl_template_PDF(pdf_path)
    
    # Generate ODRL agreement for each use case
    for use_case, info in USE_CASE_DESCRIPTIONS.items():
            if info['type'] == "Agreement":
                odrl_agreement = generate_odrl_agreement(agreement_context, info["description"], LLMmodel)
                print("Processing",use_case, " with ", LLMmodel )
                print(odrl_agreement)
                save_odrl_from_template(odrl_agreement, f"{info['description']}_Agreement_{LLMmodel}")


def process_all_use_cases_with_self_correction(LLMmodel):
    """Process all use cases, generate ODRL agreements, apply self-correction, and save the results."""
    # Load agreement context
    pdf_path = AGREEMENT_TEMPLATE
    agreement_context = load_odrl_template_PDF(pdf_path)
    
    # Generate ODRL agreement for each use case
    for use_case, info in USE_CASE_DESCRIPTIONS.items():
            if info['type'] == "Agreement":
                odrl_agreement = generate_odrl_agreement(agreement_context, info["description"], LLMmodel)
                print(f"ODRL agreement for {info['description']}:")
                print(odrl_agreement)
                save_odrl_from_template(odrl_agreement, f"{use_case}_{info['type']}_{LLMmodel}")

                # Apply the self-correction mechanism
                refined_odrl = odrl_corrector(info["description"], odrl_agreement, AGREEMENT_CORRECTION_REPORT, LLMmodel)
                print(f"Refined ODRL agreement for {use_case}:")
                print(refined_odrl)
                save_refined_odrl(refined_odrl, f"{use_case}_Refined_{info['type']}_{LLMmodel}")


if __name__ == "__main__":
    # for all cases:
    model_gpt_3 ="gpt-3.5-turbo"
    model_gpt_4 = "gpt-4"
    model_gpto = "gpt-4o"

    process_all_use_cases_with_self_correction(model_gpto)
    # process_all_use_cases(model_gpt_3)
    # process_all_use_cases(LLMmodel)
    # Define the models to be used
    # models = ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]
    # print()
    
    # Process use cases with each model
    # for model in models:
    #     process_all_use_cases_with_self_correction(model)


    # # run a single case
    # pdf_path = get_pdf_path(AGREEMENT_TEMPLATE)
    # agreement_context = load_odrl_ontology_PDF(pdf_path)
    # odrl_agreement = generate_odrl_agreement(agreement_context, USE_CASE_1_DESCRIPTION, model_gpt_3)
    # print( odrl_agreement)
    # save_odrl_from_template(odrl_agreement, "use_case_1_Agreement_gpt_3")
