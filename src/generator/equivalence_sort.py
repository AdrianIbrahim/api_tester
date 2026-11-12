"must implement later for case max < min"



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
        if "minimum" in parameter and "maximum" in parameter:
                x = (parameter.get("minimum") + parameter.get("maximum")) // 2
                y = parameter.get("minimum") -1
                z = parameter.get("maximum") + 1
                response.append({"value": x,"valid": True,"class":"valid_representative"})
                response.append({"value": y,"valid": False,"class":"invalid_representative"})
                response.append({"value": z,"valid": False,"class":"invalid_representative"})
                #only min
        elif "minimum" in parameter and "maximum" not in parameter:
                    x = parameter.get("minimum") + 1
                    y = parameter.get("minimum") - 1
                    response.append({"value": x,"valid": True,"class":"valid_representative"})
                    response.append({"value": y,"valid": False,"class":"invalid_representative"})
                    #only max
        elif "minimum" not in parameter and "maximum" in parameter:
                    x = parameter.get("maximum") - 1
                    z = parameter.get("maximum") + 1
                    response.append({"value": x,"valid": True,"class":"valid_representative"})
                    response.append({"value": z,"valid": False,"class":"invalid_representative"})
        else:
                    response.append({"value": 5,"valid": True,"class":"valid_representative"})
        return response
    return []

def generate_string_classes(parameter):
    response = [{"value": 123,"valid": False,"class":"integer"},
                {"value": 1.5,"valid": False,"class":"float"},
                {"value": True,"valid": False,"class":"boolean"}]
    if parameter.get("type") == "string":
        if "minLength" in parameter and "maxLength" in parameter:
                   if parameter.get("maxLength") == 0 and parameter.get("minLength") == 0:
                       response.append({"value": "","valid": True,"class":"valid_representative"})
                       response.append({"value": "a","valid": False,"class":"invalid_representative"})
                   elif parameter.get("minLength") == 0 and parameter.get("maxLength") > 0:
                       x = "a" * (parameter.get("maxLength") // 2)
                       response.append({"value": x,"valid": True,"class":"valid_representative"})
                       response.append({"value": "","valid": True,"class":"valid_representative"})
                       response.append({"value": "a" * (parameter.get("maxLength") + 1),"valid": False,"class":"invalid_representative"})
                   elif parameter.get("minLength") <= parameter.get("maxLength"):
                       x = "a" * ((parameter.get("minLength") + parameter.get("maxLength")) // 2)
                       y = "a" * (parameter.get("minLength") - 1)
                       z = "a" * (parameter.get("maxLength") + 1)
                       response.append({"value": x,"valid": True,"class":"valid_representative"})
                       response.append({"value": y,"valid": False,"class":"invalid_representative"})
                       response.append({"value": z,"valid": False,"class":"invalid_representative"})
                       #only min
        elif "minLength" in parameter and "maxLength" not in parameter:
                           if parameter.get("minLength") == 0:
                               response.append({"value": "","valid": True,"class":"valid_representative"})
                               response.append({"value": "a","valid": True,"class":"valid_representative"})
                           else:
                               x = "a" * (parameter.get("minLength") + 1)
                               y = "a" * (parameter.get("minLength") - 1)
                               response.append({"value": y,"valid": False,"class":"invalid_representative"})
                               response.append({"value": x,"valid": True,"class":"valid_representative"})
                           #only max
        elif "minLength" not in parameter and "maxLength" in parameter:
                           if parameter.get("maxLength") == 0:
                               response.append({"value": "","valid": True,"class":"valid_representative"})
                               response.append({"value": "a","valid": False,"class":"invalid_representative"})
                           else:      
                             z = "a" * (parameter.get("maxLength") + 1)
                             x = "a" *(parameter.get("maxLength") - 1)
                             response.append({"value": x,"valid": True,"class":"valid_representative"})
                             response.append({"value": z,"valid": False,"class":"invalid_representative"})
        else:
                           response.append({"value": "abcdef","valid": True,"class":"valid_representative"})
        return response
    return []
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
    return []


