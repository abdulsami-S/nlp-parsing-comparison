"""
parser_compare.py

This script performs a comparative analysis between Dependency Parsing (spaCy) 
and Constituency Parsing (Stanza) to demonstrate the trade-offs between 
processing speed and structural depth.
"""

import spacy
import stanza
import time
import os
import random
import matplotlib.pyplot as plt

# =====================================================================
# GLOBAL CONFIGURATION & MAPPINGS
# =====================================================================

# TAG_MAP translates complex linguistic acronyms (like NP or VBG) 
# into human-readable phrases for clear presentation output.
TAG_MAP = {
    "ROOT": "Root", "S": "Sentence", "NP": "Noun Phrase", "VP": "Verb Phrase",
    "PP": "Prepositional Phrase", "ADVP": "Adverb Phrase", "ADJP": "Adjective Phrase",
    "SBAR": "Subordinate Clause", "WHNP": "Wh-Noun Phrase", "WHADVP": "Wh-Adverb Phrase",
    "WHPP": "Wh-Prepositional Phrase", "PRT": "Particle Phrase", "INTJ": "Interjection",
    "FRAG": "Fragment", "NN": "Noun", "NNS": "Noun (Plural)", "NNP": "Proper Noun",
    "NNPS": "Proper Noun (Plural)", "DT": "Determiner", "JJ": "Adjective",
    "JJR": "Adjective (Comparative)", "JJS": "Adjective (Superlative)", "VB": "Verb",
    "VBD": "Verb (Past)", "VBG": "Verb (Gerund)", "VBN": "Verb (Past Participle)",
    "VBP": "Verb (Present)", "VBZ": "Verb (Present)", "IN": "Preposition",
    "PRP": "Pronoun", "PRP$": "Possessive Pronoun", "RB": "Adverb",
    "RBR": "Adverb (Comparative)", "RBS": "Adverb (Superlative)", "MD": "Modal",
    "CC": "Conjunction", "CD": "Number", "UH": "Interjection", "TO": "To",
    "WDT": "Wh-Determiner", "WP": "Wh-Pronoun", "WP$": "Possessive Wh-Pronoun",
    "WRB": "Wh-Adverb", "EX": "Existential There", "POS": "Possessive Ending",
    "RP": "Particle", "SYM": "Symbol"
}

# =====================================================================
# CORE FUNCTIONS
# =====================================================================

def print_flattened_constituency(node, parent_label="ROOT"):
    """
    Recursively flattens Stanza's complex NLTK-style Tree object into a readable 
    3-column text format (Word -> Phrase Type -> Parent Phrase).
    This allows a direct side-by-side comparison with spaCy's 3-column output.
    """
    if node.is_preterminal():
        word = node.children[0].label
        tag = node.label
        
        readable_tag = TAG_MAP.get(tag, tag)
        readable_parent = TAG_MAP.get(parent_label, parent_label)
        
        print(f"{word:<12} -> {readable_tag:<22} -> {readable_parent}")
        return
        
    for child in node.children:
        print_flattened_constituency(child, node.label)


def read_conllu_sentences(file_path, limit=5):
    """
    Parses a CoNLL-U dataset file to extract the raw English sentences.
    Returns a list of randomly sampled sentences to guarantee an unbiased speed test.
    """
    all_sentences = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # We specifically target lines containing the raw text
            if line.startswith("# text ="):
                sentence = line.replace("# text =", "").strip()
                all_sentences.append(sentence)

    return random.sample(all_sentences, limit)


def compare_parsers(nlp_spacy, nlp_stanza, sentence):
    """
    Takes a single sentence and feeds it through both parsed models (spaCy and Stanza).
    Measures the exact computation time each model takes and prints their structural output.
    
    Returns:
        spacy_time (float): The time taken by spaCy in seconds.
        stanza_time (float): The time taken by Stanza in seconds.
    """
    print("\n" + "="*60)
    print("Sentence:")
    print(sentence)

    # ---------- Benchmark spaCy (Dependency Parsing) ----------
    start = time.time()
    doc = nlp_spacy(sentence)
    spacy_time = time.time() - start

    print("\n--- Dependency Parsing (spaCy) ---")
    for token in doc:
        print(f"{token.text:<12} -> {token.dep_:<12} -> {token.head.text}")
    print(f"\nspaCy parsing time: {spacy_time:.4f} sec")


    # ---------- Benchmark Stanza (Constituency Parsing) ----------
    start = time.time()
    doc2 = nlp_stanza(sentence)
    stanza_time = time.time() - start

    print("\n--- Constituency Parsing (Stanza) ---")
    try:
        # Pass the tree to our custom formatter
        print_flattened_constituency(doc2.sentences[0].constituency)
    except:
        print("Could not generate constituency tree")
    print(f"\nStanza parsing time: {stanza_time:.4f} sec")

    return spacy_time, stanza_time


def plot_performance_comparison(sentences, spacy_times, stanza_times):
    """
    Generates a 3x2 grid of subplots visualizing the parsing speeds.
    Creates 5 individual sentence comparisons and 1 total aggregate comparison.
    This gives the presentation a highly professional, academic aesthetic.
    """
    print("\nDisplaying performance graph...")
    
    total_spacy_time = sum(spacy_times)
    total_stanza_time = sum(stanza_times)
    
    # Initialize a 3x2 grid of subplots
    fig, axes = plt.subplots(3, 2, figsize=(10, 7))
    axes = axes.flatten()
    
    # Render the 5 Individual Sentence Plots
    for i in range(len(sentences)):
        ax = axes[i]
        times = [spacy_times[i], stanza_times[i]]
        bars = ax.bar(['spaCy', 'Stanza'], times, color='#1f77b4', width=0.4)  
        ax.set_title(f"Sentence {i+1}", fontsize=12)
        
        # Add 15% headroom to the y-axis so text doesn't overlap the top frame
        ax.set_ylim(0, max(times) * 1.15)
        
        # Add exact values Floating on top of bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + (max(times)*0.01), f"{yval:.4f}", ha='center', va='bottom', fontsize=10)
            
    # Render Subplot 6: Total Aggregate Time
    ax = axes[5]
    times_total = [total_spacy_time, total_stanza_time]
    bars = ax.bar(['spaCy', 'Stanza'], times_total, color='#1f77b4', width=0.4)
    ax.set_title("Total Time", fontsize=12)
    
    # Add 15% headroom to prevent overlap
    ax.set_ylim(0, max(times_total) * 1.15)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + (max(times_total)*0.01), f"{yval:.4f}", ha='center', va='bottom', fontsize=10)
        
    plt.tight_layout()
    plt.show()

# =====================================================================
# MAIN EXECUTION SEQUENCE
# =====================================================================

def main():
    """
    The central coordinator block. Loads models, reads data, runs the engine, 
    and handles graphing output.
    """
    # 1. Load the AI Models into memory
    print("Loading spaCy model...")
    nlp_spacy = spacy.load("en_core_web_sm")

    print("Loading Stanza model...")
    stanza.download("en", processors="tokenize,pos,constituency", verbose=False)
    nlp_stanza = stanza.Pipeline(
        lang="en",
        processors="tokenize,pos,constituency",
        verbose=False
    )
    
    # 2. Check and Load Dataset
    dataset_path = "UD_English-EWT/en_ewt-ud-test.conllu"

    if not os.path.exists(dataset_path):
        print(f"\nError: Dataset file not found at '{dataset_path}'")
        return

    print("\nLoading sentences from dataset...")
    sentences = read_conllu_sentences(dataset_path, limit=5)
    print(f"Successfully loaded {len(sentences)} test sentences.")

    # 3. Process Sentences & Track Speeds
    spacy_times = []
    stanza_times = []

    for s in sentences:
        sp_time, st_time = compare_parsers(nlp_spacy, nlp_stanza, s)
        spacy_times.append(sp_time)
        stanza_times.append(st_time)

    print("\nAll sentences parsed successfully.")
    
    # 4. Generate Graphical Output
    plot_performance_comparison(sentences, spacy_times, stanza_times)


if __name__ == "__main__":
    main()