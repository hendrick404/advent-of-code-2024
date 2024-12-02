def part01(input_str: list[str]):
    result = 0
    left = []
    right = []
    for line in input_str:
        left.append(int(line.split()[0].strip()))
        right.append(int(line.split()[1].strip()))
    for (l, r) in zip(sorted(left), sorted(right)):
        result += abs(l - r)
    return result


if __name__ == "__main__":
    with open("day01/input", "r", encoding="utf-8") as input_file:
        test_input = [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3"
        ]
        print(f"Test Expected 11 got {part01(test_input)}")
        print(f"Solution {part01(input_file.readlines())}")
