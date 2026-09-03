server_ip = ("192", "168", "1", "100")
"""
Project Employee Analysis (practical4/q3.py)

This script manages two projects' employee lists using Python sets
and displays:
 - employees working on both projects (intersection)
 - employees working only on one project (difference / symmetric difference)
 - total unique employees across both projects (union)

Usage: run the script and enter comma-separated names for each project.
If both inputs are left blank, example data will be used.
"""

def parse_input(prompt):
    raw = input(prompt).strip()
    if not raw:
        return set()
    return {name.strip() for name in raw.split(",") if name.strip()}


def display_set(title, s):
    print(f"{title}: ")
    if not s:
        print("  (none)")
    else:
        for name in sorted(s):
            print(f"  - {name}")
    print()


def main():
    print("Project Employee Analysis")
    print("Enter employee names separated by commas. Leave blank to use example data.")
    a = parse_input("Project A employees: ")
    b = parse_input("Project B employees: ")

    # If both empty, provide example data
    if not a and not b:
        a = {"Alice", "Bob", "Charlie", "David"}
        b = {"Charlie", "Eve", "Frank", "Bob"}
        print("\nNo input provided — using example sets:\n")

    display_set("Project A", a)
    display_set("Project B", b)

    intersection = a & b
    only_a = a - b
    only_b = b - a
    only_one = a ^ b  # symmetric difference
    union = a | b

    display_set("Employees working on both projects (intersection)", intersection)
    display_set("Employees only in Project A (A - B)", only_a)
    display_set("Employees only in Project B (B - A)", only_b)
    display_set("Employees working only on one project (symmetric difference)", only_one)
    display_set("Total unique employees across both projects (union)", union)


if __name__ == "__main__":
    main()

allowed_ips = ["192.168.1.10", "192.168.1.20"]

def update_allowed_ips():
    ip = input("Enter new allowed IP: ")
    allowed_ips.append(ip)
    print("IP added successfully.")

def display_configuration():
    print("\nServer Configuration")
    print("Server IP :", ".".join(server_ip))
    print("Allowed IPs :", allowed_ips)

display_configuration()

update_allowed_ips()

print("\nTrying to update Server IP...")
print("Server IP cannot be changed because it is stored as a tuple.")

display_configuration()