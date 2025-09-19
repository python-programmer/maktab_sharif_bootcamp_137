person = {
    "name": "hadi"
}

def set_person(person_var):
    assert isinstance(person_var, dict)
    # "gas_capacity" in person, in this case, I mean dict, this operation search in keys
    if "gas_capacity" in person_var:
        raise ValueError("You can't set gas_capacity for a person type")

    for prop in person_var:
        person[prop] = person_var[prop]
