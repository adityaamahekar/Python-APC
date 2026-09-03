import re
from collections import Counter


def analyze_text(text: str):
    # Normalize and extract words (letters, digits, underscore)
    words = re.findall(r"\b\w+\b", text.lower())
    total_words = len(words)
    freq = Counter(words)
    top3 = freq.most_common(3)
    vowel_count = sum(1 for ch in text.lower() if ch in "aeiou")

    return {
        "total_words": total_words,
        "frequencies": freq,
        "top3": top3,
        "vowel_count": vowel_count,
    }


def print_report(report):
    print(f"Total words: {report['total_words']}")
    print("\nWord frequencies:")
    if not report['frequencies']:
        print("  (none)")
    else:
        for word, count in report['frequencies'].most_common():
            print(f"  {word}: {count}")

    print("\nTop 3 most frequent words:")
    if not report['top3']:
        print("  (none)")
    else:
        for word, count in report['top3']:
            print(f"  {word}: {count}")

    print(f"\nTotal vowels in text: {report['vowel_count']}")


def main():
    print("Simple Text Analysis Tool")
    print("Enter a paragraph (press Enter for example text):\n")
    try:
        text = input().strip()
    except EOFError:
        text = ""

    if not text:
        text = (
            "Python is a versatile programming language. "
            "It is widely used for scripting, web development, and data analysis. "
            "Python's simple syntax makes it popular among beginners and experts alike."
        )
        print("\nUsing example text:\n")
        print(text)

    report = analyze_text(text)
    print("\nAnalysis Report:\n")
    print_report(report)


if __name__ == '__main__':
    main()
