def isAnagram(s, t):
    if len(s) != len(t):
        return False
    else:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
s = "rat"
t = "car"
print(isAnagram(s, t))

