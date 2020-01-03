# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def find_common_between_string(cs, y):
    if not cs or not y:
        return ""
    cm = ""
    for i in range(min(len(cs), len(y))):
        if cs[i] == y[i]:
            cm += cs[i]
        else:
            return cm
    return cm


def find_common_prefix(input_list):
    common_prefix = input_list[0]
    for i in range(1, len(input_list)):
        this = input_list[i]
        common_prefix = find_common_between_string(common_prefix, this)
    return common_prefix


t1 = ["flower", "flow", "flight"]
t2 = ["dog", "racecar", "car"]

print(find_common_prefix(t1))
print(find_common_prefix(t2))