# Ancient Tamil Interpreter — Methodology

## 1. Overview

The Ancient Tamil Interpreter is a lightweight system for interpreting classical Tamil text and presenting the result in English.

The system combines:

* Ancient Tamil text normalization
* Domain-specific Tamil vocabulary
* Curated interpretations of selected classical verses
* Tamil-to-English fallback translation
* Heuristic word-importance estimation
* Structured attention-style visualization
* A Streamlit-based user interface
* A command-line interface

The project is designed as an interpretable prototype rather than a fully trained end-to-end neural translation model.

---

## 2. System Architecture

The processing flow is divided into several components:

```text
Ancient Tamil Input
        │
        ▼
┌─────────────────────────┐
│ Ancient Tamil           │
│ Normalizer              │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Translation Pipeline    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Indic Translator        │
│                         │
│ 1. Curated phrases      │
│ 2. Fallback translator  │
└────────────┬────────────┘
             │
             ▼
      English Interpretation
```

The explainability components operate separately:

```text
Normalized Tamil
       │
       ├──────────────► Domain Lexicon
       │                      │
       │                      ▼
       │                Literal Insight
       │
       ├──────────────► Word Importance
       │                      │
       │                      ▼
       │                Importance Scores
       │
       └──────────────► Attention Visualizer
                              │
                              ▼
                    Structured Attention Map
```

---

## 3. Text Normalization

The `AncientTamilNormalizer` prepares the input before translation.

The normalization process includes:

1. Collapsing repeated whitespace.
2. Removing selected punctuation.
3. Applying predefined character replacements.
4. Removing leading and trailing whitespace.

Example replacements include:

```text
ஜ்ஞ → ஞ
ஸ்ரீ → ஸ்ரி
```

The goal is to provide a more consistent input representation for subsequent processing.

---

## 4. Domain Lexicon

The `DomainLexicon` contains selected Ancient Tamil terms with English contextual meanings.

Examples include:

| Tamil term | Contextual meaning   |
| ---------- | -------------------- |
| யாதும்     | every                |
| ஊரே        | place                |
| யாவரும்    | everyone             |
| கேளிர்     | kin                  |
| கற்றது     | learned              |
| கல்லாதது   | not learned          |
| உலகளவு     | as vast as the world |
| பகவன்      | divine being         |

The lexicon is used for contextual explanation rather than being inserted directly into the translation input.

This separation prevents the English annotations from interfering with curated phrase matching.

---

## 5. Translation

The translation component uses two levels of processing.

### 5.1 Curated Classical Interpretations

Several well-known classical Tamil expressions have predefined English interpretations.

For these phrases, the system returns the curated interpretation directly.

Examples include:

```text
யாதும் ஊரே யாவரும் கேளிர்
```

and

```text
கற்றது கைமண் அளவு கல்லாதது உலகளவு
```

This provides stable outputs for the phrases explicitly included in the project.

### 5.2 Fallback Translation

For text that does not match a curated phrase, the system uses `deep-translator` with Tamil-to-English translation.

The resulting text is then passed through lightweight post-processing and philosophical refinement rules.

---

## 6. Philosophical Refinement

The translator contains simple rule-based refinement for certain themes.

For example, translations containing concepts associated with:

* knowledge
* learning
* good and bad
* truth
* lies

may be converted into a higher-level philosophical interpretation.

These refinements are rule-based and should not be interpreted as outputs from a trained semantic reasoning model.

---

## 7. Word Importance

The `WordImportance` component produces a heuristic importance score for each Tamil word.

The score is primarily based on:

```text
Word length
+
Selected domain-concept boost
```

Selected concepts include terms related to:

```text
நன்று
தீது
அறிவு
உலக
கற்று
```

The score is normalized to a maximum of `1.0`.

### Important limitation

These scores are **heuristic indicators**, not model-derived semantic attribution scores.

They should therefore be interpreted as an explanatory visualization rather than a mathematically calibrated measure of linguistic importance.

---

## 8. Attention Visualization

The project includes an attention-style visualization for connecting source and target tokens.

The current implementation generates a structured matrix using relative token positions.

The matrix:

1. Calculates source-target positional distance.
2. Assigns higher values to closer positions.
3. Adds a small amount of random noise.
4. Normalizes the resulting matrix.
5. Displays it as a heatmap.

### Important limitation

This is a **structured attention visualization**, not attention extracted from a trained transformer model.

The project therefore does not claim that the displayed heatmap represents actual neural attention weights.

The architecture retains an `AttentionExtractor` utility for future integration with a transformer-based model that exposes decoder attention.

---

## 9. Confidence Estimate

The Streamlit interface displays a confidence estimate.

The current confidence value is a simple heuristic based on:

* A default confidence value.
* Whether the translation indicates uncertainty.
* The approximate length of the input.

It is bounded within a predefined range.

### Important limitation

This is **not a calibrated probability** and should not be interpreted as the statistical probability that an interpretation is correct.

---

## 10. User Interfaces

The project provides two interfaces.

### Streamlit Interface

Run:

```bash
streamlit run app.py
```

The interface provides:

* Tamil text input
* English interpretation
* Contextual interpretation
* Literal/domain insight
* Refined interpretation
* Cultural context
* Word-importance visualization
* Structured attention visualization
* Heuristic confidence estimate

### Command-Line Interface

Run:

```bash
python run.py --text "யாதும் ஊரே யாவரும் கேளிர்"
```

The CLI returns the English interpretation directly in the terminal.

---

## 11. External Dependency

The fallback translation component uses `deep-translator`.

Therefore, fallback translation requires network access to the underlying translation service.

Curated phrase interpretations do not depend on the fallback translation service.

---

## 12. Limitations

The current prototype has several limitations:

1. It does not contain a dedicated trained Ancient Tamil translation model.
2. Curated interpretations are limited to predefined phrases.
3. Fallback translation depends on an external translation service.
4. Word importance is heuristic.
5. The attention visualization is simulated/structured rather than model-derived.
6. Confidence is heuristic rather than calibrated.
7. Highly complex classical poetry may require specialist linguistic and cultural analysis.
8. Translation quality may vary for uncommon vocabulary, poetic constructions, historical language forms, and context-dependent expressions.

---

## 13. Future Development

Potential future improvements include:

* Training or integrating a dedicated classical Tamil translation model.
* Adding a larger Ancient Tamil domain lexicon.
* Integrating linguistic morphology analysis.
* Supporting Sangam-era vocabulary and grammatical structures.
* Using real transformer attention weights.
* Developing model-based token attribution.
* Adding retrieval-augmented cultural context.
* Building a curated corpus of classical Tamil texts.
* Evaluating translation quality against expert-annotated references.
* Adding multilingual output support.

---

## 14. Design Principle

The central design principle of the project is to separate:

```text
Translation
     +
Explanation
     +
Visualization
```

This makes it possible to improve the translation component independently while retaining the explainability and user-interface layers.
