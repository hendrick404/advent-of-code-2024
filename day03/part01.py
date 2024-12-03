import re


def part01(input_str: list[str]):
    result = 0
    regex = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    for line in input_str:
        for match in regex.finditer(line):
            result += int(match.group(1)) * int(match.group(2))
    return result


if __name__ == "__main__":
    with open("day03/input", "r", encoding="utf-8") as input_file:
        test_input = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
        print(f"Test Expected 161 got {part01(test_input)}")
        print(f"Solution {part01(input_file.readlines())}")
