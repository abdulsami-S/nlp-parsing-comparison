import spacy
import stanza

# Load spaCy dependency parser
nlp_spacy = spacy.load("en_core_web_sm")

# Load Stanza constituency parser
nlp_stanza = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."

print("\nSentence:")
print(sentence)

print("\n--- Dependency Parsing (spaCy) ---")
doc = nlp_spacy(sentence)
for token in doc:
    print(f"{token.text:10} --> {token.dep_:10} --> {token.head.text}")

print("\n--- Constituency Parsing (Stanza) ---")
doc_stanza = nlp_stanza(sentence)
for sent in doc_stanza.sentences:
    print(sent.constituency)
