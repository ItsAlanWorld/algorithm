s = "ac"
result = ""
length = len(s)

for x in range(len(s)):
    for _ in range(len(s)):
        text = s[x:length]
        if not text:
            break
        reversedS = ''.join(reversed(text))
        if text == reversedS :
            if len(text) > len(result):
                result = text
        print(text, x, length)
        length -= 1
    length = len(s)
print(result)

