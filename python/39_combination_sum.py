# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note: All numbers (including target) will be positive integers.
#       The solution set must not contain duplicate combinations.
# Example 1:
#       Input: candidates = [2,3,6,7], target = 7,
#       A solution set is:
#           [ [7],
#             [2,2,3] ]
# Example 2:
#       Input: candidates = [2,3,5], target = 8,
#       A solution set is:
#           [ [2,2,2,2],
#             [2,3,3],
#             [3,5] ]


class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        candidates = sorted(candidates)
        res = []
        self.backtrace_helper(candidates, [], 0, target, res)
        return res

    def backtrace_helper(self, candi, path, start_index, target, res):
        if target == 0:
            res.append(path[:])
        else:
            for i in range(start_index, len(candi)):
                if candi[i] > target:
                    break
                path.append(candi[i])
                self.backtrace_helper(candi, path, i, target-candi[i], res)
                path.pop()


x = [2,3,6,7]
print(Solution().combinationSum(x, 7))