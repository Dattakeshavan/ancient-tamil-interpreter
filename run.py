
import argparse

from src.pipeline.inference_pipeline import TranslationPipeline


def main():
    parser = argparse.ArgumentParser(
        description="Interpret Ancient Tamil text."
    )

    parser.add_argument(
        "--text",
        required=True,
        help="Ancient Tamil text to interpret.",
    )

    args = parser.parse_args()

    pipeline = TranslationPipeline()
    result = pipeline.run(args.text)

    print("\nAncient Tamil Interpretation")
    print("-" * 30)
    print(result)


if __name__ == "__main__":
    main()
