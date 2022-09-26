#!/bin/python3
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):

  word_height = []
  for i in word:
    word_height.append(h[ord(i) - 97])
  print(max(word_height) * len(word))


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
