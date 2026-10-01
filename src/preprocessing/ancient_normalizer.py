
import regex as re
class AncientTamilNormalizer:
    """Normalize Ancient Tamil text before interpretation."""

    def __init__(self):
        self.replacements = {
            "ஜ்ஞ": "ஞ",
            "ஸ்ரீ": "ஸ்ரி",
        }

    def normalize(self, text: str) -> str:
        """
        Normalize whitespace, remove selected punctuation,
        and apply known character replacements.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")

        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[॥|]", "", text)

        for source, replacement in self.replacements.items():
            text = text.replace(source, replacement)

        return text.strip()
