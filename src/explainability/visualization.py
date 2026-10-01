
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class AttentionVisualizer:
    """Generate structured attention visualizations for interpretation."""

    def __init__(self, output_dir: str = "outputs/attention_maps"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_structured_attention(
        self,
        src_len: int,
        tgt_len: int,
    ) -> np.ndarray:
        """
        Generate a structured attention-like matrix.

        This is a visualization proxy based on token-position alignment.
        It is not extracted from a trained transformer model.
        """
        if src_len <= 0 or tgt_len <= 0:
            return np.empty((tgt_len, src_len))

        attention = np.zeros((tgt_len, src_len), dtype=float)

        for i in range(tgt_len):
            for j in range(src_len):
                distance = abs(
                    (i / tgt_len) - (j / src_len)
                )
                attention[i, j] = np.exp(-distance * 5)

        # Small amount of noise to make the visualization less uniform.
        noise = np.random.rand(tgt_len, src_len) * 0.1
        attention += noise

        max_value = attention.max()

        if max_value > 0:
            attention /= max_value

        return attention

    def plot(
        self,
        src_tokens: list[str],
        tgt_tokens: list[str],
    ) -> str:
        """
        Create and save an attention visualization.

        Returns:
            Path to the generated PNG image.
        """
        if not src_tokens or not tgt_tokens:
            raise ValueError(
                "Source and target token lists must not be empty."
            )

        attention = self.generate_structured_attention(
            len(src_tokens),
            len(tgt_tokens),
        )

        figure, axis = plt.subplots(figsize=(10, 6))

        image = axis.imshow(
            attention,
            aspect="auto",
        )

        figure.colorbar(image, ax=axis)

        axis.set_xticks(range(len(src_tokens)))
        axis.set_xticklabels(
            src_tokens,
            rotation=90,
        )

        axis.set_yticks(range(len(tgt_tokens)))
        axis.set_yticklabels(tgt_tokens)

        axis.set_xlabel("Source Tokens")
        axis.set_ylabel("Target Tokens")
        axis.set_title("Structured Attention Visualization")

        figure.tight_layout()

        filename = (
            self.output_dir
            / f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.png"
        )

        figure.savefig(filename, dpi=150)
        plt.close(figure)

        return str(filename)
