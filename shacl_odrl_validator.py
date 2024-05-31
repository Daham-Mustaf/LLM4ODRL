import os

import pyshacl
from rdflib import Graph, Namespace, RDF
import os
from file_paths import (AGREEMENT_SHAPES,
                    RULE_SHAPES,
                    OFFER_SHAPES,
                    REFINED_ODRL,
                    ODRL_POLICY_DIRECTORY,
                    ODRL_POLICY_ONTOLOGY_GEN
                    )

def validate_odrl_against_shacl(odrl_ttl_path, shacl_ttl_path):
    """
    Validates the given ODRL Turtle file against the SHACL shapes.
    
    :param odrl_ttl_path: Path to the ODRL Turtle file.
    :param shacl_ttl_path: Path to the SHACL shapes Turtle file.
    :return: Tuple (conforms, num_results, num_violations)
    """
    # Load the ODRL data
    odrl_graph = Graph()
    try:
        with open(odrl_ttl_path, 'r', encoding='utf-8') as file:
            odrl_data = file.read()
            print("ODRL File Content:")
            # print(odrl_data)
        
        odrl_graph.parse(data=odrl_data, format='ttl')
        print("ODRL graph successfully parsed.")
    except Exception as e:
        print(f"Error parsing ODRL file: {e}")
        return None, None, None
    
    # Load the SHACL shapes
    shacl_graph = Graph()
    try:
        with open(shacl_ttl_path, 'r', encoding='utf-8') as file:
            shacl_data = file.read()
            print("SHACL Shapes File Content:")
            # print(shacl_data)
        
        shacl_graph.parse(data=shacl_data, format='ttl')
        print("SHACL graph successfully parsed.")
    except Exception as e:
        print(f"Error parsing SHACL shapes file: {e}")
        return None, None, None
    
    # Perform SHACL validation
    conforms, results_graph, _ = pyshacl.validate(
        data_graph=odrl_graph,
        shacl_graph=shacl_graph,
        inference='rdfs',
        abort_on_first=False,
        meta_shacl=False,
        advanced=True,
        debug=False
    )
    
    # Count the validation results
    SH = Namespace("http://www.w3.org/ns/shacl#")
    validation_results = list(results_graph.subjects(RDF.type, SH.ValidationResult))
    num_results = len(validation_results)
    
    violations = [
        result for result in validation_results
        if (result, SH.resultSeverity, SH.Violation) in results_graph
    ]
    num_violations = len(violations)
    
    return conforms, num_results, num_violations



def load_odrl_agreement_kg(directory):
    """
    Finds all ODRL agreement Turtle files in the specified directory and assigns sequential numbers.
    
    :param directory: Path to the directory containing ODRL Turtle files.
    :return: List of tuples (file number, file path) of agreement Turtle files.
    """
    agreement_files = []
    file_number = 1
    
    for filename in os.listdir(directory):
        if filename.endswith(".ttl") and "agreement" in filename.lower():
            filepath = os.path.join(directory, filename)
            agreement_files.append((file_number, filepath))
            file_number += 1
            
    return agreement_files

def load_odrl_offer_kg(directory):
    """
    Finds all ODRL offer Turtle files in the specified directory and assigns sequential numbers.
    
    :param directory: Path to the directory containing ODRL Turtle files.
    :return: List of tuples (file number, file path) of offer Turtle files.
    """
    offer_files = []
    file_number = 1
    
    for filename in os.listdir(directory):
        if filename.endswith(".ttl") and "offer" in filename.lower():
            filepath = os.path.join(directory, filename)
            offer_files.append((file_number, filepath))
            file_number += 1
            
    return offer_files

def load_odrl_rule_kg(directory):
    """
    Finds all ODRL rule Turtle files in the specified directory and assigns sequential numbers.
    
    :param directory: Path to the directory containing ODRL Turtle files.
    :return: List of tuples (file number, file path) of rule Turtle files.
    """
    rule_files = []
    file_number = 1
    
    for filename in os.listdir(directory):
        if filename.endswith(".ttl") and "rule" in filename.lower():
            filepath = os.path.join(directory, filename)
            rule_files.append((file_number, filepath))
            file_number += 1
            
    return rule_files

# def validate_all_agreements(odrl_files, shacl_shapes):
#     for odrl_file in odrl_files:
#         conforms, num_results, num_violations = validate_odrl_against_shacl(odrl_file, shacl_shapes)
#         print(f"Validation for {odrl_file}:")
#         print(f"Conforms: {conforms}")
#         print(f"Number of Results: {num_results}")
#         print(f"Number of Violations: {num_violations}")
#         print("-" * 40)

def validate_odrl_files(odrl_files, shacl_shapes):
    """
    Validates all ODRL KG files against the given SHACL shapes.
    
    :param odrl_files: List of tuples (file number, file path) of ODRL files.
    :param shacl_shapes: Path to the SHACL shapes Turtle file.
    """
    for file_number, odrl_file in odrl_files:
        conforms, num_results, num_violations = validate_odrl_against_shacl(odrl_file, shacl_shapes)
        print(f"Validation for {odrl_file}:")
        print(f"File Number: {file_number}")
        print(f"Conforms: {conforms}")
        print(f"Number of Results: {num_results}")
        print(f"Number of Violations: {num_violations}")
        print("-" * 40)

# Example usage
if __name__ == "__main__":
    import file_paths
    # Access the ODRL policy directory path from the config module
    odrl_from_template = file_paths.ODRL_POLICY_DIRECTORY
    
    print(RULE_SHAPES)



    # odrl_directory = ODRL_POLICY_DIRECTORY
    # agreement_shapes_path = AGREEMENT_SHAPES

    # offer_shapes_path = "C:/Users/mustafa/Desktop/odrl-langchane/ODRL_policy_validation_shapes/ODRL_Offer_Shape.ttl"
    # rule_shapes_path = "C:/Users/mustafa/Desktop/odrl-langchane/ODRL_policy_validation_shapes/ODRL_Rule_Shape.ttl"
    
    # # Load agreement files
    # agreement_files = load_odrl_agreement_kg(odrl_directory)
    # print("Agreement files:")
    # for file_number, filepath in agreement_files:
    #     print(f"{file_number}: {filepath}")
    
    # # Validate agreement files
    # print("\nValidating Agreement Files:")
    # validate_odrl_files(agreement_files, agreement_shapes_path)
    
      
    # # Load offer files
    # offer_files = load_odrl_offer_kg(odrl_directory)
    # print("Offer files:")
    # for file_number, filepath in offer_files:
    #     print(f"{file_number}: {filepath}")
    
    # # Validate offer files
    # print("\nValidating Offer Files:")
    # validate_odrl_files(offer_files, offer_shapes_path)
    
    # Load rule files
    rule_files = load_odrl_rule_kg(odrl_from_template)
    print("Rule files:")
    for file_number, filepath in rule_files:
        print(f"{file_number}: {filepath}")
    
    # Validate rule files
    print("\nValidating Rule Files:")
    validate_odrl_files(rule_files, RULE_SHAPES)