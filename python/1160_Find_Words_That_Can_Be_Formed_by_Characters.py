# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
#
# Example 1:
#       Input: words = ["cat","bt","hat","tree"], chars = "atach"
#       Output: 6
#       Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
#
# Example 2:
#       Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
#       Output: 10
#       Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

import copy


class Solution:
    def countCharacters(self, words, chars):
        dic = {}
        for c in chars:
            if c not in dic.keys():
                dic[c] = 1
            else:
                dic[c] += 1

        res = []
        for w in words:
            dic_copy = copy.deepcopy(dic)
            tmp = []
            i = 0
            while i < len(w):
                if w[i] in dic_copy.keys() and dic_copy[w[i]] != 0:
                    dic_copy[w[i]] -= 1
                    tmp.append(w[i])
                    i += 1
                else:
                    tmp = []
                    i = len(w)
            res.extend(tmp)
        return len(res)


x = ["cat","bt","hat","tree"]
chars = "atach"
print(Solution().countCharacters(x, chars))

x = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(Solution().countCharacters(x, chars))