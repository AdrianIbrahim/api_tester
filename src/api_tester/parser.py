def extract_info(specification: dict) -> dict:
    """
        Extracts relevant information from the OpenAPI specification.
    """
    operations =[]

    for path, path_item in specification.get("paths", {}).items():
        for method, details in path_item.items():
              if method.lower() not in ["get", "post", "put", "delete", "patch","trace", "head", "options","connect","query"]:
                continue
              operations.append({
                  "path": path,
                  "method": method.upper(),
                    "summary": details.get("summary", ""),
                    "parameters": details.get("parameters", []),
                    "requestBody": details.get("requestBody", {}),
                    "responses": details.get("responses", {})
                })
    return operations