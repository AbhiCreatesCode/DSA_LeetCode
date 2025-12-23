# def lengthOfLongestSubstring(self, s: str) -> int:
#         res = ""
#         for i in range(len(s)):
#             for j in range(i):
#                 if s[i:j] == res:
#                     res = s[i:j]
#         return res
# s = input()
# a = lengthOfLongestSubstring(s)
# print(a)
s ="abcabc"
res = ""
for i in range(len(s)):
    for j in range(i):
        if s[i:j] == res:
            print(s[:j])