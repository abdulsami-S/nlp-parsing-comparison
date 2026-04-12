# 🧠 Syntactic Parsing Benchmarker: Dependency vs. Constituency

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?logo=spacy&logoColor=white)
![Stanza](https://img.shields.io/badge/Stanza-Stanford-B1040E)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)

## 📌 Executive Summary

This repository hosts a high-performance NLP benchmarking tool engineered to evaluate the architectural differences, structural trade-offs, and processing speeds between **Dependency Parsing** and **Constituency Parsing**. 

By natively pulling sample data from real-world `CoNLL-U` linguistic datasets and running them concurrently through modern production pipelines (`spaCy`) and deep-academic pipelines (`Stanford Stanza`), the script provides empirical data outlining the balance between execution speed and hierarchical depth.

---

## 📖 A-to-Z How It Works (Code Breakdown for New Users)

The `parser_compare.py` script is designed to be fully modular and process data through 4 primary phases:

1. **Configuration & `TAG_MAP` Definition**:
   At the top of the file, we import the standard libraries (`spacy`, `stanza`, `matplotlib`). We define a global `TAG_MAP` dictionary. Many parsers output complex syntactic acronyms like `SBAR` (Subordinate Clause) or `VBG` (Verb Gerund). The `TAG_MAP` automatically intercepts and translates these into plain English, ensuring final output is human-readable.

2. **Dataset Ingestion (`read_conllu_sentences`)**:
   Standard NLP benchmark datasets come in CoNLL-U formatting (which contains a lot of metadata). The script safely opens `UD_English-EWT/en_ewt-ud-test.conllu`, ignores the complex metadata, extracts only the raw `# text = ` lines, and randomly samples exactly 5 sentences. **Why random?** This ensures we benchmark system processing speeds unbiasedly on fresh data each run.

3. **Core Benchmarking Engine (`compare_parsers`)**:
   This loop forms the heart of the project. A sampled sentence is passed individually to:
   * **spaCy (Dependency)**: The script marks a start timestamp, processes the sentence into direct word-to-word relationships (shallow but fast), marks an end timestamp, and prints the result.
   * **Stanza (Constituency)**: Repeating the exact same process, the sentence is fed into Stanza to construct a deep structural recursion tree. The custom `print_flattened_constituency` algorithm kicks in to untangle and normalize Stanza's nested matrix, aligning its visual aesthetic to match spaCy.

4. **Visual Metrics Aggregation (`plot_performance_comparison`)**:
   Once computational bounds for all 5 sentences are captured, the engine launches `Matplotlib`. It mathematically aggregates execution speeds array-by-array and deploys a clean 3x2 graphing matrix mapping the precise fraction-of-a-second cost differential.

---

## 🎯 Key Capabilities

- **Unbiased Comparative Benchmarking:** Ingests the `UD_English-EWT` dataset natively, randomizing sentence sampling to ensure unbiased speed tests.
- **Output Normalization:** Flattens Stanza's deeply nested, algorithmic constituency NLTK-trees into a normalized, 3-column read format to allow for direct 1-to-1 visual comparison with spaCy’s planar maps.
- **Acronym Translation:** Utilizes a custom structural `TAG_MAP` to automatically translate rigid linguistic taxonomy (e.g., `VP`, `SBAR`) into plain English.
- **Empirical Visualizations:** Features a dynamic Matplotlib visualization integration that automatically generates a 3x2 graphing sequence to cleanly visualize processing speeds and calculate the cost of latency vs. structural accuracy.

---

## 🔬 Architectural Comparison

### 🔹 Dependency Parsing (Powered by `spaCy`)
Dependency parsing strictly models grammatical relationships linearly, assigning "head-word" relationships. 
* **Profile:** Lightweight, shallow structure.
* **Advantage:** Production-grade execution speed.
* **Use Cases:** Search indexing, live user-input validation, chatbot entity extraction.

### 🔹 Constituency Parsing (Powered by `Stanza`)
Constituency parsing focuses on deep morphological derivation, analyzing how smaller word clusters nest recursively inside larger phrase hierarchies (like Russian nesting dolls).
* **Profile:** Deep, highly nested tree structures.
* **Advantage:** Maximum structural context and linguistic modeling.
* **Use Cases:** Automated grammar checking, academic translation mapping, semantic syntax analysis.

---

## 📂 Project Structure

```text
NLP-Parsing-Comparison/
├── UD_English-EWT/         # Core CoNLL-U syntactic dataset containing test sentences
├── venv/                   # Isolated Python virtual environment
├── parser_compare.py       # Main parser evaluation engine
├── Code_Walkthrough.md     # Step-by-step academic presentation guide
└── README.md               # Overview and execution documentation
```

---

## 🚀 Installation & Execution Guide (A-Z)

Follow these steps to fully configure and run the engine from scratch.

### 1️⃣ Virtual Environment and Dependencies
Because AI modules (`spaCy` and `Stanza`) are computationally heavy and have strict dependencies, they must run inside the virtual repository.

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

*Required pip packages if setting up on a fresh machine:*
`pip install spacy stanza matplotlib`
`python -m spacy download en_core_web_sm`

### 2️⃣ Run Benchmarker
Execute the core Python engine. The script will automatically load the NLP models, parse the linguistic dataset, benchmark the performance, output textual mapping logs to the terminal, and physically render the visualization UI.

```bash
python parser_compare.py
```

---

## 📊 Evaluation Output

The system's terminal output structurally maps the parsing differences intuitively for academic review:

```text
--- Dependency Parsing (spaCy) ---
Word         -> Dependency   -> Head Word
-----------------------------------------
fox          -> nsubj        -> jumps

--- Constituency Parsing (Stanza) ---
Word         -> Classification -> Parent Phrase
-----------------------------------------
fox          -> Noun           -> Noun Phrase
```
> *Additionally, executing the engine launches a comprehensive `Matplotlib` graphical UI showcasing execution times per sentence and macro-aggregates.*

---

## 👨‍💻 Author

**Abdul Sami**  
*Developed as part of a comprehensive NLP academic evaluation targeting the architectural limitations and performance capabilities of modern syntactic parsing techniques.*
