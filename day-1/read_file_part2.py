import sys


def read_file():
    total_sum = 0
    for line in sys.stdin:
        word_to_number = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        tokens = word_to_number.keys()

        positions = {
            line.find(token): token for token in tokens if line.find(token) != -1
        }
        first_digit = word_to_number[positions[min(positions)]]

        r_positions = {
            line.rfind(token): token for token in tokens if line.rfind(token) != -1
        }
        last_digit = word_to_number[r_positions[max(r_positions)]]

        number = int(str(first_digit) + str(last_digit))
        total_sum += number

        print(f"number: {number} :: sum: {total_sum}")
    print(f"The total is: {total_sum}")


read_file()
