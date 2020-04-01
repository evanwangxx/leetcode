# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,
# there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like:
# "Hi, A. Do you know B?" to get information of whether A knows B.
# You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B.
# Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party.
# Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
#
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
#
# Example1:
#       Input: graph = [[1,1,0],
#                       [0,1,0],
#                       [1,1,1]]
#       Output: 1
#       Explanation: There are three persons labeled with 0, 1 and 2.
#                    graph[i][j] = 1 means person i knows person j,
#                    otherwise graph[i][j] = 0 means person i does not know person j.
#                    The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
#
# Example2:
#       Input: graph = [[1,0,1],
#                       [1,1,0],
#                       [0,1,1]]
#       Output: -1
#       Explanation: There is no celebrity.


# 解题思路
#   设待定名人candidate为0， 遍历每一个人，candidate认识另一个人i，说明他不是名人，把i变成名人。
#   最后再判断是不是所有人都认识他，而他不认识所有人
#   为什么第一步能找到可能的名人（出度可能为0）证明：
#       反证法： 假如找到candidate的不是名人，说明出度不为0。
#       但若该candidate出度不为0，则轮到candidate的时候一定会转移，矛盾。
#
# 那有没有可能漏掉名人呢？答案是否定的，
# 因为名人一定不认识其他人，并且其他人都是认识他，迭代了n次之后，最后会收敛到一定是名人。

def knows(a: int, b: int) -> bool:
    return

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = []
        for p1 in range(n):
            if self.is_celebrity(p1, n):
                celebrity.append(p1)

        return celebrity[0] if len(celebrity) == 1 else -1

    def is_celebrity(self, p, n):
        for i in range(n):
            if i == p:
                continue
            print(p, i, knows(p, i))
            if knows(p, i) or not knows(i, p):
                return False
        return True
