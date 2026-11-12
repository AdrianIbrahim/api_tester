from generator.equivalence_sort import generate_classes
def test_integer_boundaries():
    parameter = {
        "type": "integer",
        "minimum": 5,
        "maximum": 10
    }

    result = generate_classes(parameter)

    assert any(x["value"] == 7 and x["valid"] for x in result)
    assert any(x["value"] == 4 and not x["valid"] for x in result)
    assert any(x["value"] == 11 and not x["valid"] for x in result)
    assert any(x["value"] == 5 and x["valid"] for x in result)
    assert any(x["value"] == "10" and x["valid"] for x in result)