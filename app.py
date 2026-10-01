
import streamlit as st

from src.explainability.visualization import AttentionVisualizer
from src.explainability.word_importance import WordImportance
from src.pipeline.inference_pipeline import TranslationPipeline


st.set_page_config(
    page_title="Ancient Tamil Interpreter",
    page_icon="📜",
    layout="wide",
)


def calculate_confidence(
    translated: str,
    word_count: int,
) -> float:
    """Calculate a simple heuristic confidence score."""
    confidence = 0.85

    if "unclear" in translated.lower():
        confidence -= 0.20

    if word_count > 15:
        confidence -= 0.05

    return max(0.50, min(confidence, 0.95))


def main():
    st.title("📜 Ancient Tamil Interpreter")

    st.markdown(
        """
        Interpret classical Tamil verses with translation,
        contextual meaning, cultural context, and explainability.
        """
    )

    st.divider()

    user_input = st.text_area(
        "Enter Ancient Tamil Text",
        height=150,
        placeholder="உதாரணம்: யாதும் ஊரே யாவரும் கேளிர்",
    )

    analyze = st.button(
        "🔍 Analyze",
        type="primary",
        use_container_width=True,
    )

    if not analyze:
        return

    if not user_input.strip():
        st.warning("Please enter some Ancient Tamil text.")
        return

    try:
        pipeline = TranslationPipeline()

        # Normalize and translate the input.
        translation = pipeline.run(user_input)

        # Prepare enriched text for explainability.
        enriched_text = pipeline.enrich(user_input)

        st.subheader("📖 Interpretation")
        st.write(translation)

        st.subheader("🔎 Contextual Interpretation")
        st.info(
            "The input is interpreted using classical Tamil phrase "
            "patterns and Tamil-to-English translation."
        )

        st.subheader("💡 Literal Insight")
        st.write(enriched_text)

        st.subheader("✨ Refined Interpretation")
        st.write(translation)

        st.subheader("🏛️ Cultural Context")
        st.write(
            "The interpretation may reflect themes such as knowledge, "
            "ethics, human relationships, philosophy, or universal values."
        )

        # ---------------------------------------------------------
        # Word-level importance
        # ---------------------------------------------------------
        st.subheader("🧠 Word Importance")

        normalized = pipeline.normalizer.normalize(user_input)
        words = normalized.split()

        importance_model = WordImportance()
        importance_scores = importance_model.compute(
            words,
            translation,
        )

        for word, score in importance_scores:
            st.write(f"**{word}** — {score:.2f}")
            st.progress(score)

        # ---------------------------------------------------------
        # Structured attention visualization
        # ---------------------------------------------------------
        st.subheader("📊 Attention Visualization")

        source_tokens = normalized.split()
        target_tokens = translation.split()

        visualizer = AttentionVisualizer()

        attention_image = visualizer.plot(
            source_tokens,
            target_tokens,
        )

        st.image(
            attention_image,
            caption=(
                "Structured attention visualization "
                "(position-based proxy)"
            ),
            use_container_width=True,
        )

        # ---------------------------------------------------------
        # Confidence
        # ---------------------------------------------------------
        confidence = calculate_confidence(
            translation,
            len(words),
        )

        st.subheader("📈 Interpretation Confidence")

        st.progress(confidence)
        st.write(f"Confidence estimate: **{confidence:.0%}**")

        st.caption(
            "Confidence is a heuristic estimate and should not be "
            "interpreted as a calibrated model probability."
        )

    except Exception as error:
        st.error(
            "An error occurred while processing the text."
        )

        with st.expander("Technical details"):
            st.code(str(error))

    st.divider()

    st.caption(
        "Designed for classical Tamil interpretation. "
        "Accuracy may vary for highly complex poetry."
    )


if __name__ == "__main__":
    main()
