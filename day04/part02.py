import numpy as np

STENCIL = np.array([['M','.','M'],
                     ['.','A','.'],
                     ['S','.','S']])
MASK = STENCIL == np.full((3,3), '.')


def repeat(f, n):
    def _f(x):
        for _ in range(n):
            x = f(x)
        return x
    return _f


def part02(input_str):
    count = 0
    for i in range(input_str.shape[0] - 2):
        for j in range(input_str.shape[1] - 2):
            for transformation in [repeat(np.rot90, i) for i in range(4)]:
                if (np.logical_or((input_str[i:i+3,j:j+3] == transformation(STENCIL)), MASK)).all():
                    count += 1
    return count


if __name__ == "__main__":
    with open("day04/input", "r", encoding="utf-8") as input_file:
        test_input = np.array(list(map(list, [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ])))
        print(f"Test Expected 9 got {part02(test_input)}")
        print(f"Solution {part02(np.array(list(map(list, input_file.readlines()))))}")
