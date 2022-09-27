def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    charMap = {}
    for idx, char in enumerate(s):
        if charMap.get(s[idx]) == None:
            charMap[s[idx]] = t[idx]
        elif charMap.get(s[idx]) != t[idx]:
            return False
    return True

print(isIsomorphic("badc", "baba"))