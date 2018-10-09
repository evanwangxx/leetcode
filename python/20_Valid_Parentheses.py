class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = []
        for index in range(len(s)):
            item = s[index]

            if item == "{" or item == "(" or item == "[" or len(x) == 0:
                x.append(item)
            else:
                p = x.pop()
                if (item == "}" and p != "{") \
                        or (item == "]" and p != '[') \
                        or (item == ")" and p != "("):
                    return False

        return False if len(x) != 0 else True



if __name__ == "__main__":

    x = "[]),[()],{{}))".split(",")

    for i in x:
        test = Solution().isValid(i)
        print(test)