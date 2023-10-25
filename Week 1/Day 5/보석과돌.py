def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum(s in jewels for s in stones)


jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels,stones))