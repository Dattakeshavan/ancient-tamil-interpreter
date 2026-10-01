
class WordImportance:
    """Estimate word importance using lightweight linguistic heuristics."""

    KEY_CONCEPTS = (
        "நன்று",
        "தீது",
        "அறிவு",
        "உலக",
        "கற்று",
    )

    def compute(
        self,
        words: list[str],
        translated: str | None = None,
    ) -> list[tuple[str, float]]:
        """
        Calculate an importance score for each Tamil word.

        The score is a heuristic based on word length and the presence
        of selected domain-specific concepts. It is not a model-derived
        semantic importance score.
        """
        if not words:
            return []

        max_length = max(len(word) for word in words)

        if max_length == 0:
            return [(word, 0.0) for word in words]

        importance = []

        for word in words:
            score = len(word) / max_length

            if any(
                concept in word
                for concept in self.KEY_CONCEPTS
            ):
                score += 0.2

            score = min(score, 1.0)

            importance.append(
                (word, round(score, 2))
            )

        return importance
