
class AttentionExtractor:
    """Safely extract decoder attention from model outputs."""

    def extract(self, outputs):
        """
        Extract the final decoder attention layer when available.

        Returns:
            Attention matrix as a NumPy-compatible array, or None
            when attention data is unavailable.
        """
        if outputs is None:
            return None

        try:
            attentions = outputs.decoder_attentions

            if not attentions:
                return None

            last_layer = attentions[-1][0]

            # Average across attention heads.
            avg_attention = last_layer.mean(dim=0).cpu().numpy()

            return avg_attention

        except (AttributeError, IndexError, TypeError):
            return None
