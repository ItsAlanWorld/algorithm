import string
from pprint import pprint

text = 'hello, this is sparta'

counter = {}
# 21 번 연산
for char in text:
    if not char.isalpha():
        continue
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
pprint(counter)
