def part01(input_str: list[str]):
    return len([x for x in input_str if safe(x)])


def safe(report: str):
    levels = [int(x.strip()) for x in report.split()]
    return (
        all(map(
            lambda e: e[0] > e[1] and e[0] <= e[1] + 3,
            zip(levels, levels[1:])
        )) or all(map(
            lambda e: e[0] < e[1] and e[0] >= e[1] - 3,
            zip(levels, levels[1:])
        ))
    )


if __name__ == "__main__":
    with open("input", "r", encoding="utf-8") as input_file:
        test_input = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"
        ]
        print(f"Test Expected 2 got {part01(test_input)}")
        print(f"Solution {part01(input_file.readlines())}")
