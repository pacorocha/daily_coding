import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    temp_grid = []
    for string in grid:
        temp = [string[i] for i in range(len(string))]
        temp.sort(reverse=False)
        temp_grid.append(temp)
        for col in zip(*temp_grid):
            for i in range(len(col) - 1):
                if col[i] > col[i + 1]:
                    return "NO"
    return "YES"


if __name__ == '__main__':
    grid = ["eabcd",
            "fghij",
            "olkmn",
            "trpqs",
            "xywuv"]

    grid2 = ["eksdi",
             "cosmq",
             "dbcea",
             "sdlks "]

    result = gridChallenge(grid2)

    print(result)
