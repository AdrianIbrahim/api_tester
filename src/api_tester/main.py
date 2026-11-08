from specification import load_yaml_file
from parser import extract_info

def main():
    specification = load_yaml_file("example_api/openapi.yaml")
    extracted_info = extract_info(specification)
    print(extracted_info)
if __name__ == "__main__":
    main()

specification = load_yaml_file("example_api/openapi.yaml")

