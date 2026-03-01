# NLP Parsing Comparison Project

## 📌 Project Title

**Constituency vs Dependency Parsing Comparison using NLP**

---

## 📖 Overview

This project demonstrates and compares two important syntactic parsing techniques in Natural Language Processing (NLP):

* **Dependency Parsing**
* **Constituency Parsing**

The implementation uses modern NLP libraries to analyze sentence structure and highlight the differences between these two parsing approaches.

---

## 🎯 Objectives

* Understand syntactic parsing in NLP
* Implement two different parsing techniques
* Compare their outputs
* Analyze structural differences in sentence representation

---

## 🧠 Concepts Used

### 🔹 Dependency Parsing

Shows grammatical relationships between words.

Example:

```
fox → subject → jumps
dog → object → over
```

Used in:

* Chatbots
* Search engines
* Question answering systems

---

### 🔹 Constituency Parsing

Breaks sentence into hierarchical phrase structure.

Example:

```
(S
   (NP The quick brown fox)
   (VP jumps over the lazy dog)
)
```

Used in:

* Grammar checking
* Linguistic analysis
* Text structure understanding

---

## 🛠 Technologies Used

* Python
* spaCy
* Stanza (Stanford NLP)
* PyTorch

---

## 📂 Project Structure

```
NLP-Parsing-Comparison
│
├── parser_compare.py
├── .gitignore
└── README.md
```

---

## ▶ How to Run Project

### 1️⃣ Activate Virtual Environment

```
venv\Scripts\activate
```

### 2️⃣ Run Script

```
python parser_compare.py
```

---

## 📊 Sample Output

```
--- Dependency Parsing ---
fox --> nsubj --> jumps

--- Constituency Parsing ---
(ROOT (S (NP ...) (VP ...)))
```

---

## 🔬 Methodology

1. Load spaCy dependency parser
2. Load Stanza constituency parser
3. Input sentence
4. Generate both parse outputs
5. Compare structures

---

## 📈 Comparison Summary

| Feature   | Dependency Parsing | Constituency Parsing |
| --------- | ------------------ | -------------------- |
| Structure | Word relations     | Phrase tree          |
| Speed     | Faster             | Slower               |
| Detail    | Less hierarchical  | Highly structured    |
| Use case  | NLP systems        | Linguistic analysis  |

---

## 🚀 Future Improvements

* Add Universal Dependencies dataset testing
* Evaluate parser accuracy
* Visualize parse trees
* Compare multiple parsers

---

## 👨‍💻 Author

**Abdul Sami**

---

## 📚 References

* spaCy Documentation
* Stanford Stanza NLP
* Universal Dependencies Project

---

⭐ *This project was developed as part of an NLP academic assignment to study syntactic parsing techniques.*
