
from src.preprocessing.ancient_normalizer import AncientTamilNormalizer
from src.preprocessing.domain_lexicon import DomainLexicon
from src.translation.indictrans_model import IndicTranslator


class TranslationPipeline:
    """Main processing pipeline for Ancient Tamil interpretation."""

    def __init__(self):
        self.normalizer = AncientTamilNormalizer()
        self.lexicon = DomainLexicon()
        self.translator = IndicTranslator()

    def run(self, text: str) -> str:
        """
        Normalize and translate Ancient Tamil text.

        Translation is performed on normalized Tamil text so that
        domain annotations do not interfere with phrase matching.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")

        if not text.strip():
            return "Please provide Tamil text for interpretation."

        normalized = self.normalizer.normalize(text)

        translated, _ = self.translator.translate(normalized)

        if not translated or len(translated.strip()) < 5:
            return "Interpretation unclear — possible poetic meaning."

        return translated.strip()

    def enrich(self, text: str) -> str:
        """
        Add domain-specific English annotations to Tamil terms.

        This is intended for explainability and analysis rather than
        being used directly as the translation input.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")

        normalized = self.normalizer.normalize(text)
        return self.lexicon.apply(normalized)
