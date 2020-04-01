"""
5. Longest Palindromic Substring
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


class Solution:
    def longestPalindrome_old(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(set(s)) == 1:
            return s
        elif len(s) == 2 and s[0] != s[1]:
            return s[0]

        max_list = []
        for i in range(1, len(s)-1):
            left_index = i-1
            right_index = i+1

            tmp_lift = i
            tmp_right = i
            sem = False

            while left_index >= 0 and right_index < len(s):
                left = s[left_index]
                right = s[right_index]

                if left == right:
                    tmp_lift = left_index
                    tmp_right = right_index
                    sem = True
                elif left == s[tmp_lift] and not sem:
                    tmp_lift = left_index
                elif right == s[tmp_right] and not sem:
                    tmp_right = right_index
                else:
                    break

                left_index = tmp_lift - 1
                right_index = tmp_right + 1

            tmp_p = s[tmp_lift:tmp_right + 1]
            max_list = tmp_p if len(max_list) < len(tmp_p) else max_list

        return ''.join(max_list)

    def longestPalindrome(self, s):
        if not s:
            return 0
        elif len(s) == 1:
            return 1

        tmp_length = 1
        max_length = 1
        for p in range(1, len(s)-1):
            i = p - 1
            j = p + 1
            while i >= 0 and s[i] == s[p]:
                i -= 1
                tmp_length += 1
            while j < len(s) and s[j] == s[p]:
                j += 1
                tmp_length += 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                tmp_length += 2
                i -= 1
                j += 1
            max_length = max(max_length, tmp_length)
            tmp_length = 1
        return max_length


t1 = "222020221"
t2 = "aaaa"
t3 = "caba"
t4 = "abba"
t5 = "asdsa"
t6 = "abbd"

s = Solution()
for i in [t1,t2,t3,t4,t5,t6]:
    str = s.longestPalindrome_old(i)
    lens = s.longestPalindrome(i)
    print(len(str), lens)
