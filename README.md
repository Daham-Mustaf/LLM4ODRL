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

[![](https://mermaid.ink/img/pako:eNqlVV1v0zAU_SuWERJI7Ug_kq594GWtykRLUVMEIkHIi2_SiNQOjsM6xv47106apWUMaeQh8sc55_qee-Pc0khyoBOaKJZvyWYaCoLP8-dkyVJBLuQulwKELqr1zTR4FdI35Y4JsmAiKVkCZAN7TV5sWPGNTKGIVJrrVIqXIX31pWIt5htDWyyWZF6mnInIkHZ5xjS0UItlLzCY90pGUBSpSOqdt_MgpKvpeoGjkNaL_sXSiPqQxd0LqRREJipZlxkUR6J9K7qGOBWww1TqnTWqVoucVNpCXmfAMaG58QJhjReYQMsK4pdX1q5qv6hnBvX1HhW8V5AzheqHnOvAR5zVu01go6-ElplMblog86xWdru7-vggBAR_SNSf-YF5kUtRpMlWFyeq_jrwb4Rm-8qu093LwAessE6jvwnMPgXTtNBphoaR2Z5hLY9kmnPZQePjh5xjyTmJpBBVvQoSS4Xzpn5xJq8PvUa63de_QsrlzvSigu9lqmwJscC_bL80_VVDE7QaCpKAAMWM3jEQ3a6BuZI_LLTQqox0qcAi55saaMyrkCBUGm0RqZuObQGN9iF2FRTs4bBR79O2PdrKMRV5efii3s4N3fZpO-3WAjb6yYoZ1UGV7WAbcn0cU99k-AXVLYoTMMoxVmzyLI5jFvEOpi6_gZnykePU0-51yvV2Msj3bapx-Klcc_4nxzX21uRzPuKsIfNo4A7df5H7TyZjXSqqNxy7s2lDHfa88az3KHX9H9zjO-TeNxe8lm_MPfWtfyxjGv3ABQ9Yi-uNr4aPHsH2fkWGcww8bsj9czb6h22rVROXe-A8GvfkzP66pvIh8FaxHop6Sr2sqVEEbhw3VMdxvavBo9TZp3uTB0fNGfWc0R9U2qE7UHgfcfxn3hqhkOotXkohneCQQ8zKTIc0FHcIZaWWeNFGdIK3DHSokmWypZOYZQXOSnsbTlOGt_auWc2ZoJNbuqcTjH828LzzvjMY9p2e44469AaXvcGZN-6Pe47ZG7rjwV2H_pQSJZwzt0OBp1qqZfVbt393K_rZImyQu9_vaYan?type=png)](https://mermaid.live/edit#pako:eNqlVV1v0zAU_SuWERJI7Ug_kq594GWtykRLUVMEIkHIi2_SiNQOjsM6xv47106apWUMaeQh8sc55_qee-Pc0khyoBOaKJZvyWYaCoLP8-dkyVJBLuQulwKELqr1zTR4FdI35Y4JsmAiKVkCZAN7TV5sWPGNTKGIVJrrVIqXIX31pWIt5htDWyyWZF6mnInIkHZ5xjS0UItlLzCY90pGUBSpSOqdt_MgpKvpeoGjkNaL_sXSiPqQxd0LqRREJipZlxkUR6J9K7qGOBWww1TqnTWqVoucVNpCXmfAMaG58QJhjReYQMsK4pdX1q5qv6hnBvX1HhW8V5AzheqHnOvAR5zVu01go6-ElplMblog86xWdru7-vggBAR_SNSf-YF5kUtRpMlWFyeq_jrwb4Rm-8qu093LwAessE6jvwnMPgXTtNBphoaR2Z5hLY9kmnPZQePjh5xjyTmJpBBVvQoSS4Xzpn5xJq8PvUa63de_QsrlzvSigu9lqmwJscC_bL80_VVDE7QaCpKAAMWM3jEQ3a6BuZI_LLTQqox0qcAi55saaMyrkCBUGm0RqZuObQGN9iF2FRTs4bBR79O2PdrKMRV5efii3s4N3fZpO-3WAjb6yYoZ1UGV7WAbcn0cU99k-AXVLYoTMMoxVmzyLI5jFvEOpi6_gZnykePU0-51yvV2Msj3bapx-Klcc_4nxzX21uRzPuKsIfNo4A7df5H7TyZjXSqqNxy7s2lDHfa88az3KHX9H9zjO-TeNxe8lm_MPfWtfyxjGv3ABQ9Yi-uNr4aPHsH2fkWGcww8bsj9czb6h22rVROXe-A8GvfkzP66pvIh8FaxHop6Sr2sqVEEbhw3VMdxvavBo9TZp3uTB0fNGfWc0R9U2qE7UHgfcfxn3hqhkOotXkohneCQQ8zKTIc0FHcIZaWWeNFGdIK3DHSokmWypZOYZQXOSnsbTlOGt_auWc2ZoJNbuqcTjH828LzzvjMY9p2e44469AaXvcGZN-6Pe47ZG7rjwV2H_pQSJZwzt0OBp1qqZfVbt393K_rZImyQu9_vaYan)

# ODRL Policy Generation Workflow
## Workflow Legend
### Components by Color
- 🟡 **Yellow Components** (Parallelogram shape): Human-prepared inputs
  - Task Description
  - LLM Guidance Template
  - Self-Correction Rules

- 🔵 **Blue Components** (Rectangle shape): Machine-generated outputs
  - ODRL KG
  - Refined ODRL Knowledge Graph

- 🔴 **Red Component** (Rectangle shape): Processing
  - LLM Processing

### Supporting Knowledge (in Prepared Guidance)
- 🌸 **Pink Box**: ODRL Ontology
  - ODRL-OWL Ontology

- 🌿 **Green Box**: OSES Insights
  - Syntax Rules
  - Semantic Insights
  - Distilled Examples

### Edge Labels
- "domain requirements": Task description to LLM
- "guides validation": Task description to Self-Correction
- "guides generation": LGT to LLM
- "provides structure": Ontology to LGT
- "enriches template": OSES to LGT
- "generates": LLM to KG
- "inputs for correction": KG to SCM
- "refines": SCM to RKG

The workflow represents a novel methodology for generating ODRL policies using LLMs, combining human expertise with machine processing. It consists of three main phases: Input (human-prepared), Processing (machine), and Refinement (human-guided correction), resulting in a refined ODRL Knowledge Graph.

## Citation

If you use this code in your research, please cite:

```
@inproceedings{mustafa2024instructions,
  title={From Instructions to ODRL Usage Policies: An Ontology Guided Approach},
  author={Mustafa, Daham M. and Nadgeri, Abhishek and Collarana, Diego and Arnold, Benedikt T. and Quix, Christoph and Lange, Christoph and Decker, Stefan},
  booktitle={Proceedings of the LLM+KG Workshop at VLDB},
  year={2024}
}
```

## Authors

- Daham M. Mustafa, Fraunhofer FIT, Sankt Augustin, Germany
- Abhishek Nadgeri, Fraunhofer FIT, Sankt Augustin, Germany
- Diego Collarana, Fraunhofer FIT, Sankt Augustin, Germany & Universidad Privada Boliviana, Cochabamba, Bolivia
- Benedikt T. Arnold, Fraunhofer FIT, Sankt Augustin, Germany & RWTH Aachen University, Aachen, Germany
- Christoph Quix, RWTH Aachen University, Aachen, Germany
- Christoph Lange, Fraunhofer FIT, Sankt Augustin, Germany & RWTH Aachen University, Aachen, Germany
- Stefan Decker, Fraunhofer FIT, Sankt Augustin, Germany & RWTH Aachen University, Aachen, Germany


