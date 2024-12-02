def part02(input_str: list[str]):
    result = 0
    left: list[int] = []
    right: dict[int, int] = {}
    for line in input_str:
        left.append(int(line.split()[0].strip()))
        r = int(line.split()[1].strip())
        if r in right:
            right[r] += 1
        else:
            right[r] = 1
    for l in left:
        result += l * right[l] if l in right else 0
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
        print(f"Test Expected 31 got {part02(test_input)}")
        print(f"Solution {part02(input_file.readlines())}")
