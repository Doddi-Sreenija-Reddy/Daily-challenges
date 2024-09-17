def prefix(strs):
    if not strs:
        return ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))
    i = 0
    while i < min_length and first[i] == last[i]:
        i += 1
    if i == 0:
        return ""
    return first[:i]
s = input()
words = s.split()
prefix(words)
