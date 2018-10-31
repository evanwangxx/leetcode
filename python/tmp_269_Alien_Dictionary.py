# 269 Alien Dictionary

x = ["wrt", "wrf", "er", "ett", "rftt"]
y = ["w", "t", "tt", "tw"]
z = ["ac", "ab", "b"]
s = ["wrt", "wrtkj"]


def alienOrder(words):

    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    if len(chars) == 1:
        return chars.pop()

    ind = ""
    if chars - set("".join(less)):
        for i in list(chars - set("".join(less))):
            ind += i

    if not less:
        return max(words, key=len)

    dic = {}
    for i in chars:
        for c in less:
            if c[0] == i:
                if i not in dic.keys():
                    dic[i] = c[1]

    if not list(set(dic.keys()) - set(dic.values())):
        return ""
    else:
        r = ""
        root = list(set(dic.keys()) - set(dic.values()))[0]
        k = root
        while k in dic.keys():
            r += dic[k]
            k = dic[k]

        return root + r + ind