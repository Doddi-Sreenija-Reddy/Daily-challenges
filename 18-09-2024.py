def anagrams(words):
    anagram_dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(word)
    return list(anagram_dict.values())  
s = input()
words = s.split()
a = anagrams(words)
print(a)
