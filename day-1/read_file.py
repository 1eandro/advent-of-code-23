import sys
import re
def read_file():
    total_sum = 0
    for line in sys.stdin:
        first_digit = re.search(r'\d', line)
        first_digit = first_digit.group(0) if first_digit else None
        last_digit = re.findall(r'\d', line)[-1] if re.search(r'\d', line) else None
        number = int(str(first_digit) + str(last_digit))
        total_sum += number
    print(total_sum)
read_file() 
import re