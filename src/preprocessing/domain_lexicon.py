
class DomainLexicon:
    """Domain-specific vocabulary for Ancient Tamil interpretation."""

    def __init__(self):
        self.lexicon = {
            "யாதும்": "every",
            "ஊரே": "place",
            "யாவரும்": "everyone",
            "கேளிர்": "kin",
            "கற்றது": "learned",
            "கல்லாதது": "not learned",
            "உலகளவு": "as vast as the world",
            "பகவன்": "divine being",
        }

    def apply(self, text: str) -> str:
        """
        Add English contextual meanings to recognized Tamil terms.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")

        enriched_text = text

        for word, meaning in self.lexicon.items():
            annotation = f"{word} ({meaning})"
            enriched_text = enriched_text.replace(word, annotation)

        return enriched_text
