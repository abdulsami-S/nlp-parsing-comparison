import spacy
import stanza
import time
import os
import random

# -------------------------
# LOAD MODELS
# -------------------------

print("Loading spaCy model...")
nlp_spacy = spacy.load("en_core_web_sm")

print("Loading Stanza model...")
stanza.download("en", processors="tokenize,pos,constituency", verbose=False)
nlp_stanza = stanza.Pipeline(
    lang="en",
    processors="tokenize,pos,constituency",
    verbose=False
)

# -------------------------
# READ SENTENCES FROM DATASET
# -------------------------

def read_conllu_sentences(file_path, limit=5):
    all_sentences = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("# text ="):
                sentence = line.replace("# text =", "").strip()
                all_sentences.append(sentence)

    # Select random sentences
    return random.sample(all_sentences, limit)


# -------------------------
# PARSER COMPARISON FUNCTION
# -------------------------

def compare_parsers(sentence):
    print("\n" + "="*60)
    print("Sentence:")
    print(sentence)

    # ---------- spaCy ----------
    start = time.time()
    doc = nlp_spacy(sentence)
    spacy_time = time.time() - start

    print("\n--- Dependency Parsing (spaCy) ---")
    for token in doc:
        print(f"{token.text:<12} → {token.dep_:<12} → {token.head.text}")

    print(f"\nspaCy parsing time: {spacy_time:.4f} sec")

    # ---------- Stanza ----------
    start = time.time()
    doc2 = nlp_stanza(sentence)
    stanza_time = time.time() - start

    print("\n--- Constituency Parsing (Stanza) ---")
    try:
        print(doc2.sentences[0].constituency)
    except:
        print("Could not generate constituency tree")

    print(f"\nStanza parsing time: {stanza_time:.4f} sec")


# -------------------------
# MAIN EXECUTION
# -------------------------

if __name__ == "__main__":

    dataset_path = "UD_English-EWT/en_ewt-ud-test.conllu"

    if not os.path.exists(dataset_path):
        print("\nDataset file not found!")
        print("Expected path:", dataset_path)
        exit()

    print("\nLoading sentences from dataset...")
    sentences = read_conllu_sentences(dataset_path, limit=5)

    print(f"Loaded {len(sentences)} sentences")

    for s in sentences:
        compare_parsers(s)

    print("\nDone.")