#!/bin/python3
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairs = 0
    dup = {x for x in ar if ar.count(x) > 1}

    for i in dup:
      if (ar.count(i) % 2 == 0):
        pairs += ar.count(i) / 2
      else:
        pairs += (ar.count(i)-1) / 2
    print(int(pairs))


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
