# 定义一个字符串的 Rotate 操作：
# abcdefgh, 在位置3 Rotate 后的结果是 defghabc。
# 给定一个长度为n的字符串以及Rotate 位置s，如何做Rotate 操作？ 使用 O(1) 空间如何做 Rotate 操作？


def rotate(s: str, i: int):
    if len(s) < i:
        return None
    while i != 0:
        s = s[1:] + s[0]
        i -= 1
    return s


if __name__ == "__main__":
    x = "abcdefg"
    for i in (0, 2, 4, 9):
        print(rotate(x, i))
