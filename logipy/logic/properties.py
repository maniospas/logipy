class LogipyPropertyException(Exception):
    def __init__(self, message):
        super().__init__(message)


def empty_properties():
    return set()


def combine(property_set1, property_set2):
    for property in property_set2:
        property_set1.add(property)


def has_property(property_set, property):
    positive = True
    if property.startswith("NOT "):
        property = property[4:]
        positive = False
    if property == "TRUE":
        return True
    if property == "FALSE":
        return False
    return (property in property_set) == positive


def add_property(property_set, given_rules, properties):
    if given_rules is not None:
        for rule in given_rules.split(" AND "):
            if not has_property(property_set, rule):
                return
    for property in properties.split(" AND "):
        if property.startswith("SHOULD "):
            if not has_property(property_set, property[len("SHOULD "):]):
                raise LogipyPropertyException(property)
        elif property.startswith("NOT "):
            if property[4:] in property_set:
                property_set.remove(property[4:])
        elif property.startswith("ERROR"):
            raise LogipyPropertyException(property[5:])
        elif property.startswith("PRINT"):
            print(property[5:])
        else:
            property_set.add(property)