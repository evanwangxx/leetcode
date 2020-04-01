# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example:
#   Input: "23"
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note: Although the above answer is in lexicographical order,
#       your answer could be in any order you want.

class Solution:
    phone_button = {"2": "a,b,c".split(","),
                    "3": "d,e,f".split(","),
                    "4": "g,h,i".split(","),
                    "5": "j,k,l".split(","),
                    "6": "m,n,o".split(","),
                    "7": "p,q,r,s".split(","),
                    "8": "t,u,v".split(","),
                    "9": "w,x,y,z".split(",")}

    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []
        if len(digits) == 1:
            return self.phone_button[digits]

        result = self.phone_button[digits[0]]
        for d in digits[1:]:
            temp = []
            for r in result:
                for dc in self.phone_button[d]:
                    temp.append(r + dc)
            result.extend(temp)
        result = [x for x in result if len(x) == len(digits)]
        return result

if __name__ == "__main__":
    x = Solution().letterCombinations("2")
    print(x)