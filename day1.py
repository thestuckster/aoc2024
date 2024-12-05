import helper

# NOTE: hasn't been converted to smart runner
def run(file_path: str) -> int:
    content = helper.read_input(file_path)
    lines = content.split("\n")

    # distances = _find_shortest_distances(lines)
    occurances = build_occurances(lines)

    simularities = []
    for key, value in occurances.items():
        simularities.append(key * value)

    return sum(simularities)


def build_occurances(lines):
    occurances = {}
    l1, l2 = _parse_input(lines)
    for i in range(0, len(l1)):
        x = l1[i]

        for j in range(0, len(l2)):
            y = l2[j]

            if int(x) == int(y):
                occurances[int(x)] = occurances.get(int(x), 0) + 1
    return occurances


def _parse_input(lines):
    l1 = []
    l2 = []
    for line in lines:
        parts = line.split("   ")
        l1.append(parts[0])
        l2.append(parts[1])

    return l1, l2


def _find_shortest_distances(lines):
    distances = []
    l1, l2 = _parse_input(lines)
    while len(l1) > 0 and len(l2) > 0:
        min1 = min(l1)
        min2 = min(l2)

        l1.remove(min1)
        l2.remove(min2)

        if min1 > min2:
            distances.append(int(min1) - int(min2))
        elif min1 < min2:
            distances.append(int(min2) - int(min1))
    return distances