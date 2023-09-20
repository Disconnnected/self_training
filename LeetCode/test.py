def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_length = len(strs[0])
    for word in strs:
        if not word:
            return ""
        if len(word) < min_length:
            min_length = len(word)
    for i in range(min_length):
        char = strs[0][:i]
        for word in strs:
            if word[:i] != char:
                if i == 0:
                    return ""
                return strs[0][:i - 1]





x = longestCommonPrefix(["dog","racecar","car"])
print(x)