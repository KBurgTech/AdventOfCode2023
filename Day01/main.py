import re

from helper.file_helper import load_input_as_lines


def part1(input):
    total = 0
    for line in input:
        digits = ''.join(filter(str.isdigit, line))
        total += int(digits[0] + digits[-1])

    print(f"Total Part 1 {total}")


def part2(input):
    total = 0
    digit_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    re_names = '|'.join(digit_names)
    for line in input:
        digits = []
        for m in re.finditer(r'(?=(\d{1}|' + f"{re_names}))", line):
            if len(m.groups()) == 0:
                continue
            digits.append(m.groups()[0] if str.isdigit(m.groups()[0]) else str(digit_names.index(m.groups()[0]) + 1))
        number = digits[0] + digits[-1]
        total += int(number)

    print(f"Total Part 2 {total}")


def main():
    lines = load_input_as_lines("input.txt")
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
