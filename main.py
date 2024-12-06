import os
import importlib

import helper


def main():
    problem_input = get_input()
    day_str = get_current_day()
    runner = importlib.import_module(day_str)
    runner.part_one(problem_input)
    runner.part_two(problem_input)


def get_input() -> list[str]:
    # assume run is test unless specified
    is_test = True if os.environ.get("IS_TEST", "True").lower() == "true" else False
    return helper.read_input(get_day(), test=is_test)

def get_day() -> int:
    # if no day is supplied assume you're running the most recent problem in the data folder
    day_str = os.getenv("DAY", get_current_day())
    if "day" in day_str:
        return int(day_str.split("day")[1])
    return int(day_str)


def get_current_day() -> str:
   return os.listdir("data").pop()


if __name__ == "__main__":
    main()
