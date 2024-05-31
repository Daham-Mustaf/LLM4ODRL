from langchain.prompts import PromptTemplate
from util import(initialize_language_model,
                setup_llm_chain,
                load_odrl_template_PDF,
                set_openai_api_key,
                save_refined_odrl,
                save_odrl_from_template) 
from constants import(APIKEY)
from file_paths import OFFER_TEMPLATE, USE_CASE_DESCRIPTIONS
import os
from correction_report import( odrl_corrector,
                               OFFER_CORRECTION_REPORT )

os.environ["OPENAI_API_KEY"] = APIKEY

# Constants
OFFER_TEMPLATE




def setup_prompt_template(odrl_ontology, offer_description):
    return  PromptTemplate(template="""Generate a comprehensive ODRL Policy for \n {offer_description} based on
                                    ODRL Classes and Instructions given in the file \n odrl_ontology = {odrl_ontology}.
                                     \n Give output in well formatted as ttl""",
                                     input_variables=["odrl_ontology","offer_description"])


def odrl_offer_generator(odrl_ontology, offer_description, LLMmodel):
    # gpt-3.5-turbo
    # Initialize the language model
    llm = initialize_language_model(LLMmodel)
    prompt_template = setup_prompt_template(odrl_ontology, offer_description)
    
    chain = setup_llm_chain(llm, prompt_template)
    res = chain.run({"odrl_ontology":odrl_ontology, "offer_description":offer_description})
    # print(res)
    return res

# def process_all_use_cases(LLMmodel):
#     """Process all use cases and save the generated ODRL Offer."""
#     # Load offer context
#     pdf_path = OFFER_TEMPLATE
#     offer_context = load_odrl_template_PDF(pdf_path)
    
#     # Generate ODRL offer for each use case
#     for use_case, info in USE_CASE_DESCRIPTIONS.items():
#             if info['type'] == "Offer":
#                 odrl_offer = odrl_offer_generator(offer_context, info["description"], LLMmodel)
#                 print("Processing",use_case, " with ", LLMmodel )
#                 print(odrl_offer)
#                 save_odrl_from_template(odrl_offer, f"{use_case}_{info['type']}_{LLMmodel}")


# def process_all_use_cases_with_self_correction(LLMmodel):
#     """Process all use cases, generate ODRL offers, apply self-correction, and save the results."""
#     # Load offer context
#     pdf_path = OFFER_TEMPLATE
#     offer_context = load_odrl_template_PDF(pdf_path)
    
#     # Generate ODRL offer for each use case
#     for use_case, info in USE_CASE_DESCRIPTIONS.items():
#             if info['type'] == "Offer":
#                 odrl_offer = odrl_offer_generator(offer_context, info["description"], LLMmodel)
#                 print("Processing",use_case, " with ", LLMmodel )
#                 print(odrl_offer)
#                 save_odrl_from_template(odrl_offer, f"{info['description']}_{info['type']}_{LLMmodel}")

#                 # Apply the self-correction mechanism
#                 refined_odrl = odrl_corrector(info["description"], odrl_offer, OFFER_CORRECTION_REPORT, LLMmodel)
#                 print("Refined ODRL offer for", info["description"])
#                 print(refined_odrl)
#                 save_refined_odrl(refined_odrl, f"{use_case}_Refined_{info['type']}_{LLMmodel}")

def process_all_use_cases_with_self_correction(LLMmodel):
    """Process all use cases, generate ODRL agreements or offers, apply self-correction, and save the results."""
    # Load agreement context
    pdf_path = OFFER_TEMPLATE
    offer_context = load_odrl_template_PDF(pdf_path)
    
    # Generate ODRL policy for each use case
    for use_case, info in USE_CASE_DESCRIPTIONS.items():
        if info['type'] == "Offer":
            odrl_policy = odrl_offer_generator(offer_context, info["description"], LLMmodel)
            print("Processing", use_case, "with", LLMmodel)
            print(odrl_policy)
            
            # Generate a concise and safe filename based on the type
            filename = f"{use_case}_{info['type'].capitalize()}_{LLMmodel}"
            save_odrl_from_template(odrl_policy, filename)

            # Apply the self-correction mechanism
            refined_odrl = odrl_corrector(info["description"], odrl_policy, OFFER_CORRECTION_REPORT, LLMmodel)
            print(f"Refined ODRL {info['type'].lower()} for {use_case}:")
            print(refined_odrl)
            
            # Generate a filename for the refined ODRL
            refined_filename = f"{use_case}_Refined_{info['type'].capitalize()}_{LLMmodel}"
            save_refined_odrl(refined_odrl, refined_filename)

if __name__ == "__main__":
    # # List of models to use
    # models = ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]

    # # Process all use cases for each model
    # for model in models:
    #     process_all_use_cases(model)
       # for all cases:
    model_gpt_3 ="gpt-3.5-turbo"
    model_gpt_4 = "gpt-4"
    model_gpto = "gpt-4o"
    # process_all_use_cases(model_gpt_3)
    process_all_use_cases_with_self_correction(model_gpto)

    # # run a single case
    # pdf_path = get_pdf_path(OFFER_TEMPLATE)
    # offer = load_odrl_ontology_PDF(pdf_path)
    # odrl_offer = odrl_offer_generator(offer, USE_CASE_5_DESCRIPTION)
    # print( odrl_offer)
    # save_odrl_from_template(odrl_offer, f"{USE_CASE_5_DESCRIPTION}_Offer")

    # count token_length
    # pdf_path = get_pdf_path(OFFER_TEMPLATE)
    # pdf_text = extract_text_from_pdf(pdf_path)
    # # Measure the token length using the specified language model (here, "gpt-4")
    # token_length = measure_token_length(pdf_text, model_name=model_gpt_3)
    # print(f"Token length: {token_length}")


