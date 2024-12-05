import helper

# NOTE: method signature required for smart runner
def run(reports: list[str]):
    safe_reports = 0

    for report in reports:
        levels = report.split(" ")
        is_increasing = validate_increasing(levels)
        is_decreasing = validate_decreasing(levels)

        if is_increasing or is_decreasing:
            safe_reports += 1

    return safe_reports

def validate_increasing(levels: list[str]) -> bool:
    removed = False

    for i in range(1, len(levels)):
        current = int(levels[i])
        last = int(levels[i - 1])

        if current > last:
            distance = current - last
            if distance < 1 or distance > 3:
                if not removed and can_get_ahead(i, levels):
                    ahead = int(levels[i+1])
                    removed = remove_bad_level(levels, last, current, ahead)
                else:
                    return False
        else:
            return False

    return True

def validate_decreasing(levels: list[str]) -> bool:
    removed = False
    for i in range(1, len(levels)):
        current = int(levels[i])
        last = int(levels[i - 1])

        if current < last:
            distance = last - current
            if distance < 1 or distance > 3:
                if not removed and can_get_ahead(i, levels):
                    ahead = levels[i+1]
                    removed = True
                else:
                    return False
        else:
            return False

    return True

def can_get_ahead(current: int, levels: list[str]) -> bool:
    return current + 1 < len(levels) - 1

def distance_in_bounds(left: int, right: int) -> bool:
    distance = left - right
    return distance < 1 or distance > 3


def remove_bad_level(levels: list[str], last: int, current: int, ahead: int, decreasing: bool = False) -> bool:
    if decreasing:
        if distance_in_bounds(last, ahead):
            levels.remove(str(current))
            return True
    else:
        if distance_in_bounds(ahead, last):
            levels.remove(str(current))
            return True

    return False