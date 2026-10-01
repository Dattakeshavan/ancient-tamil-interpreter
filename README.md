# 📜 Ancient Tamil Interpreter

A lightweight, explainable system for interpreting classical Tamil text and presenting contextual English interpretations.

The project combines curated classical Tamil interpretations, Tamil-to-English fallback translation, domain-specific vocabulary, heuristic word importance, and structured attention-style visualization through a Streamlit interface.

> **Note:** This is a research/engineering prototype. It is not a dedicated trained Ancient Tamil translation model, and its explainability scores and confidence estimates are heuristic.

---

## ✨ Features

* 📜 Ancient Tamil text normalization
* 🌐 Tamil → English translation
* 📚 Curated interpretations for selected classical Tamil verses
* 🔤 Ancient Tamil domain lexicon
* 🧠 Heuristic word-importance analysis
* 📊 Structured attention visualization
* 📈 Heuristic interpretation-confidence estimate
* 🖥️ Streamlit web interface
* 💻 Command-line interface
* 📝 Methodology documentation

---

## 🏗️ Architecture

```text
                         Ancient Tamil Input
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │   Text Normalization    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Translation Pipeline  │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
          ┌──────────────────┐      ┌──────────────────┐
          │ Curated Classical│      │ Fallback Tamil → │
          │ Interpretations  │      │ English          │
          └────────┬─────────┘      └────────┬─────────┘
                   │                         │
                   └────────────┬────────────┘
                                ▼
                       English Interpretation
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
       Domain Lexicon    Word Importance    Visualization
              │                 │                 │
              ▼                 ▼                 ▼
       Literal Insight    Heuristic Scores   Attention Map
```

---

## 📁 Project Structure

```text
ancient-tamil-interpreter/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── app.py
├── run.py
│
├── src/
│   ├── __init__.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── inference_pipeline.py
│   │
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── ancient_normalizer.py
│   │   └── domain_lexicon.py
│   │
│   ├── translation/
│   │   ├── __init__.py
│   │   └── indictrans_model.py
│   │
│   └── explainability/
│       ├── __init__.py
│       ├── attention.py
│       ├── visualization.py
│       └── word_importance.py
│
├── docs/
│   └── methodology.md
│
└── outputs/
    └── attention_maps/
        └── .gitkeep
```

---

## ⚙️ Requirements

* Python 3.10+
* Internet connection for fallback translation
* pip

The project currently uses:

```text
streamlit
regex
deep-translator
numpy
matplotlib
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ancient-tamil-interpreter.git
cd ancient-tamil-interpreter
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application provides:

1. Ancient Tamil text input
2. English interpretation
3. Contextual interpretation
4. Literal/domain insight
5. Refined interpretation
6. Cultural context
7. Word-importance scores
8. Structured attention visualization
9. Heuristic confidence estimate

---

## 💻 Command-Line Usage

The project can also be used without Streamlit.

```bash
python run.py --text "யாதும் ஊரே யாவரும் கேளிர்"
```

Example output:

```text
Ancient Tamil Interpretation
------------------------------
Every place is my town, and all people are my kin.
```

Another example:

```bash
python run.py --text "கற்றது கைமண் அளவு கல்லாதது உலகளவு"
```

---

## 📜 Example Classical Tamil Expressions

The current implementation contains curated interpretations for selected expressions.

### யாதும் ஊரே யாவரும் கேளிர்

```text
Every place is my town, and all people are my kin.
```

### கற்றது கைமண் அளவு கல்லாதது உலகளவு

```text
What we have learned is a handful; what we have not learned is as vast as the world.
```

### அகர முதல எழுத்தெல்லாம் ஆதி பகவன் முதற்றே உலகு

```text
As the letter 'A' is the first of all letters, God is the first in the world.
```

### தீதும் நன்றும் பிறர் தர வாரா

```text
Good and evil do not come from others; they arise from one's own actions.
```

---

## 🧠 Explainability

The project contains multiple lightweight explainability components.

### Domain Lexicon

Selected Tamil words are associated with contextual English meanings.

For example:

```text
யாதும் → every
ஊரே → place
யாவரும் → everyone
கேளிர் → kin
```

These annotations are used separately from the translation input.

### Word Importance

Word importance is calculated using a heuristic based primarily on:

* Word length
* Presence of selected domain concepts

It is **not** a model-derived semantic attribution score.

### Attention Visualization

The application produces a structured attention-style heatmap based on source and target token positions.

It is important to note that this is a **visualization proxy**, not actual transformer attention.

---

## 📊 Confidence Estimate

The application displays an interpretation-confidence estimate.

The current implementation uses a simple heuristic based on:

* A default confidence value
* Uncertainty indicators in the interpretation
* Input length

The value is **not a calibrated probability** and should not be interpreted as the probability that an interpretation is correct.

---

## 🌐 Translation Backend

The fallback translation component uses:

```python
GoogleTranslator(
    source="ta",
    target="en"
)
```

through the `deep-translator` package.

Therefore, fallback translation requires network access.

Curated classical Tamil expressions are handled locally.

---

## ⚠️ Limitations

This project is a prototype and has several limitations:

* It does not currently contain a dedicated trained Ancient Tamil translation model.
* Curated interpretations are limited to predefined expressions.
* Fallback translation depends on an external translation service.
* Word importance is heuristic.
* Attention visualization is structured/simulated rather than extracted from a trained transformer.
* Confidence estimation is heuristic rather than calibrated.
* Complex classical poetry may require specialist linguistic and cultural analysis.
* Translation quality may vary for uncommon vocabulary, poetic constructions, and context-dependent expressions.

---

## 🔬 Methodology

A detailed description of the processing architecture and methodology is available in:

```text
docs/methodology.md
```

---

## 🔮 Future Work

Potential future improvements include:

* Dedicated Ancient Tamil translation models
* Larger classical Tamil vocabulary resources
* Morphological analysis
* Sangam literature support
* Real transformer attention extraction
* Model-based token attribution
* Retrieval-augmented cultural context
* Curated classical Tamil datasets
* Expert-annotated evaluation datasets
* Quantitative translation evaluation
* Multilingual interpretation support

---

## 📄 License

This project is released under the MIT License.

See:

```text
LICENSE
```

---

## 👨‍💻 Author

**Sarath B Raam**

Artificial Intelligence and Machine Learning
SRM Institute of Science and Technology, Ramapuram

---

## ⚠️ Disclaimer

This project is intended for educational, research, and experimental purposes.

Ancient Tamil interpretation can depend heavily on historical context, grammar, literary tradition, and cultural references. The outputs of this prototype should therefore not be treated as authoritative scholarly translations.
