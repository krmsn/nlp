import spacy

nlp = spacy.load("en_core_web_sm")

document = nlp("In 1994, Tim Berners-Lee founded the World Wide Web \n Consortium (W3C), devoted to developing web technologies.")

for entity in document.ents:
    print(entity.text, ":", entity.label_)
