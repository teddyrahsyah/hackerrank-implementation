#!/bin/python3
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    high_counter = 0
    low_counter = 0

    highest_record = scores[0]
    lowest_record = scores[0]

    for i in scores:
      if (i > highest_record):
        highest_record = i
        high_counter += 1

      if (i < lowest_record):
        lowest_record = i
        low_counter += 1

    print(f"{high_counter} {low_counter}")

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
