import re

# Once again changed runner format to run both parts. this signature is required going forward
def part_one(data: list[str]):
    pattern = r"mul\((\d+),(\d+)\)"

    total = 0
    for line in data:
        matches = re.findall(pattern, line)
        for match in matches:
            total += (int(match[0]) * int(match[1]))

    print(total)


def part_two(data: list[str]):
    print("TODO")