import re
from typing import Set


def load_text_from_file(path: str) -> str:
	try:
		with open(path, 'r', encoding='utf-8') as f:
			return f.read()
	except Exception:
		return ''


def tokenize_to_set(text: str) -> Set[str]:
	# extract word tokens, normalize to lowercase
	tokens = re.findall(r"\b[\w']+\b", text.lower())
	return set(tokens)


def display_sample(title: str, s: Set[str], limit: int = 20) -> None:
	print(f"{title} (count = {len(s)}):")
	if not s:
		print("  (none)")
		print()
		return
	sample = sorted(s)[:limit]
	for w in sample:
		print(f"  - {w}")
	if len(s) > limit:
		print(f"  ... and {len(s)-limit} more")
	print()


def main():
	print("Vocabulary Analyzer for Two Books")

	a_path = input("Enter file path for Book A (leave blank to use example): ").strip()
	b_path = input("Enter file path for Book B (leave blank to use example): ").strip()

	if a_path:
		a_text = load_text_from_file(a_path)
		if not a_text:
			print(f"Warning: could not read '{a_path}'. Using empty text for Book A.")
	else:
		a_text = (
			"Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, "
			"and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."
		)

	if b_path:
		b_text = load_text_from_file(b_path)
		if not b_text:
			print(f"Warning: could not read '{b_path}'. Using empty text for Book B.")
	else:
		b_text = (
			"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, "
			"it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness."
		)

	a_set = tokenize_to_set(a_text)
	b_set = tokenize_to_set(b_text)

	intersection = a_set & b_set
	only_a = a_set - b_set
	only_b = b_set - a_set
	union = a_set | b_set

	print()
	display_sample("Unique words in Book A", a_set)
	display_sample("Unique words in Book B", b_set)
	print(f"Common words (intersection) count: {len(intersection)}")
	display_sample("Common words (intersection)", intersection)
	display_sample("Words only in Book A (A - B)", only_a)
	display_sample("Words only in Book B (B - A)", only_b)

	print(f"Total unique words across both books (union): {len(union)}")


if __name__ == '__main__':
	main()
