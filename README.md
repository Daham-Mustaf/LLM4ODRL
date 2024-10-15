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

[![](https://mermaid.ink/img/pako:eNqdVP-PmjAU_1dI71e8Q0A8-WHJchqzqOECJksml6UrDyUHLYGS6Yz_-14BUZzZLusP5L2-z5e29PVImIiAuGRb0Hynrach13Csp5s1Ld-1KZSsSHKZCI5zb01xOV9vlsuVNq-SiHIG2hqyPKUSVKXFNN-y-tHoYuH7i8hywYHLsin2AB6XIhXbwyYk51B7pYUMydsFrYbnbbypvxx4X5cd6QoCPLokd3w-R1GidkNTdLok2tXi_nD0a8fO7ckHJrIMnagilzfwINgEkFEuE_YUHLikDCPtCy-T7U7egr1Zoz3bUzxCKO_tpAva01-u6tN_LQSDskz4tiUt5o3WYt5OBC8rXEoaD5goCmD1T1zh305VpcX4yPIhTjhEWp99vgjaYPBJmfZyFOjuQh_geU0-X7e538-D4KY-6-dqa2piMT_vqm-IQT3hnwHtTZOHFGpynKSp-xBPohGM9FIW4h3cB8uy2njwM4nkzjXz_TVRqTZEqMeHibi8lufEVhx_mOf_L7HrjnafMcPRsePYwPFXgatL30gwpkQ6CcOg9B8SeAnO7j2qSu5QiU4yKDKaRPjOHJVQSOQOMgiJi2EEMa1S7PSQnxBKKymwbxhxZVGBTgpRbXfEjWlaYlbl2HUwTSi2c3aG5JQT90j2xHWMR9s0rMlkZBrGxHJGOjnUs6Y1sk3bNp-HY_vZcU46-SUEChiP48lwPDJsa2g4BsY6ATwfUayaZ7F-HWuHbzVeGZ5-A6-8lUs?type=png)](https://mermaid.live/edit#pako:eNqdVP-PmjAU_1dI71e8Q0A8-WHJchqzqOECJksml6UrDyUHLYGS6Yz_-14BUZzZLusP5L2-z5e29PVImIiAuGRb0Hynrach13Csp5s1Ld-1KZSsSHKZCI5zb01xOV9vlsuVNq-SiHIG2hqyPKUSVKXFNN-y-tHoYuH7i8hywYHLsin2AB6XIhXbwyYk51B7pYUMydsFrYbnbbypvxx4X5cd6QoCPLokd3w-R1GidkNTdLok2tXi_nD0a8fO7ckHJrIMnagilzfwINgEkFEuE_YUHLikDCPtCy-T7U7egr1Zoz3bUzxCKO_tpAva01-u6tN_LQSDskz4tiUt5o3WYt5OBC8rXEoaD5goCmD1T1zh305VpcX4yPIhTjhEWp99vgjaYPBJmfZyFOjuQh_geU0-X7e538-D4KY-6-dqa2piMT_vqm-IQT3hnwHtTZOHFGpynKSp-xBPohGM9FIW4h3cB8uy2njwM4nkzjXz_TVRqTZEqMeHibi8lufEVhx_mOf_L7HrjnafMcPRsePYwPFXgatL30gwpkQ6CcOg9B8SeAnO7j2qSu5QiU4yKDKaRPjOHJVQSOQOMgiJi2EEMa1S7PSQnxBKKymwbxhxZVGBTgpRbXfEjWlaYlbl2HUwTSi2c3aG5JQT90j2xHWMR9s0rMlkZBrGxHJGOjnUs6Y1sk3bNp-HY_vZcU46-SUEChiP48lwPDJsa2g4BsY6ATwfUayaZ7F-HWuHbzVeGZ5-A6-8lUs)



## License


