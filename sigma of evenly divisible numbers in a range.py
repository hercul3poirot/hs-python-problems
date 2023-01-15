def relation_to_luke(name):
    relationships = {"Darth Vader":"Luke, I am your father.", "Leia":"Luke, I am your sister.", "Han": "Luke, I am your brother in law.", "R2D2":"Luke, I am your droid."}
    return(relationships[name])

print(relation_to_luke("Darth Vader"))