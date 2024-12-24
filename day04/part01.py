import numpy as np


STENCIL = np.array(['X', 'M', 'A', 'S'])


def part01(input_str):
    count = 0
    for i in range(input_str.shape[0]):
        for j in range(input_str.shape[1]):
            if j < input_str.shape[1] - STENCIL.shape[0] + 1:
                # Check horizontal
                if np.array_equiv(input_str[i,j:j+STENCIL.shape[0]], STENCIL):
                    count += 1
                # Check horizontal backward
                if np.array_equiv(input_str[i,j:j+STENCIL.shape[0]], STENCIL[::-1]):
                    count += 1
            if i < input_str.shape[0] - STENCIL.shape[0] + 1:
                # Check vertical downwards
                if np.array_equiv(input_str[i:i+STENCIL.shape[0],j], STENCIL):
                    count += 1
                # Check vertical upwards
                if np.array_equiv(input_str[i:i+STENCIL.shape[0],j], STENCIL[::-1]):
                    count += 1
            if i < input_str.shape[0] - STENCIL.shape[0] + 1 and j < input_str.shape[1] - STENCIL.shape[0] + 1:
                # Check diagonal from top left to bottom right
                if np.array_equiv(np.diag(input_str[i:i+STENCIL.shape[0],j:j+STENCIL.shape[0]]), STENCIL):
                    count += 1
                # Check diagonal from bottom right to top left
                if np.array_equiv(np.diag(input_str[i:i+STENCIL.shape[0],j:j+STENCIL.shape[0]]), STENCIL[::-1]):
                    count += 1
                # Check diagonal from bottom left to top right
                if np.array_equiv(np.diag(np.flipud(input_str[i:i+STENCIL.shape[0],j:j+STENCIL.shape[0]])), STENCIL):
                    count += 1
                # Check diagonal from top right to bottom left
                if np.array_equiv(np.diag(np.flipud(input_str[i:i+STENCIL.shape[0],j:j+STENCIL.shape[0]])), STENCIL[::-1]):
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
        print(f"Test Expected 18 got {part01(test_input)}")
        print(f"Solution {part01(np.array(list(map(list, input_file.readlines()))))}")
