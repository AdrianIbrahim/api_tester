"must implement later for case max < min"

import abc


def generate_classes(parameter):
    if parameter.get("type") == "integer":
        return generate_integer_classes(parameter)

    elif parameter.get("type") == "string":
        return generate_string_classes(parameter)

    elif parameter.get("type") == "boolean":
        return generate_boolean_classes(parameter)

    return []

def generate_integer_classes(parameter):
    response = [{"value": "abc","valid": False,"class":"string"},
                {"value": 1.5,"valid": False,"class":"float"},
                {"value": True,"valid": False,"class":"boolean"}]
    if parameter.get("type") =="integer":
        if "minimum" in parameter:
            response.append({"value": parameter.get("minimum"),"valid": True,"class":"minimum"})
            response.append({"value": parameter.get("minimum") - 1,"valid": False,"class":"below_minimum"})

        if "maximum" in parameter:
          response.append({"value": parameter.get("maximum"),"valid": True,"class":"maximum"})
          response.append({"value": parameter.get("maximum") + 1,"valid": False,"class":"above_maximum"})

        if "minimum" in parameter or "maximum" in parameter:
             if (
        ("minimum" not in parameter or parameter["minimum"] <= 5)
        and
        ("maximum" not in parameter or parameter["maximum"] >= 5)
    ):
                 response.append({"value": 5,"valid": True,"class":"between_minimum_maximum"})
        else :
                 response.append({"value": 5,"valid": False,"class":"between_minimum_maximum"})
        return response

    

def generate_string_classes(parameter):
    response = [{"value": 123,"valid": False,"class":"integer"},
                {"value": 1.5,"valid": False,"class":"float"},
                {"value": True,"valid": False,"class":"boolean"},
                {"value": "abc","valid": True,"class":"string"}]
    if parameter.get("type") == "string":
        if "minLength" in parameter:
            response.append({"value": "a" * parameter.get("minLength"),"valid": True,"class":"minLength"})
            response.append({"value": "a" * (parameter.get("minLength") - 1),"valid": False,"class":"below_minLength"})
        if "maxLength" in parameter:
            response.append({"value": "a" * parameter.get("maxLength"),"valid": True,"class":"maxLength"})
            response.append({"value": "a" * (parameter.get("maxLength") + 1),"valid": False,"class":"above_maxLength"})
        if "minLength" in parameter or "maxLength" in parameter:
                if (
                ("minLength" not in parameter or parameter["minLength"] <= 5)
                and
                ("maxLength" not in parameter or parameter["maxLength"] >= 5)
            ):
                 response.append({"value": "abcde","valid": True,"class":"between_minlength_maxlength"})
        else :
                 response.append({"value": "abcde","valid": False,"class":"between_minlength_maxlength"})
        return response

def generate_boolean_classes(parameter):
    if parameter.get("type") == "boolean":
     response = [{"value": 123,"valid": False,"class":"integer"},
                {"value": 1.5,"valid": False,"class":"float"},
                {"value": "abc","valid": False,"class":"string"},
                {"value": True,"valid": True,"class":"true"},
                {"value": False,"valid": True,"class":"false"},
                {"value": "True","valid": False,"class":"true"},
                {"value": "False","valid": False,"class":"false"}]
    return response


