# From Instructions to ODRL Usage Policies: An Ontology Guided Approach

This project aims to convert instructions into ODRL (Open Digital Rights Language) usage policies using an ontology-guided approach. The approach leverages LLMs (Large Language Models) to generate accurate ODRL representations based on predefined criteria.

## Overview

The repository contains the implementation of the method, experimental results, and related scripts.

## Directory Structure

- `data/`: Dataset used for experiments.
  - `ontology/`: Contains the ODRL ontology file.
    - `odrl.ttl`: The ODRL ontology file in Turtle format.
  - `tasks/`: Contains use case files used as experiments for testing the approach.
- `llm_guidance_template/`: Contains PDF templates used to guide the LLM in generating ODRL knowledge graphs.
  - `templates/`: Subdirectory containing the PDF templates.
    - `ODRL-Agreement_Generator_template.pdf`: Template for generating ODRL Agreement policies.
    - `ODRL-Offer_Generator_Template.pdf`: Template for generating ODRL Offer policies.
    - `ODRL_Rule_Generator_template.pdf`: Template for generating ODRL Rule policies.
- `generated_odrl_from_ontology/`: Contains the ODRL knowledge graphs generated directly from the ODRL ontology.
- `generated_odrl_policy_from_template/`: Contains the ODRL knowledge graphs generated from context and self-correction mechanisms.
- `ODRL_policy_validation_shapes/`: Contains shapes for validating ODRL rules, agreements, and offers.

- `config.json`: Configuration file containing settings for the scripts.
- `constants.py`: File containing constant variables used throughout the project.
- `correction_report.py`: Script containing correction rules applied for the self-correction mechanism.
- `file_paths.py`: File handling paths used by the scripts.

## Scripts

- `ODRL_From_Ontology.py`: Script to generate ODRL knowledge graphs solely from the ontology and apply self-correction mechanisms.
- `ODRL_Agreement_Gen.py`: Script to generate agreement policies from context and apply self-correction mechanisms.
- `ODRL_Offer_Gen.py`: Script to generate offer policies from context and apply self-correction mechanisms.
- `ODRL_Rule_Gen.py`: Script to generate rule policies from context templates.
- `shacl_odrl_validator.py`: Script for SHACL validation of ODRL policies.

## Setup

Before running the scripts, ensure that you have set up an Open API key and configured the `config.json` file with the appropriate settings.

### Running the Scripts

1. Set up the Open API key.
2. Configure the `config.json` file with the necessary settings.
3. Run the desired script using Python, e.g., `python ODRL_From_Ontology.py`.
4. Follow the prompts and provide any required inputs.


## Methodology 

[![](https://mermaid.ink/img/pako:eNqdVV2PmzgU_SuWV5V2pWQKIYSEh75MRtnRJk0VIm21sKocfElQwWaN6SSdzn_vNTAMSaeRtkSKbHzO_Tg-No80lhyoT_eKFQeynUeC4PPmDVmxVJBbmRdSgNBl8347D99G9M8qZ4IsmdhXbA9kC0dNft-y8jOZQxmrtNCpFH9E9O2_DWu52BracrkiiyrlTMSGlBcZ09BDLVehgXxQMoayTMW-XfhrEUZ0Pd8scRTR9mVwuzIxA8iS4a1UCmKTlGyqDMqXmBvkbiBJBXDSRBDyIQOOVS9MwwjrGsYqe_2SoNrVmjTrZTszqE8vqPCDgoIpjP7cWJv4jLN-vw3r7GuhZSb3px7IPOt1vTxc__0qBAR_LWhwF4Tmj9yLMt0fdHkRNdiEwUlodmxEuVy9DwPAbdRp_LMAdx_DeVrqNEPByN2R4YadhenqqgedjrdSiGY3SvKQapSM7SDrDESGw3ffIsplbgym4L8qVZDXFqPfjAkugHsUFkryhWUosIlqYLj7nbXOcXsQoDpcFw63oMUVSn6pkaVWVawrBTVwsW2BRtEGCUKl8QGRuvNqD2is2mZuUkLdAFq0NW27moqiQjslUpG48-lZDzhosaq2ah1nYwJ1mgb6lOGBIKGCUhOZkJOsFHbQvDVHGJU0gmKxByAly5-NaDBg1ExwH_3fkiRhMR9g7_IzmCn3LKudDh9Srg--Uxz7VKPwr3JNZ_-P-0PHRrecxQfUBfs8v43aApddkin3OOuS8Nhxx-7VAnGXGiq3IU7sjmp7bLSbXqVufol7oWzvKnkRyoVJTyjmXgo1Oi_EWPuZCxNgPe5kthtfbaJ2e0OGKSaedeTRlHk_Fe8sxLrLzidgXc1-UXmweVZwDLy3ca_lvqTet9Q4BjdJOqpluZOdc5V69_FFaufMk7FteT9Q6YDmoPBscfxKPppAEcUzluNt4OOQQ8KqTEc0Ek8IZZWWeOvG1MfbBQZUyWp_oH7CshJnVYFXGMxThld43r0tmKD-Iz1Sf2bd2DPHtR3XnY5tz7UH9ER923JvnJFn2WPLG82ckTN-GtCvUmIE68ZzXcfC39jxrMnUdQcUeKqlWjWf9frrXqf4pyaYqp6-Ayj5jAM?type=png)](https://mermaid.live/edit#pako:eNqdVV2PmzgU_SuWV5V2pWQKIYSEh75MRtnRJk0VIm21sKocfElQwWaN6SSdzn_vNTAMSaeRtkSKbHzO_Tg-No80lhyoT_eKFQeynUeC4PPmDVmxVJBbmRdSgNBl8347D99G9M8qZ4IsmdhXbA9kC0dNft-y8jOZQxmrtNCpFH9E9O2_DWu52BracrkiiyrlTMSGlBcZ09BDLVehgXxQMoayTMW-XfhrEUZ0Pd8scRTR9mVwuzIxA8iS4a1UCmKTlGyqDMqXmBvkbiBJBXDSRBDyIQOOVS9MwwjrGsYqe_2SoNrVmjTrZTszqE8vqPCDgoIpjP7cWJv4jLN-vw3r7GuhZSb3px7IPOt1vTxc__0qBAR_LWhwF4Tmj9yLMt0fdHkRNdiEwUlodmxEuVy9DwPAbdRp_LMAdx_DeVrqNEPByN2R4YadhenqqgedjrdSiGY3SvKQapSM7SDrDESGw3ffIsplbgym4L8qVZDXFqPfjAkugHsUFkryhWUosIlqYLj7nbXOcXsQoDpcFw63oMUVSn6pkaVWVawrBTVwsW2BRtEGCUKl8QGRuvNqD2is2mZuUkLdAFq0NW27moqiQjslUpG48-lZDzhosaq2ah1nYwJ1mgb6lOGBIKGCUhOZkJOsFHbQvDVHGJU0gmKxByAly5-NaDBg1ExwH_3fkiRhMR9g7_IzmCn3LKudDh9Srg--Uxz7VKPwr3JNZ_-P-0PHRrecxQfUBfs8v43aApddkin3OOuS8Nhxx-7VAnGXGiq3IU7sjmp7bLSbXqVufol7oWzvKnkRyoVJTyjmXgo1Oi_EWPuZCxNgPe5kthtfbaJ2e0OGKSaedeTRlHk_Fe8sxLrLzidgXc1-UXmweVZwDLy3ca_lvqTet9Q4BjdJOqpluZOdc5V69_FFaufMk7FteT9Q6YDmoPBscfxKPppAEcUzluNt4OOQQ8KqTEc0Ek8IZZWWeOvG1MfbBQZUyWp_oH7CshJnVYFXGMxThld43r0tmKD-Iz1Sf2bd2DPHtR3XnY5tz7UH9ER923JvnJFn2WPLG82ckTN-GtCvUmIE68ZzXcfC39jxrMnUdQcUeKqlWjWf9frrXqf4pyaYqp6-Ayj5jAM)


## License


