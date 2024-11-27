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

[![](https://mermaid.ink/img/pako:eNqdVctu2zgU_RWCgwIzgJ3KD8mxF7OJDU8wdl1YLlpUKga0eCULlUgNRSVO0_x7LyWFkd0ki2hhiOQ593HuMXVPI8mBzmiiWHEgu3koCD7v3pE1SwW5knkhBQhdNvu7efA-pP9UORNkxURSsQTIDo6a_Llj5XcyhzJSaaFTKf4K6ftvDWu13BnaarUmyyrlTESGlBcZ09BBrdaBgXxUMoKyTEXSHvy7DEK6mW9X-BbSdtO_WpuYPmRx_0oqBZFJSrZVBuVTzC1ytxCnAjhpIgh5mwHHqpemYYTZhrHKTr_Er_a1Js152a4M6r8nVPBRQcEURn9srE18wtl82AV19o3QMpPJXQdkns2mPu5vPj8LAcGfC-ov_MD8kGtRpslBl2dR_W3g3wnNjo0o56fXgQ84Rp1GLwVYfAnmaanTDAUjiyPDgZ2EsXXVL1bHKylEM42S3KYaJWN7yKyBSL__98-Qcpkbgyn4v0oV5LXF6E9jgjNggsJCSW5YhgKbqAaG07fWOsUlIEBZnA2HI2hxhZI3NbLUqop0paAGLnct0CjaIEGoNDogUluvdoDGqm3mJiXUDaBFW9O2p6koKrRTLBWJrE9PesCXFqtqq9ZxtiaQ1dTXdxn-IVov4gKMQDGOZvZHHMcs4j1sR34Hs-QTx2mX_duU68NsVBy7VCPaW7mm2DfnXVnuJZ9wZrk8Grlj9wWuFeFTgQZAK2pJGMmlAoKGZCV6mJQHxoHImOyzCmqtcxYdUMv-43A4qn96lzU14Zyakrzx1F3MbUnjgTddDF5tZ_sm7tkgOpfJk64ueB1dmXuu6_C0EGPuRy54wDpcb7ofv9pE7feGDJeYeGrJw0s2eXEoLXlj83IPnFfzntXsb1sqHwPvWOG5rOfU65YaReDGsaU6juvtR69SF1-eRB6dmDcaOJPfqLRHc1B4UXH8Qt6bQCHVB7ytQjrDVw4xqzId0lA8IJRVWuKNG9EZ3izQo0pWyYHOYpaVuKpq985Thtd3bncLJujsnh7pDPNfjDzvcuiMxkNn4LiTHr3DbW904U2H04FjzsbudPTQoz-kxBDOhdujwFMt1br5iNff8jro1xph6nj4BRCwhYY?type=png)](https://mermaid.live/edit#pako:eNqdVctu2zgU_RWCgwIzgJ3KD8mxF7OJDU8wdl1YLlpUKga0eCULlUgNRSVO0_x7LyWFkd0ki2hhiOQ593HuMXVPI8mBzmiiWHEgu3koCD7v3pE1SwW5knkhBQhdNvu7efA-pP9UORNkxURSsQTIDo6a_Llj5XcyhzJSaaFTKf4K6ftvDWu13BnaarUmyyrlTESGlBcZ09BBrdaBgXxUMoKyTEXSHvy7DEK6mW9X-BbSdtO_WpuYPmRx_0oqBZFJSrZVBuVTzC1ytxCnAjhpIgh5mwHHqpemYYTZhrHKTr_Er_a1Js152a4M6r8nVPBRQcEURn9srE18wtl82AV19o3QMpPJXQdkns2mPu5vPj8LAcGfC-ov_MD8kGtRpslBl2dR_W3g3wnNjo0o56fXgQ84Rp1GLwVYfAnmaanTDAUjiyPDgZ2EsXXVL1bHKylEM42S3KYaJWN7yKyBSL__98-Qcpkbgyn4v0oV5LXF6E9jgjNggsJCSW5YhgKbqAaG07fWOsUlIEBZnA2HI2hxhZI3NbLUqop0paAGLnct0CjaIEGoNDogUluvdoDGqm3mJiXUDaBFW9O2p6koKrRTLBWJrE9PesCXFqtqq9ZxtiaQ1dTXdxn-IVov4gKMQDGOZvZHHMcs4j1sR34Hs-QTx2mX_duU68NsVBy7VCPaW7mm2DfnXVnuJZ9wZrk8Grlj9wWuFeFTgQZAK2pJGMmlAoKGZCV6mJQHxoHImOyzCmqtcxYdUMv-43A4qn96lzU14Zyakrzx1F3MbUnjgTddDF5tZ_sm7tkgOpfJk64ueB1dmXuu6_C0EGPuRy54wDpcb7ofv9pE7feGDJeYeGrJw0s2eXEoLXlj83IPnFfzntXsb1sqHwPvWOG5rOfU65YaReDGsaU6juvtR69SF1-eRB6dmDcaOJPfqLRHc1B4UXH8Qt6bQCHVB7ytQjrDVw4xqzId0lA8IJRVWuKNG9EZ3izQo0pWyYHOYpaVuKpq985Thtd3bncLJujsnh7pDPNfjDzvcuiMxkNn4LiTHr3DbW904U2H04FjzsbudPTQoz-kxBDOhdujwFMt1br5iNff8jro1xph6nj4BRCwhYY)

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

## License


