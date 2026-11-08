from api_tester.specification import load_yaml_file

def main():
    specification = load_yaml_file("example_api/openapi.yaml")
    print(specification)

if __name__ == "__main__":
    main()
