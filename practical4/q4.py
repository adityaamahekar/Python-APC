def get_names(prompt):
	s = input(prompt).strip()
	if not s:
		return set()
	return {x.strip() for x in s.split(',') if x.strip()}


def print_list(title, items):
	print(f"{title}:")
	if not items:
		print("  (none)")
	else:
		for name in sorted(items):
			print(f"  - {name}")
	print()


def main():
	print("Employee Involvement Analysis")
	a = get_names("Enter Project A employees (comma-separated): ")
	b = get_names("Enter Project B employees (comma-separated): ")

	if not a and not b:
		a = {"Ravi", "Maya", "Sonia", "Karan"}
		b = {"Sonia", "Peter", "Maya", "Lina"}
		print("\nUsing example data:\n")

	print_list("Project A", a)
	print_list("Project B", b)

	inter = a & b
	only_a = a - b
	only_b = b - a
	union = a | b
	only_one = a ^ b

	print_list("Employees in both projects (intersection)", inter)
	print_list("Employees only in Project A (A - B)", only_a)
	print_list("Employees only in Project B (B - A)", only_b)
	print_list("Employees in only one project (symmetric difference)", only_one)
	print_list("Total unique employees (union)", union)


if __name__ == '__main__':
	main()
