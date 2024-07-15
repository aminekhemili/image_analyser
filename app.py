import numpy as np
from numpy._core._multiarray_umath import index

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

titles = ["bananas", "strawberry", "kiwi", "manga", "lemon", "dragonfruit", "ananas", "apple", "cherry"]
for x in range(len(numbers)):
    print(str(titles[x]),numbers[x])