import spacy
ner = spacy.load("it_core_news_sm")

testo = ner("I marchi automobilistici Italiani tra cui: Ferrarri, Fiat e Alfa Romeo, sono i più acclamati in europa")
for ent in testo.ents:
    print(ent.text, ent.label_)
